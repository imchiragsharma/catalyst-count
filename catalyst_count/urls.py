from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/login/', permanent=False)),
    path('logout/',include('accounts.urls')),
    path('upload_data/', include('data.urls')),
    path('query_builder/', include('query_builder.urls')),
    path('users/', include('users.urls')),
]
# print(urlpatterns)
