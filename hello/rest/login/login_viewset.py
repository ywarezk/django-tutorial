from rest_framework.views import APIView
from hello.rest.login.login_serializer import LoginSerializer
from rest_framework.response import Response

class Login(APIView):
    def post(self, request, format='json'):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.data)
            return Response(data={'success': True}, status=200)
        return Response(data=serializer.errors, status=401)