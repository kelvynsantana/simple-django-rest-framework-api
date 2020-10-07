from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


from accounts.api.serializers import RegistrationSerializer

class RegisterView(APIView):
    def post(self, request):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Sucessfully registred a new user'
            data['id'] = account.id
            data['email'] = account.email
            data['username'] = account.username
            status_code = status.HTTP_201_CREATED

        else:
            data = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data, status_code)