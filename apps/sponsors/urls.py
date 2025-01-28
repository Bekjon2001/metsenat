from django.urls import path
from apps.sponsors.views import StudentSponsorList, StudentSponsorCreate

urlpatterns = [
    path('list/', StudentSponsorList.as_view(), name='student-sponsor-list'),
    path('create/', StudentSponsorCreate.as_view(), name='student-sponsor-create'),
]
