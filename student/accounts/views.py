from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.
def accounts(request):
    return render(request, 'accounts.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =  password)

        if user is not None:
            auth.login(request, user)
            print('user is logged in')
            return redirect('/homepage')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']


        user = User.objects.create_user(username = userName, email=email, password = password, first_name = firstName, last_name = lastName)
        print('user created')
        return redirect('/')

    else:
        return render(request, 'signup.html')

def homepage(request):
    return render(request, 'homepage.html')

def contact(request):
    return render(request, 'contact.html')

def discussion(request):
    return render(request, 'discussion.html')

def buy(request):
    return render(request, 'buy.html')

def sell(request):
    return render(request, 'sell.html')

def donate(request):
    return render(request, 'donate.html')