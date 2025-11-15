from django.urls import path
from .views import RegisterView, MeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PromoteToAdminView
from .views import UserListView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("promote/<int:user_id>/", PromoteToAdminView.as_view()),
    path("users/", UserListView.as_view()),
    path("me/", MeView.as_view(), name="me"),
]
