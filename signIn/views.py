from django.shortcuts import render,redirect
import pyrebase
import requests
import json
from django.contrib import auth
config = {
    "apiKey": "AIzaSyD_zk03qUvvtOXDNjwlSPsYDuGLtKBUt4s",
    "authDomain": "django-812f9.firebaseapp.com",
    "projectId": "django-812f9",
    "storageBucket": "django-812f9.appspot.com",
    "messagingSenderId": "783956036102",
    "appId": "1:783956036102:web:216c6d65745356caf39187",
    "measurementId": "G-PJGEPXKW93",
    "databaseURL": "https://django-812f9-default-rtdb.firebaseio.com"
}

firebasse = pyrebase.initialize_app(config)

authe = firebasse.auth()

def signIn(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except requests.exceptions.HTTPError as e:
        response = e.args[0].response
        error = response.json()['error']
        message = error['message']
        return render(request, "signIn.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html", {"e": email})

# Create your views here.

def postsign(request):

    return render(request, "signIn.html")

def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')