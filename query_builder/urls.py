from django.urls import path
from .views import QueryBuilderView, query_builder, download_csv

urlpatterns = [
    path('', query_builder, name='query_builder'),
    path('api/query-builder/', QueryBuilderView.as_view() , name='query_builder_api'),
    path('api/download-csv/', download_csv, name='download_csv'),
]
