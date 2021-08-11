from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Q, query
from django.views import generic
from .models import Order, Worker, OrderWork

class IndexView(generic.TemplateView):
    template_name = 'index.html'

from .forms import QueryDatePeriodForm, PaginateByForm

class OrderListView(generic.ListView):
    '''依頼一覧ビュー'''
    model = Order
    paginate_by = 25

    def get_queryset(self):
        '''グローバル検索の値を取得'''
        search = self.request.GET.get('search')

        '''期間検索の値を取得'''
        query_start_year = self.request.GET.get('start_period_year')
        query_start_month = self.request.GET.get('start_period_month')
        query_start_day = self.request.GET.get('start_period_day')
        query_end_year = self.request.GET.get('end_period_year')
        query_end_month = self.request.GET.get('end_period_month')
        query_end_day = self.request.GET.get('end_period_day')

        if search:
            '''グローバル検索'''
            return Order.objects.filter(
                Q(order_number__icontains=search) | Q(management_number__icontains=search) | Q(management_code__icontains=search) | Q(name__icontains=search) | Q(work_content__icontains=search)
            )
        elif query_start_year and query_start_month and query_start_day and query_end_year and query_end_month and query_end_day:
            '''期間検索'''
            from datetime import date
            start_date = date(int(query_start_year), int(query_start_month), int(query_start_day))
            end_date = date(int(query_end_year), int(query_end_month), int(query_end_day))
            return Order.objects.filter(order_date__range=(start_date, end_date))
        else:
            return Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_date_period_form'] = QueryDatePeriodForm(self.request.GET)
        context['paginate_by_form'] = PaginateByForm(self.request.session)
        return context

    def get_paginate_by(self, queryset):
        if 'paginate_by' in self.request.GET:
            self.request.session['paginate_by'] = int(self.request.GET.get('paginate_by'))
        if 'paginate_by' in self.request.session:
            return self.request.session.get('paginate_by')
        else:
            return int(self.request.GET.get('paginate_by', self.paginate_by))

class OrderDetailView(generic.DetailView):
    '''依頼詳細ビュー'''
    model = Order

from .forms import OrderCreateForm

class OrderCreateView(generic.CreateView):
    '''依頼作成ビュー'''
    model = Order
    form_class = OrderCreateForm

    def get_success_url(self):
        return reverse('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True
        return context

class OrderUpdateView(generic.UpdateView):
    '''依頼更新ビュー'''
    model = Order
    form_class = OrderCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

class OrderDeleteView(generic.DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

import io, csv
from datetime import datetime
from .forms import CSVUploadForm
from django.shortcuts import render

class CSVImport(generic.FormView):
    '''CSVファイルをインポート'''
    template_name = 'myapp/import.html'
    form_class = CSVUploadForm
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        csv_file = io.TextIOWrapper(form.cleaned_data['file'], encoding='shift-jis')
        if csv_file.name.lower().endswith('.csv'):
            reader = csv.reader(csv_file, delimiter=',')
        elif csv_file.name.lower().endswith('.tsv'):
            reader = csv.reader(csv_file, delimiter="\t")

        line = [row for row in reader]
        if line[0][0] != '依頼LotNo.':
            context = {
                'form': form,
                'message': 'ファイルのインポートに失敗しました。インポートするファイルを確認してください。'
            }
            # エラーメッセージと一緒にもとのフォームを返す
            return render(self.request, 'myapp/import.html', context)

        line.pop(0) # ヘッダー行を削除
        for row in line:
            print(row)
            post, created = Order.objects.get_or_create(
                pk=row[1],
                order_date=datetime.strptime(row[23], '%Y/%m/%d'),
                management_number=row[8],
                management_code=row[17],
                name=row[13],
                lot_number=row[14],
                work_content=row[18],
                unit_price=float(row[19]),
                number=int(float(row[9].replace(',', '', row[9].count(',')))),
                )
            print(post)
            print(created)

        return super().form_valid(form)

from django.http import HttpResponse, request

def csv_export(request):
    '''リストをCSVファイルにエクスポート'''
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="orderlist.csv"'} ,
        charset='shift-jis',
    )

    writer = csv.writer(response)
    writer.writerow(['依頼No.', '依頼日', '管理番号', '管理コード', '品名', 'ロットNo.', '作業内容', '単価', '数量',])
    for order in Order.objects.all():
        writer.writerow(
            [
                order.pk,
                order.order_date,
                order.management_number,
                order.management_code,
                order.name,
                order.lot_number,
                order.work_content,
                order.unit_price,
                order.number,
            ]
        )

    return response