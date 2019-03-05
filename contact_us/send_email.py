from django.core.mail import send_mail
from share_settings.base import EMAIL_HOST_USER

from django.contrib import messages

def send_contact_request(request, name, email, number, text):

    subject = 'Contact Request'

    message = """
    
        Hello, You have a new contact request from """ + name + """
        
        \n Name: """ + name + """
        \n Email: """ + email + """
        \n Number: """ + number + """
        \n Message: """ + text + """
        """

    send_mail(subject, message, EMAIL_HOST_USER, [str(email)])


def authError(request):

    messages.warning(request, 'Sorry, Your email can not be sent at this time!')


