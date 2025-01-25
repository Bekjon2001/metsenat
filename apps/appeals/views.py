from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.appeals.models import Appeal
from apps.appeals.serializers import AppealSerializer


class AppealList(APIView):
    def get(self, request):
        appeals = Appeal.objects.all()
        serializer = AppealSerializer(appeals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)