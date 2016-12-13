from django.conf.urls import url
from practice import views

urlpatterns = [
    url(r'^start_task/(?P<task_id>.+)/$', views.start_task, name='practice_start_task'),
    url(r'^recommend', views.recommend, name='practice_recommend'),
]
