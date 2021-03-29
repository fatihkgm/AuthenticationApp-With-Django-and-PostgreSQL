from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	return render (request , 'accounts/home.html' )

def login (request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			messages.success(request , 'You are now logged in.!')
			return redirect('dashboard')
		else:
			messages.error(request, 'Invalid login credentials')
			return redirect('login')

	return render (request , 'accounts/login.html' )

def register (request):
	if request.method == 'POST':
		username= request.POST['username']
		email= request.POST['email']
		password= request.POST['password']
		password_confirm= request.POST['password_confirm']

		if password == password_confirm:
		    if User.objects.filter(username=username).exists():
		    	messages.error(request,'User name is already exists!')
		    	return redirect('register')
		    else:
		    	if User.objects.filter(email=email).exists():
		    		messages.error(request,'Email is already exists')
		    		return redirect('register')
		    	else:
		    		user = User.objects.create_user(username = username,email=email , password=password)
		    		auth.login(request,user)
		    		messages.success(request, 'Welcome to your panel')
		    		return redirect('dashboard')
		    		user.save()
		    		messages.success(request, 'You are registered succesfully')
		    		return redirect('login')





		else: 
			messages.error(request, 'Password dont match')
			return redirect('register')
	else:
		return render (request , 'accounts/register.html' )

def dashboard (request):
	return render (request , 'accounts/dashboard.html' )

def logout (request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request,'You are successfully logout')
		return redirect('home')
	return redirect ('home')




