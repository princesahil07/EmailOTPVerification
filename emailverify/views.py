from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import random
from .models import EmailOTP
import smtplib
from email.message import EmailMessage

# Global Variables
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Create your views here.
def otp_send(username, gen_otp) :
	from_mail = 'test@gmail.com'
	server.login(from_mail, 'password')
	to_mail = username
	msg = EmailMessage()
	msg['Subject'] = "OTP verification"
	msg['From'] = from_mail
	msg['To'] = to_mail
	content = f'''
	This is system generated mail, do not reply
	on this mail

	{username} your OTP is {gen_otp}

	*do not share this OTP with anyone, this will response
	for loss your data or may hack your account
	'''
	msg.set_content(content)
	server.send_message(msg)
	print("email send", content)

def login_view(request) :
	message = ''
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		
		users = auth.authenticate(username=username, password=password)
		if users is not None :
			gen_otp = random.randint(000000, 999999)
			otpobj = EmailOTP.objects.create(
				username = username,
				otp = gen_otp
			)
			otpobj.save()

			otp_send(username, gen_otp)

			request.session['username'] = username
			get_users =  request.session['username']

			auth.login(request, users)
			return redirect('emailverify')
		else :
			message = "Username & Password dosn't match"
			return render(request, 'login.html', {'message' : message})
	return render(request, 'login.html', {})

def register_view(request) :
	if request.method == 'POST' :
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['email']
		email = request.POST['email']
		password = request.POST['password']
		users = User.objects.create_user(
			first_name = first_name,
			last_name = last_name,
			username = username,
			email = email,
			password = password
		)
		users.save()
		return redirect('/', {'message' : 'Successfully Registered'})
	return render(request, 'register.html', {})

def email_verify(request) :
	if request.method == 'POST' :
		otpobj = request.POST['get_otp']
		verify_otp = EmailOTP.objects.filter(otp = otpobj).exists()
		if verify_otp :
			return redirect('dashboard')
		else :
			return render(request, 'verify.html', {'message' : "OTP dosn't match"})
	return render(request, 'verify.html', {})

def dashboard(request) :
	username = request.session['username']
	return render(request, 'dashboard.html', {'username' : username})
