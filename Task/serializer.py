from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ['id', 'Title', 'Description',
                  'DueDate', 'Tags', 'Status','timeStamp', ]

    def validate_Tags(self,value):
        data = set()
        for x in value.split(','):
            data.add(x)        
        return ','.join(data)

    def validate(self, attrs):
        date = attrs.get('DueDate')
        if date:
            if date < datetime.date.today():
                raise serializers.ValidationError({'DueDate':"Due Date Shoulde be Greater Than Today's Date "})
        return attrs

    def update(self, instance, validated_data):
        instance.Title = validated_data.get('Title', instance.Title)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.DueDate = validated_data.get('DueDate', instance.DueDate)
        instance.Tags = validated_data.get('Tags', instance.Tags)
        instance.Status = validated_data.get('Status', instance.Status)
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = dict()
        rep['id'] = instance.id
        rep['Title'] = instance.Title
        rep['DueDate'] = instance.DueDate or "No Due Date"
        rep['Tags'] = instance.Tags

        if instance.Status == 'O':
            rep['Status'] = 'Open'
        elif instance.Status == 'W':
            rep['Status'] = 'Working'
        elif instance.Status == 'D':
            rep['Status'] = 'Done'
        else:
            rep['Status'] = 'Overdue'
        return rep
