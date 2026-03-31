import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "residentevil_gunshop.settings")
django.setup()



from guns.tasks import send_welcome_email, log_stock_update, send_stock_report
from guns.models import Gun

email = "test@example.com"
result1 = send_welcome_email.delay(email)
print(f"Queued send_welcome_email task for {email}: {result1.id}")

gun_name = "AK-47"

gun, _ = Gun.objects.get_or_create(name=gun_name, defaults={"stock": 10})
new_stock = 15
result2 = log_stock_update.delay(gun_name, new_stock)
print(f"Queued log_stock_update task for {gun_name}: {result2.id}")

result3 = send_stock_report.delay()
print(f"Queued send_stock_report task: {result3.id}")

print("Waiting for task results (10s timeout)...")
print("send_welcome_email result:", result1.get(timeout=10))
print("log_stock_update result:", result2.get(timeout=10))
print("send_stock_report result:", result3.get(timeout=10))

print("All tasks queued and tested successfully!")