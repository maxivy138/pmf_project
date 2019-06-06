from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail

def contact(request):
#     import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, lastname=lastname, address=address, email=email, phone=phone, message=message)
        # import ipdb; ipdb.set_trace()
        contact.save()

        # Send email
        send_mail(
            'PMF | Contact Form',
            'There has been an inquiry for a private mortgage. Check out your admin panel.',
            'contact@privatemortgagefinder.com',
            ['contact@privatemortgagefinder.com'],
            fail_silently=False
        )

        # Send email
        send_mail(
            'PrivateMortgageFinder.com | Your request has been received',
            'Thank you for your inquiry.',
            'contact@privatemortgagefinder.com',
            [ email ],
            fail_silently=False
        )

        return render(request, 'pages/sendsuccessed2.html')

        # Check if user has made inquiry already
        # messages.success(request, 'Your request has been submitted.')
        
    return render(request, 'pages/contactus.html', {
        'showapplybutton': True
    })

