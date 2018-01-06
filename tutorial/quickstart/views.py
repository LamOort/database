from django.contrib.auth.models import User, Group
from .models import Song, Employee
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, SongSerializer, EmployeeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
	
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer