from django.shortcuts import get_object_or_404

from events.models import EmailQuestion


def email_question(request, uuid):
    email_question = get_object_or_404(EmailQuestion, uuid=uuid)
