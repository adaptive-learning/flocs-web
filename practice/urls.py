from django.conf.urls import url
from practice import views

urlpatterns = [
    url(r'^start/$', views.start, name='practice_start'),
    url(r'^start_task/(?P<task_id>.+)/$', views.start_task, name='practice_start_task'),
]
