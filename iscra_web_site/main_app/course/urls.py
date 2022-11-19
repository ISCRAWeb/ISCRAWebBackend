from django.urls import path, include
from rest_framework import routers
from .views import course, course_deal, course_for_auth

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("course_page/", course),
    path("course_page/", course_for_auth),
    path("course_page/deal", course_deal),
]