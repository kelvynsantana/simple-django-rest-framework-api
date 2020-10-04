from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


from accounts.api.serializers import RegistrationSerializer


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Sucessfully registred a new user'
            data['email'] = account.email
            data['username'] = account.username
            status_code = status.HTTP_201_CREATED

        else:
            data = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data, status_code)
