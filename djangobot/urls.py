from django.contrib import admin
from django.urls import path
from bot.views import user_registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration', user_registration, name='user_registration')

]
