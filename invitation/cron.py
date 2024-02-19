from .models import Invitation
import datetime


def delete_expired_invitations():
    now = datetime.date.today()
    expired_invitations = Invitation.objects.filter(
        expiration_date=now
    )
    expired_invitations.delete()
