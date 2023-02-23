from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from common.models import Course, Unit, File
from common.serializers import CourseSerializer, UserSerializer, UnitSerializer, VideoSerializer
from django.contrib.auth.models import User

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances in dashboard
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request):
        queryset =  Course.objects.all() if request.user else Course.objects.filter(educator = request.user.id)
        # serializer = CourseSerializer(queryset, many=True, context={'request': request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(educator=self.request.user)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = File.objects.all()