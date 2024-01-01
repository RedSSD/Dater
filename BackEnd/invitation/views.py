from rest_framework import generics

from .models import Invitation
from .serializers import InvitationSerializer


class InvitationRetrieveAPIView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        # TODO get token, analyze it and send request to bot
        pass


class InvitationCreateAPIView(generics.CreateAPIView):
    serializer_class = InvitationSerializer


