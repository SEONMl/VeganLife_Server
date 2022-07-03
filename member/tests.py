from django.test import TestCase

# Create your tests here.
from member.models import Member,TestDB
from member.serializers import MemberSerializer, TestDBSerializer


class MemberTest(TestCase):
    def setUp(self):
        Member.objects.create(email="test@tt",password="123qwe")

    def get_member_database(self):
        member=Member.objects.all()
        print(member.all())
        member=MemberSerializer(data=member)
        #self.assertEqual("test@tt",member.get(email="test@tt"))

class TestDatabase(TestCase):
    def test_save(self):
        #self.assertEqual("123","121231233","실패")
        tmp=TestDBSerializer(data={"content":"123","id":1})
        if tmp.is_valid():
            print('성공')
            tmp.save()
        #test=TestDB.objects.get(pk=1)
        #self.assertEqual(test.data,"123")
