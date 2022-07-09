import json

from django.http import *

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

import my_settings
from member.models import Member
from member.serializers import MemberSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def member_api(request):
    if request.method == "POST":  # 200
        seri = MemberSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=200)
        return Response(seri.errors, status=400)

    if request.method == "GET":  # 200
        members = Member.objects.all()  # 쿼리셋
        serialized = MemberSerializer(members, many=True)
        # print(serialized.data) # 쿼리셋? OrderedDict
        return Response(serialized.data, status=200)  # Json으로 반환


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def member_with_email(request, email):
    reqdata = request.data

    if request.method == "GET":  # 200
        try:
            target = Member.objects.get(email=email)
            serialized = MemberSerializer(target)
            return Response(serialized.data, status=200)
        except:
            return Response(-1, status=200)

    elif request.method == "POST":
        pass

    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
