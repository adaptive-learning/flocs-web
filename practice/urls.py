from django.conf.urls import url
from practice import views

urlpatterns = [
    url(r'^get_or_create_student$', views.get_or_create_student, name='practice_get_or_create_student'),
    url(r'^start_task/(?P<task_id>.+)/$', views.start_task, name='practice_start_task'),
    url(r'^see_instruction$', views.see_instruction, name='practice_see_instruction'),
    url(r'^recommend', views.recommend, name='practice_recommend'),
]
