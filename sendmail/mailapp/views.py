from django.shortcuts import render
from django.core.mail import send_mail
import requests
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives



# mail = EmailMultiAlternatives(
#   subject="Your Subject",
#   body="This is a simple text email body.",
#   from_email="Yamil Asusta <pariskamal8@gmail.com>",
#   to=["pariskamal8@gmail.com"],
#   headers={"Reply-To": "support@sendgrid.com"}
# )
# mail.attach_alternative("<p>This is a simple HTML email body</p>", "text/html")

from django.core.mail import EmailMultiAlternatives



# Create your views here.
def sendmail(request):
	if request.method == 'GET':
		# mail.send()
		# send_mail('Subject here', 'Here is the message.', 'pariskamal8@example.com', ['pariskamal8@example.com'], fail_silently=False)
		# return HttpResponse("hello")
		return render(request,"sendmail.html",{})
	if request.method == 'POST':
		data = request.body
		
		send_simple_message()
		return HttpResponse("hi")

def send_simple_message():
		return requests.post(
				"https://api.mailgun.net/v3/sandboxe81398f95cc198be3.mailgun.org/messages",
				auth=("api", "key-fa2723c0e2940ad1102060a1a7a27062"),
				data={"from": "Mailgun Sandbox <postmaster@sandboxe81393df42d04cc198be3.mailgun.org>",
							"to": "AnandPatil <anandpatil108@gmail.com>",
							"subject": "Hello ParisKamal",
							"text": "Congratulations ParisKamal, you just sent an email with Mailgun."})
