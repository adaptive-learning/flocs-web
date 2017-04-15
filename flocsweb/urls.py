""" URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from users import views as users_views
from tasks import views as tasks_views
from practice import views as practice_views
from . import views


router = DefaultRouter()
router.register(r'users', users_views.UsersViewSet, base_name='user')
router.register(r'tasks', tasks_views.TaskViewSet, base_name='task')
router.register(r'categories', tasks_views.CategoryViewSet, base_name='category')
router.register(r'levels', tasks_views.LevelViewSet, base_name='level')
router.register(r'toolboxes', tasks_views.ToolboxViewSet, base_name='toolbox')
router.register(r'blocks', tasks_views.BlockViewSet, base_name='block')
router.register(r'instructions', tasks_views.InstructionViewSet, base_name='instruction')
router.register(r'students', practice_views.StudentsViewSet, base_name='student')
router.register(r'task_sessions', practice_views.TaskSessionsViewSet, base_name='task_session')
router.register(r'actions', views.ActionsViewSet)


urlpatterns = [
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/.*/$', 'flocsweb.views.wrong_api_call'),
    url(r'^accounts/profile', 'flocsweb.views.redirect_home'),
    url(r'^([^a].*)?$', 'flocsweb.views.frontend_app'),
]
