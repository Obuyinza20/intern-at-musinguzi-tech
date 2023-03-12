from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def signUp(request):
    page = 'signup'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'error occurred during registration, check fields again.')

    return render(request, 'register_login.html' , {'page':page, 'form':form})




def loginPage(request):
    page= 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User Does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Bad Credentials!, try again.')
        
            
    context = {
        'page':page

    }
    return render (request, 'register_login.html' , context)

def logoutPage(request):
    logout(request)
    return redirect('home')




def home(request):
    interneez = Internee.objects.all()
    number = interneez.count()
    photos = Photo.objects.all()
    context = {'photos':photos , 'number': number}
    return render(request, 'home.html' , context)


def application(request):
    interneez = Internee.objects.all()
    number = interneez.count()
    if request.method == 'POST':
        internee = Internee.objects.create(
            first_name = request.POST['first_name'],
            second_name = request.POST['second_name'],
            institution = request.POST['institution'],
            course = request.POST['course'],
            gender = request.POST['gender'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            period = request.POST['period'],
            willingness = request.POST['willingness'],
            area_of_interest = request.POST['area_of_interest']
        )
        internee.save()
        return redirect(reverse('home'))
    
    context ={
        'number':number
    }

    return render(request, 'application.html' , context)


def interneeView(request):
    interneez = Internee.objects.all()
    number = interneez.count()
    page = 'internees'
    internees = Internee.objects.all()
    context ={'internees':internees,
              'page': page,
              'number': number
              }
    return render(request, 'view_internees.html' , context)


def singleInternee(request, pk):
    interneez = Internee.objects.all()
    number = interneez.count()
    page = 'singleinternee'
    internee = Internee.objects.get(id = pk)
    context ={
        'page': page,
        'internee': internee,
        'number': number
    }
    return render(request, 'view_internees.html', context)


# Sending acceptance letter 

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def accept(request, pk):
    accepted_internee = Internee.objects.get(id = pk)
    template = render_to_string('email_template.html', {'accepted_internee': accepted_internee})
    email = EmailMessage(
        'Thanks for placing your application',
        template,
        settings.EMAIL_HOST_USER,
        [accepted_internee.email],
    )
    email.fail_silently=False
    email.send()
    interneez = Internee.objects.all()
    number = interneez.count()
    page = 'accept'
   
    context ={
        'page': page,
        'accepted_internee': accepted_internee,
        'number': number
    }
    return render(request, 'view_internees.html' , context)
