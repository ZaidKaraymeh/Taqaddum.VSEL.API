from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from common.models import Course
from common.serializers import CourseSerializer, UserSerializer
from django.contrib.auth.models import User

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # def get_permissions(self):
        # """
        # Instantiates and returns the list of permissions that this view requires.
        # """
        # if self.action == 'list':
        #     permission_classes = [IsAuthenticated]
        # else:
        #     permission_classes = [IsAdminUser]
        # return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Course.objects.filter(educator = request.user.id)
        serializer = CourseSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
