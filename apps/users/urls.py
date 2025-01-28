from django.urls import path
from apps.users.views import (
    CustomUserList,
    CustomUserCreate,
    CustomUserRetrieve,
    CustomUserUpdate,
)

urlpatterns = [
    path('', CustomUserList.as_view(), name='user-list'),
    path('create/', CustomUserCreate.as_view(), name='user-create'),
    path('<int:pk>/', CustomUserRetrieve.as_view(), name='user-retrieve'),
    path('<int:pk>/update/', CustomUserUpdate.as_view(), name='user-update'),
]
