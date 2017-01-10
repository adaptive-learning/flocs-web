"""flocsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from users import views as users_views
from tasks import views as tasks_views
from practice import views as practice_views
from practice import urls as practice_urls

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', users_views.UsersViewSet, base_name='user')
router.register(r'tasks', tasks_views.TasksViewSet, base_name='task')
router.register(r'students', practice_views.StudentsViewSet, base_name='student')
router.register(r'task_sessions', practice_views.TaskSessionsViewSet, base_name='task_session')
router.register(r'practice', practice_views.PracticeViewSet, base_name='practice')

urlpatterns = [
    url(r'^api/auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/practice/', include(practice_urls)),
    url(r'^api/.*/$', 'flocsweb.views.wrong_api_call'),
    url(r'^accounts/profile', 'flocsweb.views.redirect_home'),
    url(r'^([^a].*)?$', 'flocsweb.views.frontend_app'),
]
