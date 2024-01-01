from django.urls import path

from .views import InvitationCreateAPIView, InvitationRetrieveAPIView

urlpatterns = [
    path("create/", InvitationCreateAPIView.as_view(), name="create_invitation")
]