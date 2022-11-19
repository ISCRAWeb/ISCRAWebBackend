from rest_framework import serializers
from django.contrib.auth.models import User

class DealWithCourseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    user_deal = serializers.IntegerField

    def deal(self, user_deal):
        # join or leave course
        pass
