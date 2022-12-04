from django.urls import path, include
from rest_framework import routers
<<<<<<< HEAD
from .views import login, change_password,change_creds, current_user
=======
from .views import *
>>>>>>> de37dd7 (testing serializers and views)

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD
    path("login/", login),
    path("change_pass/", change_password),
    path("change_creds/", change_creds),
    path("user_info/", current_user),
    path('course/', include('course.urls'))
=======
    path('courses/course/', show_course)
>>>>>>> de37dd7 (testing serializers and views)
]