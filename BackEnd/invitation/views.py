from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

import requests

from .config import TELEGRAM_TOKEN
from .models import Invitation
from .serializers import InvitationSerializer


TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'
TELEGRAM_MESSAGE_CREATE_TEXT = "Your invitation link has been created successfully"
TELEGRAM_MESSAGE_AGREEMENT_TEXT = "Someone agreed to go out with you"


def send_telegram_message(chat_id, text):
    response = requests.post(
        TELEGRAM_API_URL + "sendMessage",
        {'chat_id': chat_id, 'text': text}
    )
    return response.json()['ok']


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

    def post(self, request, *args, **kwargs):
        serializer = InvitationSerializer(
            data={"telegram_id": request.data['telegram_id']}
        )
        if serializer.is_valid():
            chat_id = str(request.data['telegram_id'])

            if send_telegram_message(chat_id, TELEGRAM_MESSAGE_CREATE_TEXT):
                serializer.save()
                return Response(serializer.data)

        return Response(status=status.HTTP_204_NO_CONTENT)
