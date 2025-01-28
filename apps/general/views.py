from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView,CreateAPIView

from apps.general.models import University,PaymentMethod
from apps.general.serializers import UniversitySerializer,PPaymentMethodSerializer

class UniversityList(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filterset_fields = ['contract_amount']
    search_fields = ['name']
    filter_backends = (DjangoFilterBackend,SearchFilter)

class UniversityCreate(CreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def create(self,request,*args,**kwargs):
        response = super().create(request,*args,**kwargs)
        response.data ={
            "success": True,
            "message": "University muvaffaqiyatli yaratildi",
            "data": response.data
        }



class PaymentMethodList(ListAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PPaymentMethodSerializer
    search_fields = ['name']
    filter_backends = (SearchFilter,)

class PaymentMethodCreate(CreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PPaymentMethodSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            "success": True,
            "message": "Payment Method muvaffaqiyatli yaratildi",
            "data": response.data
        }
        return response


