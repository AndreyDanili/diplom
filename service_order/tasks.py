
from time import sleep
from django.core.mail import send_mail
from django.conf import settings
from django_celery_email.celery import app

from service_order.models import User, ConfirmEmailToken


@app.task
def new_user_registered_email(user_id, **kwargs):

    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    send_mail(
        "Your Token",
        f"Password Reset Token for {token.user.email} {token.key}",
        f"{settings.EMAIL_HOST_USER}",
        [token.user.email],
        fail_silently=False,
    )


@app.task
def new_order_email(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    send_mail(
        "Обновление статуса заказа",
        "Заказ сформирован",
        f"{settings.EMAIL_HOST_USER}",
        [user.email],
        fail_silently=False,
    )




