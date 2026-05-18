from api.views import MeView, UserListView,NoteListView, NoteUpdateDeleteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path


urlpatterns = [
  path("register/", UserListView.as_view(), name='register'),
  path("token/", TokenObtainPairView.as_view(), name="get_token"),
  path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
  
  path('diary_notes/', NoteListView.as_view(), name="note-list"),
  path("diary_note/<int:pk>/", NoteUpdateDeleteAPIView.as_view(), name="diary-details"),
  
  path("me/" , MeView.as_view()) 
]
