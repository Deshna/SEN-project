from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from myapp.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()   
    print request.user.is_authenticated()
    state = "Please enter your email ID below"

    return render_to_response('index.html', {'state': state, 'categories' : categories},context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    categories = Category.objects.all()
    state = "Please enter your email ID below"
    print request.user.is_authenticated()
    return render_to_response('index.html', {'state': state, 'categories' : categories},context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile(request):
    state_ = "Please enter your credentials"
    state = "Please enter your email ID below"
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('Full Name')
        email = request.POST.get('email')
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')

        try:
            #Do for other details
            u = User.objects.get(username = username)
            print "User got"
            user = authenticate(username=username, password= oldpassword)
            print user
            if user is not None:
                print "is_authenticated"
                userprofile = UserProfile.objects.get_or_create(user = user)
                userprofile = UserProfile.objects.get(user = user)
                if len(newpassword)!=0:
                    u.set_password(newpassword)
                if len(email)!=0:
                    u.email = email
                if len(fullname)!=0:
                    userprofile.fullname = fullname
                    userprofile.save()
                u.save()

            state_ = "Account updated successfully."
        except: 
            state_ = "Please enter details correctly."

    return render_to_response('user-profile.html', {'state_': state_, 'state': state}, context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_address(request):
    state = "Please enter your email ID below"
    state_ = "Please enter the billing address details carefully."

    if request.method == "POST":    
        print "enter"
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        print "enter"
        userprofile.address_line1 = request.POST.get('address1')
        userprofile.address_line2 = request.POST.get('address2')
        userprofile.city = request.POST.get('city')
        userprofile.state= request.POST.get('state')
        userprofile.postcode = request.POST.get('postcode')
        userprofile.save()
        state_ = "Address details updated successfully. Thank you. "

    return render_to_response('user-address.html', {'state_':state_, 'state':state },context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_creditcard(request):
    state = "Please enter your email ID below"
    state_ = "Please enter the billing address details carefully."

    if request.method == "POST":    
        print "enter"
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)

        userprofile.cardno = request.POST.get('cardno')
        userprofile.cardname = request.POST.get('cardname')
        userprofile.cvv = request.POST.get('cvv')
        userprofile.exp_month = request.POST.get('exp_month')
        userprofile.exp_year = request.POST.get('exp_year')
        userprofile.save()

        state_ = "Details updated successfully."
    return render_to_response('user-creditcard.html', {'state_':state_, 'state':state },context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_pastorders(request):
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)

    pastorders = userprofile.pastorders_no
    print pastorders
    plist = []
    strord = ''
    products = []
    for wish in pastorders:
        print wish
        if wish!='[' and wish!=']' and wish!=' 'and wish!=',':
            strord= strord+str(wish)
        if wish == ',' or wish == ']':
            plist.append(strord)
            strord = ''
    print plist
    for wish in plist:
        p = Product.objects.get(productID = wish)
        products.append(p)
    return render_to_response('user-pastorders.html', {'products':products}, context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_sizechart(request):
    state = "Please enter your email ID below"
    state_ = "Please enter the size in inches"
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    if request.method == "POST":
        bust = request.POST.get('bust')
        neck_back = request.POST.get('neck_back')
        neck_front = request.POST.get('neck_front')
        sleeve_width = request.POST.get('sleeve_width')
        sleeve_length = request.POST.get('sleeve_length')
        shoulder = request.POST.get('shoulder')
        length_blouse = request.POST.get('length_blouse')
        waist_blouse = request.POST.get('waist_blouse')

        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        userprofile.bust = bust
        userprofile.neck_front = neck_front
        userprofile.neck_back = neck_back
        userprofile.sleeve_length = sleeve_length
        userprofile.sleeve_width = sleeve_width
        userprofile.shoulder = shoulder
        userprofile.length_blouse = length_blouse
        userprofile.waist_blouse = waist_blouse
        userprofile.save()
        state_ = "The measurements are updated successfully. Thank you."

    return render_to_response('user-sizechart.html', {'state':state, 'state_':state_, 'userprofile':userprofile}, context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_wishlist(request):
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)

    wishlist = userprofile.wishlist
    wlist = []
    strwish = ''
    products = []
    for wish in wishlist:
        print wish + "fhiwei"
        if wish!='[' and wish!=']' and wish!=' 'and wish!=',':
            print wish + " fiji"
            strwish = strwish+str(wish)
        if wish == ',' or wish == ']':
            wlist.append(strwish)
            strwish = ''

    print wlist
    for wish in wlist:
        print wish
        p = Product.objects.get(productID = wish)
        products.append(p)
    return render_to_response('user-wishlist.html', {'products':products}, context_instance=RequestContext(request))



def shop(request):
    subcat = SubCategory.objects.get(name = "Bestseller")
    if request.method == "POST":
        sub = str(request.POST.get("subcat"))
        print sub,"sgifdigjid"
        if len(sub) == 0:
            categories = Category.objects.all()   
            state = "Please enter your email ID below"
            return render_to_response('index.html', {'state': state, 'categories' : categories}, context_instance = RequestContext(request))
        string = sub.split("/")
        sub = string[0]
        subcat = SubCategory.objects.get(name = sub)
        

    products = subcat.product_set.all()
    for n in products:
        string = n.name.split('.')
        n.name_clean = string[0]
        n.save()

    p = Paginator(products,9)

    '''try: 
        item = str(request.GET.get("item",""))
        print "detects"
        return render_to_response('product-details.html', {'name': item}, context_instance=RequestContext(request))
    except:
        pass'''

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        products = p.page(page)
    except (InvalidPage, EmptyPage):
        products = p.page(paginator.num_pages)


    return render_to_response('shop.html', {'products' : products, 'sub':sub}, context_instance=RequestContext(request))

def product_details(request):
    #Add view to Page views
    return render_to_response('product-details.html',context_instance = RequestContext(request))

def cart(request):
    cartoon = []
    if request.method == "POST":
        addcart = request.POST.get('addcart')
        print addcart
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        print userprofile.cart
        if not userprofile.cart:
            print "Enter"
            userprofile.cart = [str(addcart)]
            userprofile.save()
        else:
            cartoon = userprofile.cart
            print cartoon
            if addcart not in cartoon:
                cartoon.append(str(addcart))
            userprofile.cart = cartoon
            userprofile.save()

    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)

    pastorders = userprofile.cart
    print pastorders
    plist = []
    strord = ''
    products = []
    for wish in pastorders:
        print wish
        if wish!='[' and wish!=']' and wish!=' 'and wish!=',':
            strord= strord+str(wish)
        if wish == ',' or wish == ']':
            plist.append(strord)
            strord = ''
    print plist
    for wish in plist:
        p = Product.objects.get(productID = wish)
        products.append(p)
    return render_to_response('user-pastorders.html', {'products':products}, context_instance=RequestContext(request))
    return render_to_response('cart.html',context_instance = RequestContext(request))
    
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

        state = "Your account is active. Please login to verify."
    return render_to_response('login.html',{'state':state},context_instance = RequestContext(request))

def subscribe(request):
    state = "Please enter your email ID below"
    if request.method == "POST":
        subscriber = request.POST.get('subscriber')
        print subscriber
        state = "You have subscribed to the mailing list. Thank you!"
        mail = Mailinglist.objects.create(mail = subscriber)
        mail.save()
    categories = Category.objects.all()  

    return render_to_response('index.html', {'state' :state, 'categories' : categories},context_instance = RequestContext(request))

def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        products = Product.objects.filter(Q(name__icontains = search)|Q(description__icontains = search))
        for p in products:
            print p.name
        p = Paginator(products,10)

        try: page = int(request.GET.get("page", '1'))
        except ValueError: page = 1

        try:
            products = p.page(page)
        except (InvalidPage, EmptyPage):
            products = p.page(paginator.num_pages)
        return render_to_response('shop.html', {'products' : products}, context_instance = RequestContext(request))


    state = "Please enter your email ID below"
    categories = Category.objects.all() 
    return render_to_response('index.html', {'state' :state, 'categories' : categories},context_instance = RequestContext(request))

def filter_price(request):
    if request.method == "POST":
        price_range = request.POST.get('filter_price')
        print price_range

    categories = Category.objects.all()  
    state = "Please enter your email ID below"
    return render_to_response('index.html', {'state' :state, 'categories' : categories},context_instance = RequestContext(request))

