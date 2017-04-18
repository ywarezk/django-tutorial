from rest_framework.views import APIView
from register.rest.register.register_serializer import RegisterSerializer
from rest_framework.response import Response


class Register(APIView):
    def post(self, request, format='json'):
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.create(register_serializer.validated_data)
            return Response(data={'success': True}, status=200)
        else:
            return Response(data={'success': False}, status=500)

