from django import forms
from django.core.validators import FileExtensionValidator

class CSVUploadForm(forms.Form):
    file = forms.FileField(
        label='アップロード',
        validators=[FileExtensionValidator(['csv', 'tsv',])],
        help_text='※拡張子が csv、tsv のファイルを選択してください。'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'order_date', 'management_number', 'management_code', 'name', 'lot_number', 'work_content', 'unit_price', 'number', 'section',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control mb-3"

from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class QueryDatePeriodForm(forms.Form):
    """日付期間検索フォーム"""
    error_css_class = 'error'

    start_period = forms.DateField(
        label='開始日',
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'},
            years=range(datetime.today().year, datetime.today().year - 9, -1)
            )
        )
    end_period = forms.DateField(
        label='終了日',
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-select'},
            years=range(datetime.today().year, datetime.today().year - 9, -1)
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        start_period = cleaned_data.get('start_period')
        end_period = cleaned_data.get('end_period')

        if start_period and end_period:
            if start_period > end_period:
                raise ValidationError(_('開始日は完了日よりも前の日付に設定して下さい。'))

class PaginateByForm(forms.Form):
    '''ユーザー指定ぺージネイション'''
    paginate_by = forms.ChoiceField(
        choices=(
            (10, '10'),
            (25, '25'),
            (50, '50'),
            (75, '75'),
            (100, '100'),
        ),
        required=True,
        widget=forms.widgets.Select(attrs={'class': 'form-select'},),

    )