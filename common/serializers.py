from rest_framework import serializers
from common.models import Course, Unit, File
from django.contrib.auth.models import User

class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ['url', 'id', 'units', 'educator', 'title', 'description', 'created_at', 'updated_at']
        depth = 1
        # optional_fields = ['educator', ]
    
    # write a save function that putss user from request
    


class UnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'

class VideoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = File
        fields = ['url', 'id', 'file', 'title', 'description']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
        read_only_fields = ('is_active', 'is_staff', 'last_login', 'is_superuser', 'date_joined')
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
