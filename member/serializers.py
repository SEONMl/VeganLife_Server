from rest_framework import serializers
from rest_framework.serializers import Serializer

from member.models import *


# 객체->JSON
class MemberSerializer(serializers.Serializer):
    class Meta:
        model=Member
        fields=['id','email', 'password','name','nickname','height','weight','vege_type']
    id=serializers.IntegerField()
    email = serializers.CharField(max_length=1000)
    password = serializers.CharField(max_length=1000)
    name = serializers.CharField(max_length=100)
    nickname = serializers.CharField(max_length=100)
    height = serializers.FloatField()
    weight = serializers.FloatField()
    vege_type = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Member(**validated_data)

    def update(self, instance, validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.vege_type = validated_data.get('vege_type', instance.vege_type)
        instance.save()
        return instance
