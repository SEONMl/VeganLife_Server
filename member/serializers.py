from rest_framework import serializers as sz

from member.models import *


# 객체->JSON
class MemberSerializer(sz.Serializer):
    class Meta:
        model = Member
    email = sz.EmailField()
    password = sz.CharField(max_length=1000)
    name = sz.CharField(max_length=100)
    nickname = sz.CharField(max_length=100)
    height = sz.FloatField()
    weight = sz.FloatField()
    vege_type = sz.CharField(max_length=100)

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.vege_type = validated_data.get('vege_type', instance.vege_type)
        instance.save()
        return instance