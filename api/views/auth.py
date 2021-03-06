# -*- coding: utf8 -*-
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from api.serializer.auth import JSONWebTokenSerializer, UserSerializer


class LoginView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

class ModifyPasswordAPI(APIView):
    permission_classes = (AllowAny,)

    @classmethod
    def post(cls, request):
        data = request.data
        user = User.objects.get(username=data.get('username'))
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg': 'success'}, status=200)
        return Response(data={'error_msg': serializer.errors}, status=400)

class RegisterAPI(APIView):

    permission_classes = (AllowAny, )

    @classmethod
    def post(cls, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg': 'success'}, status=200)
        return Response(data={'error_msg': serializer.errors}, status=400)




