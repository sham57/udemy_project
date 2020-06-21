from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail



def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contained=Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contained:
                messages.error(request,'you have already made this enquiry ')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        send_mail(
            'property Inquiry',
            'hello!! there has been inquiry for' + listing+'.signup for more information.',
            'munakar0813@gmail.com',
            [realtor_email, 'ranjitkarsheetala@gmail.com'],
            fail_silently=False,

        )
        messages.success(request, 'you have maked sucessful inquiry')
        return redirect('/listings/'+listing_id)
 

