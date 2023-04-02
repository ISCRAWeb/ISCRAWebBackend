from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("login/", login),
    path("change_pass/", change_password),
    path("change_creds/", change_creds),
    path("user_info/", current_user),
    path('courses/<int:pk>/', show_course),
    path('auth/', include('djoser.urls')),
]