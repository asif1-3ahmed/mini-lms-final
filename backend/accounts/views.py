from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


# ==========================
# REGISTER (NO AUTH, NO CSRF)
# ==========================
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": str(e), "details": repr(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


# ==========================
# AUTHENTICATED USER PROFILE
# ==========================
class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


# ==========================
# PROMOTE TO ADMIN (AUTH)
# ==========================
class PromoteToAdminView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.role != "admin":
            return Response({"error": "Not allowed"}, status=403)

        try:
            user = User.objects.get(id=user_id)
            user.role = "admin"
            user.save()
            return Response({"message": "User promoted to admin"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)


# ==========================
# USER LIST (AUTH)
# ==========================
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]  # ✅ No 401 for token API

@api_view(["GET"])
@permission_classes([AllowAny])
def current_user(request):
    if request.user.is_authenticated:
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "role": getattr(request.user, "role", "")
        })
    return Response({"error": "Not logged in"}, status=401)
