from rest_framework.generics import ListAPIView, CreateAPIView

from apps.sponsors.models import StudentSponsor
from apps.sponsors.serializers import StudentSponsorSerializer


class StudentSponsorList(ListAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    filterset_fields = ['amount']
    search_fields = ['student_first_name', 'sponsor_first_name']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = StudentSponsorSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class StudentSponsorCreate(CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            "success": True,
            "message": "Homiylik muvaffaqiyatli yaratildi",
            "data": response.data
        }
        return response

