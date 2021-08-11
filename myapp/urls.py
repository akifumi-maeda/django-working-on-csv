from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('orders', views.OrderListView.as_view(), name='order_list'),
    path('order/<str:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('create', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<str:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order/<str:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('import', views.CSVImport.as_view(), name='import'),
    path('export', views.csv_export, name='export'),
]
