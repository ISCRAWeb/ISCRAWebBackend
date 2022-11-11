from django.urls import path, include
from rest_framework import routers
from .views import login, change_password,change_creds, current_user

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("login/", login),
    path("change_pass/", change_password),
    path("change_creds/", change_creds),
    path("user_info/", current_user),

]