from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from .serializers import TelegramUserSerializer


@api_view(['POST'])
def user_registration(request):
    data = request.data
    user, created = TelegramUser.objects.get_or_create(
        user_id=data['user_id'],
        defaults={
            'username': data.get('username', '')
        }
    )
    if created:
        serializer = TelegramUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'User has been already created'}, status=status.HTTP_409_CONFLICT)