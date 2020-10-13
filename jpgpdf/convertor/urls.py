from django.urls import path
from convertor import views

app_name = 'convertor'

urlpatterns = [
    path('', views.index_page.as_view(), name='index'),
    path('output<int:pk>', views.output_view.as_view(),name='output'),
    path('processed<int:pk>', views.processed.as_view(),name='processed'),
]