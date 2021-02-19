from django.urls import path
from users.views import UserCreate, UserRetrieve


urlpatterns = [
    path('retrieve/', UserCreate.as_view()),
    path('retrieve/<pk>', UserRetrieve.as_view())
]