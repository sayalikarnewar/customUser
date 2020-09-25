from rest_framework import serializers
from app.models import User
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # app = serializers.PrimaryKeyRelatedField(many=True, queryset = User.objects.all())

    class Meta:
        model = User
        fields = '__all__'