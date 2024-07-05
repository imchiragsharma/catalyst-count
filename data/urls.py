from django.urls import path
from data.views import upload_view

urlpatterns = [
    path('upload/', upload_view, name='upload'),

]
