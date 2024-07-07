from django.urls import path
from .views import QueryBuilderView, query_builder

urlpatterns = [
    path('', query_builder, name='query_builder'),
    path('api/query-builder/', QueryBuilderView.as_view() , name='query_builder_api'),
]
