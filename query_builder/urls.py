from django.urls import path
from query_builder.views import query_builder_view

urlpatterns = [
    path('query_builder/', query_builder_view, name='query_builder'),
]
