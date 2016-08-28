from django.conf.urls import url
from practice import views

urlpatterns = [
    url(r'^start/$', views.start, name='practice_start'),
    url(r'^start_task/(?P<task_id>[0-9]+)/$', views.start_task, name='practice_start_task'),
]
