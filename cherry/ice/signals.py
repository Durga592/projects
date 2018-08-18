from django.contrib.auth.models import User
from ice.models import Studyhall
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	#instance.profile.save()
	print "Hitting the signals..."
	pass

@receiver(post_save, sender=Studyhall)
def get_details(sender, instance, **kwargs):
	print ">>>>>>>>>> signal get details"
	pass