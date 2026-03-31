from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from guns.models import Gun
import logging
from datetime import timedelta

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_welcome_email(self, email):
    subject = "Welcome to the Gunshop!"
    message = "Thank you for registering. Enjoy shopping!"
    from_email = "no-reply@gunshop.com"
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        logger.warning(f"Sent welcome email to user {email}")
    except Exception as e:
        logger.error(f"Failed to send email to {email}: {e}")
        raise self.retry(exc=e)

@shared_task(bind=True)
def log_stock_update(self, gun_name: str, quantity: int):
    try:
        gun = Gun.objects.get(name=gun_name)
        gun.stock = quantity
        gun.save()
        logger.warning(f"Stock update: {gun.name} now has {gun.stock} units in stock.")
    except Gun.DoesNotExist:
        logger.error(f"Gun with name '{gun_name}' does not exist.")


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_stock_report(self):
    try:
        guns = Gun.objects.all()
        if not guns.exists():
            report = "No guns in stock."
        else:
            report_lines = [f"{gun.name}: {gun.stock} units" for gun in guns]
            report = "\n".join(report_lines)

        send_mail(
            subject="Daily Stock Report",
            message=report,
            from_email="no-reply@gunshop.com",
            recipient_list=["admin@example.com"],
        )
        logger.warning(f"Sent daily stock report to admin@example.com at {timezone.now()}")
    except Exception as e:
        logger.error(f"Failed to send stock report: {e}")
        raise self.retry(exc=e)
