from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sangmyung_univ_auth import auth

from api.serializers import UserSerializer


@api_view(['POST'])
def authenticate(request):
    return authenticate_user(request)


@api_view(['POST'])
def userinfo(request):
    return authenticate_user(request, response_body=False)


def authenticate_user(request, response_body=True):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        result = auth(username, password)
        status_code = status.HTTP_200_OK if result.is_auth else status.HTTP_401_UNAUTHORIZED
        return Response(result._asdict() if response_body else result.body, status=status_code)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
