from rest_framework import serializers

from apps.sponsors.models import StudentSponsor


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = '__all__'