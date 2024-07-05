from django.urls import path
from users.views import user_list, add_user

urlpatterns = [
    path('', user_list, name='users'),
    path('add/', add_user, name='add_user'),
]
