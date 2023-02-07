from rest_framework import serializers
from common.models import Course
from django.contrib.auth.models import User

class CourseSerializer(serializers.HyperlinkedModelSerializer):

    # def create(self, validated_data):
    #     course = Course.objects.create(
    #         title=validated_data['title'],
    #         description=validated_data['description'],
    #         educator=validated_data['educator']
    #     )
    #     return course

    class Meta:
        model = Course
        fields = ['url', 'id', 'units', 'educator', 'title', 'description', 'created_at', 'updated_at']
        # optional_fields = ['educator', ]


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
