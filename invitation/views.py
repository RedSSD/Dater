from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Invitation
from .serializers import InvitationSerializer

from .telegram import send_telegram_message


class InvitationRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = InvitationSerializer

    def retrieve(self, request, *args, **kwargs):
        telegram_token = kwargs.get('token')
        invitation = Invitation.objects.get(token=telegram_token)

        send_telegram_message(invitation.telegram_id, 'agreement')

        return Response({}, status=status.HTTP_200_OK)

    @staticmethod
    @api_view(('GET',))
    def disagreement(request, **kwargs):
        telegram_token = kwargs.get('token')
        invitation = Invitation.objects.get(token=telegram_token)

        send_telegram_message(invitation.telegram_id, 'disagreement')

        return Response({}, status=status.HTTP_200_OK)


class InvitationCreateAPIView(generics.CreateAPIView):

    serializer_class = InvitationSerializer

    def post(self, request, *args, **kwargs):
        serializer = InvitationSerializer(
            data={"telegram_id": request.data['telegram_id']}
        )
        if serializer.is_valid():
            chat_id = str(request.data['telegram_id'])

            if send_telegram_message(chat_id, 'creation'):
                serializer.save()
                return Response(serializer.data)

        return Response(status=status.HTTP_409_CONFLICT)
