# serializers.py

from django.contrib.auth.models import User, Group
from api.models import Assesment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AssesmentSerializer(serializers.HyperlinkedModelSerializer):
	model = Assesment 
	fields = ('url', 'title', 'description', 'due_date', 'assn_date')