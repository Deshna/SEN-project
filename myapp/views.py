from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User

def home(request):
    return render_to_response('index.html',context_instance=RequestContext(request))
def login_user(request):
    state = "Please log in below."
    username = password = ''
    print "--------------"
    print request.POST
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print username
        print password

        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    print state

    return render_to_response('login.html',{'state':state, 'username': username},context_instance=RequestContext(request))

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username,email,password)
        user.save()

    return render_to_response('index.html',context_instance = RequestContext(request))
