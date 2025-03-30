from django.contrib import admin
from django.urls import path
from bot.views import user_registration, get_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration', user_registration, name='user_registration'),
    path('api/user/<int:user_id>/', get_user_info)
]
