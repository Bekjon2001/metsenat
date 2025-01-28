from rest_framework import serializers

from apps.general.models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class PPaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'