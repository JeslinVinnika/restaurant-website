from datetime import date, time
from os import name
from pyexpat.errors import messages
from django.contrib import messages
from .models import Booking
from django.shortcuts import render,redirect
from myapp.models import Contact, Booking
from django.http import HttpResponse
from.models import Newsletter
from .models import Comment

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    context={}

    if request.method == 'POST':
        name = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msz = request.POST.get('message')

        obj = Contact(name=name, email=em, subject=sub, message=msz)
        obj.save()
        context['message']=(f'Dear {name}, Thank you for your time!')
    return render(request,'contact.html',context)

def about(request):
    return render(request,'about.html')

def base(request):
    return render(request,'base.html')

def blog(request):
    return render(request,'blog.html')

def order(request):
    return render(request,'order.html')

def booking(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('time')
        guests = request.POST.get('guests')

        print("POST DATA:", name, email, mobile, booking_date, booking_time, guests)

        Booking.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            booking_date=booking_date,
            booking_time=booking_time,
            guests=guests
        )

        context['message'] = f'Dear {name}, Thank you for your time!'

    return render(request, 'booking.html', context)


def feature(request):
    return render(request,'feature.html')

def menu(request):
    return render(request,'menu.html')

def single(request):
    return render(request,'single.html')

def team(request):
    return render(request,'team.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def cookies(request):
    return render(request,'cookies.html')

def help_page(request):
    return render(request,'help.html')

def faq(request):
    return render(request,'faq.html')

from django.shortcuts import redirect
from django.contrib import messages
from .models import Newsletter

def news_letter(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            messages.error(request, "Email is required")
            return redirect("index")

        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, "You are already subscribed")
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, "Subscribed successfully 🎉")

        return redirect("index")

def upi_payment(request):
    return render(request,'upi_payment.html')
def payment_success(request):
    return render(request,'payment_success.html')

def single_blog(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        message = request.POST.get("message")

        Comment.objects.create(name=name, email=email, website=website, message=message)
        return redirect("single_blog")
    comments = Comment.objects.all().order_by('-created_at')
    return render(request,'single.html',{'comments':comments})
