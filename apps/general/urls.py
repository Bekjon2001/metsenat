from django.urls import path

from apps.general.views import *

urlpatterns = [
    path('uniersit_list',UniversityList.as_view(),name='university-list'),
    path('payment_list/',PaymentMethodList.as_view(),name='payment-method-list'),
    path('create/',PaymentMethodCreate.as_view(),name='payment-method-create'),
]