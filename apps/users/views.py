from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,UpdateAPIView
from rest_framework import status
from rest_framework.response import Response

from apps.users.models import CustomUser
from apps.users.serializers import CustomUserSerializer


class CustomUserList(ListAPIView):
    """
    API for listing users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_fields = ['user_type','phone_number']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class CustomUserCreate(CreateAPIView):
    """
        API for creating a new user.
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Avtomatik validatsiya
        self.perform_create(serializer)  # Ma'lumotni saqlash
        headers = self.get_success_headers(serializer.data)

        # Javobni O‘zbek tilida qaytarish
        return Response(
            {
                "success": True,
                "message": "Foydalanuvchi muvaffaqiyatli yaratildi",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class CustomUserRetrieve(RetrieveAPIView):
    """
    API for retrieving a single user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserUpdate(UpdateAPIView):
    """
    API for updating an existing user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer