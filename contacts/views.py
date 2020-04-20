from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        # Check if inquiry has been made
        if request.user.is_authenticated:
            if Contacts.objects.filter(user_id=user_id,listing_id=listing_id).exists():
                messages.error(request, "You have already made an inquiry on this listing")
                return redirect('/listings/' + listing_id)

        contact = Contacts(listing_id=listing_id, user_id=user_id, listing=listing, name=name, email=email,
                           phone=phone, message=message)
        contact.save()

        send_mail('INQUIRY ON '+listing, message + "\n For more information on this inquiry, please Login to the admin panel",
                  email, [realtor_email, 'adeliyiseyi@gmail.com'], fail_silently=False)

        messages.success(request,'Your inquiry has been submitted. You will receive feedback from the Realtor')

        return redirect('/listings/'+listing_id)

