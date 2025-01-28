from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.appeals.models import Appeal
from apps.appeals.serializers import AppealSerializer


class AppealList(ListAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class AppealCreate(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            "success": True,
            "message": "Appeal muvaffaqiyatli yaratildi",
            "data": response.data
        }
        return response