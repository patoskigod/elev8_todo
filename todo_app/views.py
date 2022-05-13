from django.shortcuts import render

# Create your views here.
def home(request):
    '''Renders the home page when the user is logged in'''
    return render(request,'users.html')

def index(request):
    '''return the page before login in'''
    return render(request,'index.html')

def sign(request):
    '''Going to the page to login in'''
    return render(request,'sign.html')

def edit(request):
    '''Going to the page edit in'''
    return render(request,'edit.html')

def log(request):
    '''Going to the page to login in'''
    return render(request,'log.html')

def users(request):
    '''Going to the user to login in'''
    return render(request,'users.html')

def profile(request):
    '''Going to the profile to login in'''
    return render(request,'profile.html')




