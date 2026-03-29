from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_welcome_email(user_id):
    # Placeholder for sending email asynchronously
    print(f"Send welcome email to user {user_id}")