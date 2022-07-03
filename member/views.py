from django.http import *

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import my_settings
from member.models import Member
from member.serializers import MemberSerializer


@csrf_exempt
@api_view(['GET','POST'])
def member_api(request):
    if request.method=="POST":
        #request.session['key']=my_settings.SECRET_KEY
        serializer = MemberSerializer(data=request.data) #create -> 객체 리턴
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return HttpResponse(serializer.errors, status=400)

    if request.method=="GET":
        members = Member.objects.get(pk=1) # 쿼리셋
        serialized = MemberSerializer(members)
        return JsonResponse(serialized.data)


@api_view(['POST'])
def sign_up(request):
    target=Member.objects.all()
    serialized_target=MemberSerializer(data=request.data)
    if serialized_target.is_valid():
        serialized_target.save()
        return JsonResponse(serialized_target.data, status=200)

    return HttpResponse(serialized_target.errors,status=400)


@api_view(['GET'])
def sign_in(request):
    member=Member.objects.all()
    serialized=MemberSerializer(member,many=True)
    print(serialized.data)
    return JsonResponse(serialized.data)


