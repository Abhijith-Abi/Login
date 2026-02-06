from django.urls import path
from .views import (
    NoteListCreateAPIView,
    NoteRetrieveUpdateDestroyAPIView,
    RegisterView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Notes CRUD
    path("notes/", NoteListCreateAPIView.as_view(), name="note-list-create"),
    path(
        "notes/<int:pk>/",
        NoteRetrieveUpdateDestroyAPIView.as_view(),
        name="note-detail",
    ),

    # Auth
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="auth-login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
]
