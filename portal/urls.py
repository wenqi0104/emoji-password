from django.urls import path

from portal.views import login, index, register

app_name = 'portal'

# 3 different pages: login, register and main page
urlpatterns = [
    path('', login, name='login'),
    path("main/", index, name='index'),
    path("register/", register, name='register'),
]