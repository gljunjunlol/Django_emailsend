from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
	'''
		send_mail('Hey, nice to see you again',
		'Hi, this mail is coming from a tutorial',
		# input your email here
		'sender@gmail.com',
		# go to temp-mail.org for a temp email
		['pajoga8578@nhmty.com'],
		fail_silently=False)'''

	return render(request, 'home.html')