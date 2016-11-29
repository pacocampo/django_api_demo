from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alumni
from .tasks import send_email



@receiver(post_save, sender=Alumni)
def send_email_per_alumni(sender,instance,**kwargs):

	send_email.delay(instance.mail,instance.name)


	print("Mande el correo")
