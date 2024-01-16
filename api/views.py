from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sangmyung_univ_auth import auth


@api_view(['POST'])
def authenticate(request):
    if 'username' and 'password' in request.data:
        username, password = request.data['username'], request.data['password']
        result = auth(username, password)
        res = status.HTTP_200_OK if result.is_auth else status.HTTP_401_UNAUTHORIZED
        return Response(result._asdict(), status=res)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userinfo(request):
    if 'username' and 'password' in request.data:
        username, password = request.data['username'], request.data['password']
        result = auth(username, password)
        res = status.HTTP_200_OK if result.is_auth else status.HTTP_401_UNAUTHORIZED
        return Response(result.body, status=res)
    return Response(status=status.HTTP_400_BAD_REQUEST)
