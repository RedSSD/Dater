from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Invitation
from .serializers import InvitationSerializer

from .telegram import send_telegram_message


class InvitationRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = InvitationSerializer

    def retrieve(self, request, *args, **kwargs):
        # TODO get token, analyze it and send request to bot
        pass


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

        return Response(status=status.HTTP_204_NO_CONTENT)
