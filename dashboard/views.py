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
    page_size = 10

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
        # serializer = CourseSerializer(queryset, many=True, context={'request': request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    # def create(self, request):
    #     serializer = CourseSerializer(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.error_messages)



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
