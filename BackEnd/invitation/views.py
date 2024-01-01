from rest_framework import generics

from .models import Invitation
from .serializers import InvitationSerializer


class InvitationRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = InvitationSerializer

    def retrieve(self, request, *args, **kwargs):
        # TODO get token, analyze it and send request to bot
        pass


class InvitationGetIdAPIView(generics.RetrieveAPIView):
    serializer_class = InvitationSerializer

    def retrieve(self, request, *args, **kwargs):
        return Invitation.objects.get(token=kwargs['token'])


class InvitationCreateAPIView(generics.CreateAPIView):
    serializer_class = InvitationSerializer
