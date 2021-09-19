from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from users.models import User
# from .models import Author
from users.serializers import UserModelSerializer
from .permissions import IsOwnerOrReadOnly

#только чтение записей
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#детальная информация
class UserModelDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly]
