from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sangmyung_univ_auth import auth, completed_courses

from api.serializers import UserSerializer


@api_view(['POST'])
def authenticate(request):
    return authenticate_user(request)


@api_view(['POST'])
def userinfo(request):
    return authenticate_user(request, response_body=False)


@api_view(['POST'])
def courses(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username, password = serializer.validated_data['username'], serializer.validated_data['password']
        result = completed_courses(username, password)
        status_code = status.HTTP_200_OK if result.is_auth else status.HTTP_401_UNAUTHORIZED
        return Response(filter_data(result.body), status=status_code)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def authenticate_user(request, response_body=True):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username, password = serializer.validated_data['username'], serializer.validated_data['password']
        result = auth(username, password)
        status_code = status.HTTP_200_OK if result.is_auth else status.HTTP_401_UNAUTHORIZED
        return Response(result._asdict() if response_body else result.body, status=status_code)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def filter_data(original_data):
    return list(map(lambda item: {
        'number': item['SBJ_NO'],
        'name': item['SBJ_NM'],
        'credit': item['CDT'],
        'type': item['CMP_DIV_NM'],
        'grade': item['GRD_NM'],
        'year': item['SCH_YEAR'],
        'semester': item['SMT_NM'],
        'domain': item['CULT_ARA_NM'] if item['CULT_ARA_NM'] != '*' else None
    }, original_data))
