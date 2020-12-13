from django.urls import path
from . import views

app_name = 'paste'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:paste_id>/', views.paste, name='paste'),
]
