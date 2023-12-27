from rest_framework import generics

from BackEnd.invitation.serializers import InvitationSerializer


class InvitationCreateView(generics.CreateAPIView):
    serializer_class = InvitationSerializer

