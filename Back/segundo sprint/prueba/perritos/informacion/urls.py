from django.urls import path

from . import views

#URLConf
urlpatterns = [
    path('info/', views.info, name='nosotros')

]