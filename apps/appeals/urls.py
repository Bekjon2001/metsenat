from django.urls import path

from apps.appeals.views import AppealList

urlpatterns = [
    path('appeals_list/', AppealList.as_view(), name='appeals_list'),
]