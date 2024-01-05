from django.urls import path

from .views import InvitationCreateAPIView, InvitationRetrieveAPIView, InvitationGetIdAPIView

urlpatterns = [
    path("create/", InvitationCreateAPIView.as_view(), name="create_invitation"),
    path("<str:token>/", InvitationGetIdAPIView.as_view(), name="")
]
