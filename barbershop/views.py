from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import *
from .models import *
from .forms import  CreateUserForm , BarbershopForm, BookForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import (Group, User)


def home(request):
    barbershops = Barbershop.objects.all()
    return render(request, 'barbershop/home.html', {'barbershops':barbershops})


def about(request):
    return render(request, 'barbershop/about.html', {'title': 'About'})


@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(
                    user=user,
                    )
                messages.success(request,'Account was created for ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'barbershop/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def createBarbershop(request):
    form = BarbershopForm()
    if request.method =='POST':
        #print('printing POST:',request.POST)
        form=BarbershopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barbershop-home')
    context = {'form':form}
    return render(request, 'barbershop/create_barber.html',context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def createBook(request):
    form = BookForm()
    if request.method =='POST':
        #print('printing POST:',request.POST)
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barbershop-home')
    context = {'form':form}
    return render(request, 'barbershop/book_form.html',context )


@unauthenticated_user
def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('barbershop-home')

        context = {}
        return render(request, 'barbershop/login.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def Bookings(request):

    Bookings = Book.objects.last()
    context = {'Bookings':Bookings }
    return render(request, 'barbershop/bookings.html',context )




def logoutUser(request):
    logout(request)
    return redirect('login')
