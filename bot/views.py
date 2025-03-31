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
        return Response(serializer.data)
    else:
        return Response({'message': 'User has been already created'})


@api_view(['GET'])
def get_user_info(request, user_id):
    try:
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = TelegramUserSerializer(user)
        return Response(serializer.data)
    except TelegramUser.DoesNotExist:
        return Response({"message": "User does not"}, status=404)