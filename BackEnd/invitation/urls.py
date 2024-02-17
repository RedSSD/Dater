from django.urls import path

from .views import InvitationCreateAPIView, InvitationRetrieveAPIView

urlpatterns = [
    path("create/", InvitationCreateAPIView.as_view(), name="create_invitation"),
    path("<str:token>/", InvitationRetrieveAPIView.as_view(), name=""),
    path("<str:token>/disagreement", InvitationRetrieveAPIView.disagreement, name="")
]
