from django.shortcuts import render, redirect
from .models import Info
from django.core.mail import send_mail

def info(request):
#     import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        financetype = request.POST['financetype']
        credittype = request.POST['credittype']
        propvalue = request.POST['propvalue']
        firstmortgagebalance = request.POST['firstmortgagebalance']
        firstmortgagerate = request.POST['firstmortgagerate']
        secondmortgagebalance = request.POST['secondmortgagebalance']
        secondmortgagerate = request.POST['secondmortgagerate']
        borrowamount = request.POST['borrowamount']
        incometype = request.POST['incometype']
        incomerange = request.POST['incomerange']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        city = request.POST['city']
        postalcode = request.POST['postalcode']
        email = request.POST['email']
        phonenumber = request.POST['phone']

        info = Info(financetype=financetype, credittype=credittype, propvalue=propvalue, firstmortgagebalance=firstmortgagebalance, firstmortgagerate=firstmortgagerate, secondmortgagebalance=secondmortgagebalance, secondmortgagerate=secondmortgagerate, borrowamount=borrowamount, incometype=incometype, incomerange=incomerange, name=firstname, lastname=lastname, address=address, city=city, postalcode=postalcode, email=email, phonenumber=phonenumber)
        # import ipdb; ipdb.set_trace()
        info.save()

        # Send email
        send_mail(
            'PMF | Application Form',
            'There has been an inquiry for a private mortgage. Check out your admin panel.',
            'contact@privatemortgagefinder.com',
            ['contact@privatemortgagefinder.com'],
            fail_silently=False
        )

        # Send email
        send_mail(
            'PMF | Application Submission',
            'Thank you for filling out the application. A mortgage broker will be in touch with you shortly.',
            'contact@privatemortgagefinder.com',
            [ email ],
            fail_silently=False
        )

        return render(request, 'pages/sendsuccessed.html')


        # messages.success(request, 'Your request has been submitted.')
        
    return render(request, 'pages/basicinfo.html')