from django.urls import path
from account.api import UserList, UserDetail


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:id>/', UserDetail.as_view()),
]