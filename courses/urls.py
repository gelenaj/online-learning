from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.topic_list, name='list'),
    path('<int:topic_pk>/<int:course_pk>',views.course_detail, name='course'),
    path('<int:pk>/',views.topic_detail, name='detail'),
]
