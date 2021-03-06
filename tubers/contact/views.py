from django.shortcuts import get_object_or_404, render,redirect
from .models import  Contact, Address
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']



        contact = Contact(full_name=full_name, 
            phone=phone, 
            email=email, 
            company_name=company_name, 
            subject=subject, 
            message=message,)
        contact.save()
        messages.success(request, 'Thanks for contacting us!')
        return redirect('home')


    address = get_object_or_404(Address)
    data = {
        'address': address
    }

    return render(request, 'contact/contact.html', data)