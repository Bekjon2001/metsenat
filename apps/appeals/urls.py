from django.urls import path

from apps.appeals.views import AppealList,AppealCreate

urlpatterns = [
    path('appeals_list/', AppealList.as_view(), name='appeals_list'),
    path('appeals_create/', AppealCreate.as_view(), name='appeals_create'),
]