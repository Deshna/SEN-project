from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from myapp.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import Http404 
from PIL import Image
import base64, csv
from time import strftime

def home(request):
    categories = Category.objects.all()   
    print request.user.is_authenticated()
    state = "Please enter your email ID below"

    newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
    products = newarrivals.product_set.all()
    return render_to_response('index.html', {'state': state, 'categories' : categories, 'products':products},context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def createdress(request):
    bases = Base.objects.all()
    categories = Category.objects.all()   
    state = "Please enter your email ID below"

    newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
    products = newarrivals.product_set.all()
    return render_to_response('createdress.html',{'bases':bases, 'state':state, 'products':products, 'categories':categories},context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def customizedress(request):
    if request.method == "POST":
        print "POST"
        b = request.POST.get("base")
        print b
        base = Base.objects.get(image = b)
        print base.mask_sideborder.url
        patterns = Pattern.objects.all()
        borders = Border.objects.all()
        butta = Butta.objects.all()
        categories = Category.objects.all() 
        return render_to_response('customization.html',{'patterns':patterns,'borders':borders,'butta':butta,'base':base, 'categories':categories},context_instance=RequestContext(request))
    else:
        bases = Base.objects.all()
        categories = Category.objects.all()   
        print request.user.is_authenticated()
        state = "Please enter your email ID below"

        newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
        products = newarrivals.product_set.all()
        return render_to_response('createdress.html',{'bases':bases, 'state':state, 'products':products, 'categories':categories},context_instance=RequestContext(request))

def addcategory(request):
    current_user =  request.user
    print "CURRENT USER: ",current_user.username
    if current_user.username != "admin":
        raise Http404

    state = "Please add a Category"
    if request.method == "POST":
        name = request.POST.get("name")
        categoryID = request.POST.get("categoryID")
        description = request.POST.get("description")

        try:
            c = Category.objects.create(name = name, description = description, categoryID = categoryID)
            state = "Category successfully created"
        except:
            state = "Category NOT created. Check CategoryID entered."
    return render_to_response("addcategory.html",{'state':state},context_instance = RequestContext(request))

def addsubcategory(request):
    current_user =  request.user
    print "CURRENT USER: ",current_user.username
    if current_user.username != "admin":
        raise Http404
    state = "Please add a SubCategory"
    if request.method == "POST":
        name = request.POST.get("name")
        subcategoryID = request.POST.get("subcategoryID")
        categoryID = request.POST.get("categoryID")

        try:
            c = Category.objects.get(categoryID = categoryID)
            s = SubCategory.objects.create(name = name, category = c, SubCategoryID = subcategoryID)
            state = "SubCategory successfully created"
        except:
            state = "Category NOT created. Check CategoryID entered."
    return render_to_response("addsubcategory.html",{'state':state},context_instance = RequestContext(request))

def deletecategory(request):
    current_user =  request.user
    print "CURRENT USER: ",current_user.username
    if current_user.username != "admin":
        raise Http404
    state = "Please select a Product to delete"
    cat = Category.objects.all()
    if request.method == "POST":
        categoryID = request.POST.get("categoryID")
        try:
            p = Category.objects.get(categoryID = categoryID)
            p.delete()
            state = "Product successfully deleted"
        except:
            state = "System ran into an error. Check ID provided."
    return render_to_response('deletecategory.html',{'state':state,'category':cat},context_instance = RequestContext(request))

def deletesubcategory(request):
    current_user =  request.user
    if current_user.username != "admin":
        raise Http404
    state = "Please select a Product to delete"
    subcat = SubCategory.objects.all()
    if request.method == "POST":
        subcategoryID = request.POST.get("subcategoryID")
        try:
            p = SubCategory.objects.get(subcategoryID = subcategoryID)
            p.delete()
            state = "Subcategory successfully deleted"
        except:
            state = "System ran into an error. Check ID provided."
    return render_to_response('deletecategory.html',{'state':state,'subcategory':subcat},context_instance = RequestContext(request))

def addproduct(request):
    current_user =  request.user
    if current_user.username != "admin":
        raise Http404
    state = "Please add a product"
    if request.method == "POST":
        image = request.FILES.get("image")
        name = request.POST.get("name")
        print name
        productID = request.POST.get("primaryID")
        subcategory = request.POST.get("subcategory")
        price = request.POST.get("price")
        description = request.POST.get("description")
        unitsinorder = request.POST.get("unitsinorder")
        fabrics = request.POST.get("fabrics")
        color = request.POST.get("color")
        occasion = request.POST.get("occasion")
        work = request.POST.get("work")

        print productID
        print subcategory
        print price
        print description
        print unitsinorder
        print fabrics
        print color
        print occasion
        print work

        try:
            sub = SubCategory.objects.get(SubCategoryID = subcategory)
            #p = Product.objects.create(image = image, name = name, productID = productID, price = price, subcategory = sub, unitsInStock = 1, description = description, unitsInOrder = unitsinorder, views = 0)
        except: 
            state = "Please fill in Product details carefully. Not validated. Make sure ProductID is unique, subcategoryID is correct."
            return render_to_response('addproduct.html',{'state':state},context_instance = RequestContext(request))

        f = fabrics.split(",")
        c = color.split(",")
        o = occasion.split(",")
        w = work.split(",")

        try:
            p = Product.objects.get(productID = productID)
            state = "Product already exists. If not, check Product ID."
            return render_to_response('addproduct.html',{'state':state},context_instance = RequestContext(request))
        except:
            p = Product.objects.create(image = image, name = name, productID = productID, price = price, subcategory = sub, unitsInStock = 1, description = description, unitsInOrder = unitsinorder, views = 0)
            p.save()
            p = Product.objects.get(productID = productID)
        print p.name
        '''MAKE SURE THESE ARE NOT PREVIOUSLY ADDED FABRICS, COLORS, OCCASIONS, WORKS. COVER EDGE CASE.'''
        for token in f:
            print token
            try:
                fab =Fabric.objects.get(fabrics = token)
            except:
                fab =Fabric.objects.create(fabrics = token)
                fab.save()            
            fab.product.add(p)

        for token in c:
            try:
                col =Color.objects.get(colors = token)
            except:
                col =Color.objects.create(colors = token)
                col.save()            
            col.product.add(p)

        for token in o:
            try:
                occ =Occasion.objects.get(occasions = token)
            except:
                occ =Occasion.objects.create(occasions = token)
                occ.save()            
            occ.product.add(p)

        for token in w:
            try:
                work =Work.objects.get(works = token)
            except:
                work =Work.objects.create(works = token)
                work.save()            
            work.product.add(p)

        state = "successfully created"
    return render_to_response('addproduct.html',{'state':state},context_instance = RequestContext(request))

def deleteproduct(request):
    current_user =  request.user
    print "CURRENT USER: ",current_user.username
    if current_user.username != "admin":
        raise Http404
    state = "Please select a Product to delete"
    products = Product.objects.all()
    if request.method == "POST":
        productID = request.POST.get("productID")
        p = Product.objects.get(productID = productID)
        p.delete()
        state = "Product successfully deleted"
    return render_to_response('add.html',{'state':state,'products':products},context_instance = RequestContext(request))

def adminupload(request):
    current_user =  request.user
    print "CURRENT USER: ",current_user.username
    if current_user.username != "admin":
        raise Http404
    '''only ADMIN must have the permissions to upload.
    '''
    state = "please upload an image"
    if request.method == "POST":
        image = request.FILES.get("image")
        name = request.POST.get("name")
        primaryID = request.POST.get("primaryID")
        try:
            print primaryID
            p = Product.objects.get(productID = int(primaryID))
            print primaryID
            i = Images.objects.create(image = image, name = name, product = p)
            print "not creating?"
            state = "image uploaded and linked successfully"
        except:
            i = Images.objects.create(image = image, name = name)
            state = "image uploaded but not linked"
    return render_to_response('image.html',{'state':state},context_instance=RequestContext(request))

def showproducts(request):
    current_user =  request.user
    print "CURRENT USER: ",current_user.username
    if current_user.username != "admin":
        raise Http404
    products = Product.objects.all()
    return render_to_response('showproducts.html',{'products':products},context_instance = RequestContext(request))

def logout_user(request):
    logout(request)
    categories = Category.objects.all()
    state = "Please enter your email ID below"
    print request.user.is_authenticated()
    newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
    products = newarrivals.product_set.all()
    return render_to_response('index.html', {'state': state, 'categories' : categories, 'products':products},context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile(request):
    categories = Category.objects.all()
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

    return render_to_response('user-profile.html', {'state_': state_, 'state': state,'categories':categories}, context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_address(request):
    state = "Please enter your email ID below"
    state_ = "Please enter the billing address details carefully."
    categories = Category.objects.all()

    if request.method == "POST":    
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        userprofile.address_line1 = request.POST.get('address1')
        userprofile.address_line2 = request.POST.get('address2')
        userprofile.city = request.POST.get('city')
        userprofile.state= request.POST.get('state')
        userprofile.postcode = request.POST.get('postcode')
        userprofile.save()
        state_ = "Address details updated successfully. Thank you. "

    return render_to_response('user-address.html', {'state_':state_, 'state':state ,'categories':categories},context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_creditcard(request):
    state = "Please enter your email ID below"
    state_ = "Please enter the billing address details carefully."
    categories = Category.objects.all()

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
    return render_to_response('user-creditcard.html', {'state_':state_, 'state':state , 'categories':categories},context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_pastorders(request):
    
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    categories = Category.objects.all()
    
    pastorders = userprofile.pastorders_set.all()

    products = []
    for order in pastorders:
        products.append(Product.objects.get(productID = order.orderno))

    return render_to_response('user-pastorders.html', {'products':products,'categories':categories}, context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_sizechart(request):
    state = "Please enter your email ID below"
    state_ = "Please enter the size in inches"
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    categories = Category.objects.all()
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

    return render_to_response('user-sizechart.html', {'state':state, 'state_':state_, 'userprofile':userprofile,'categories':categories}, context_instance=RequestContext(request))

@login_required(login_url = '/user/login/')
def user_profile_wishlist(request):

    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    categories = Category.objects.all()
    wishlist = userprofile.wishlist_set.all()

    products = []
    for wish in wishlist:
        products.append(Product.objects.get(productID = wish.wish_products))

    return render_to_response('user-wishlist.html', {'products':products,'categories':categories}, context_instance=RequestContext(request))

 
def add_wish(request):
    productID = str(request.GET.get("product",""))
    categories = Category.objects.all()
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)

    stop = True
    if len(productID)>0:
        wishes = userprofile.wishlist_set.all()
        for w in wishes:
            if int(productID) == int(w.wish_products):
                stop = False
                break
        print stop
        if stop:
            wish = Wishlist.objects.create(wish_products = productID)
            userprofile.wishlist_set.add(wish)
            userprofile.save()

    wishlist = userprofile.wishlist_set.all()
    print wishlist

    products = []
    for wish in wishlist:
        products.append(Product.objects.get(productID = wish.wish_products))
    return render_to_response('user-wishlist.html', {'products':products,'categories':categories}, context_instance=RequestContext(request))

def price(request):
    price = request.POST.get("price")
    tokens = price.split(",")
    lower_limit = tokens[0]
    upper_limit = tokens[1]
    productlist = Product.objects.all()
    products = []
    for p in productlist:
        if int(p.price) >= int(lower_limit) and int(p.price)<= int(upper_limit):
            products.append(p)

    p = Paginator(products,9)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        products = p.page(page)
    except (InvalidPage, EmptyPage):
        products = p.page(paginator.num_pages)
    categories = Category.objects.all()
    return render_to_response('shop4.html', {'products' : products,'categories':categories}, context_instance=RequestContext(request))

def location(request):
    categories = Category.objects.all()   
    print request.user.is_authenticated()
    state = "Please enter your email ID below"

    newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
    products = newarrivals.product_set.all()
    return render_to_response('store-location.html',{'products':products,'categories':categories, 'state':state}, context_instance = RequestContext(request))

def filter_color(request):
    color = request.POST.get("colorpicker-shortlist")
    color_instances = Color.objects.get(colors = color)
    products = color_instances.product.all()

    p = Paginator(products,9)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        products = p.page(page)
    except (InvalidPage, EmptyPage):
        products = p.page(paginator.num_pages)
    categories = Category.objects.all()
    return render_to_response('shop3.html', {'products' : products,'categories':categories}, context_instance=RequestContext(request))


def filter_occasion(request):
    products = []
    productlist = []
    if request.method == "POST":
        if request.POST.get("Bridal"):
            b = Occasion.objects.get(occasions = "Bridal")
            try:
                for p in b.product.all():
                    products.append(p.name)
            except:
                pass
        if request.POST.get("Casual"):
            b = Occasion.objects.get(occasions = "Casual")
            try:
                for p in b.product.all():
                    products.append(p.name)
            except:
                pass
        if request.POST.get("Festive"):
            b = Occasion.objects.get(occasions = "Festive")
            try:
                for p in b.product.all():
                    products.append(p.name)
            except:
                pass
        if request.POST.get("Party"):
            b = Occasion.objects.get(occasions = "Party")
            try:
                for p in b.product.all():
                    products.append(p.name)
            except:
                pass
        if request.POST.get("Reception"):
            b = Occasion.objects.get(occasions = "Reception")
            try:
                for p in b.product.all():
                    products.append(p.name)
            except:
                pass
        if request.POST.get("wedding"):
            b = Occasion.objects.get(occasions = "Wedding")
            try:
                for p in b.product.all():
                    products.append(p.name)
            except:
                pass

        newproducts = []
        for p in products:
            if p not in newproducts:
                newproducts.append(p)

        for p in newproducts:
            print p
            productlist.append(Product.objects.get(name = p))
        
    products = productlist
    
    p = Paginator(productlist,9)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        products = p.page(page)
    except (InvalidPage, EmptyPage):
        products = p.page(paginator.num_pages)
    categories = Category.objects.all()
    return render_to_response('shop2.html', {'products' : products,'categories':categories}, context_instance=RequestContext(request))

def item(request):
    try: 
        item = str(request.GET.get("item",""))
        print item
        product = Product.objects.get(productID = (item))

        if product.views is None:
            product.views = 0
        product.views = product.views+1
        product.save()

        state = "Please enter your email ID below"
        state_ = "Please enter the size in inches"
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        if request.method == "POST":
            print "ENTERS"
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
            userprofile.save() # if rememberme == True
            state_ = "The measurements are updated successfully. Thank you."
        categories = Category.objects.all()
        print "ENTERS HERE"
        return render_to_response('product-details.html', {'product': product, 'userprofile':userprofile,'categories':categories}, context_instance=RequestContext(request))
    except:
        categories = Category.objects.all()   
        print request.user.is_authenticated()
        state = "Please enter your email ID below"
        newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
        products = newarrivals.product_set.all()
        return render_to_response('index.html', {'state': state, 'categories' : categories, 'products':products},context_instance=RequestContext(request))



def review(request):
    if request.method == "POST":
        productID = request.POST.get("productID")
        user = request.POST.get("user")
        description = request.POST.get("description")

        product = Product.objects.get(productID = int(productID))

        r = Review.objects.create(product = product, user = user, description = description)
        r.save()
        userprofile = UserProfile.objects.get(user = request.user)
        categories = Category.objects.all()
        return render_to_response('product-details.html', {'product': product, 'userprofile':userprofile,'categories':categories}, context_instance=RequestContext(request))
    else:
        raise Http404

def sizechart_update(request):
    if request.method == "POST":
        state_ = "Please enter the size in inches"
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
    
        productID = request.POST.get("productID")
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
        userprofile = UserProfile.objects.get(user = request.user)
        product = Product.objects.get(productID = productID)
        categories = Category.objects.all()
        return render_to_response('product-details.html', {'product': product, 'userprofile':userprofile, 'categories':categories}, context_instance=RequestContext(request))
    else:
        raise Http404

def shop(request): 
    sub = str(request.GET.get("sub",""))
    subcat = SubCategory.objects.get(name = sub)
        

    products = subcat.product_set.all()
    for p in products:
        print p.name
    '''for n in products:
        string = n.name.split('.')
        n.name_clean = string[0]
        n.save()'''
    print "-------------"

    p = Paginator(products,9)
    print "PAGINATED"
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

    categories = Category.objects.all()
    return render_to_response('shop.html', {'products' : products,'sub':sub, 'categories':categories}, context_instance=RequestContext(request))


@login_required(login_url = '/user/login/')
def item_cart(request):
    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    stop = True
    if request.method == "POST":
        addcart = request.POST.get('addcart')
        print addcart
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)

        for item in userprofile.cart_set.all():
            if item.cart_products == addcart:
                stop = False
                break
        if stop:
            print "ENTERING"
            cart_item = Cart.objects.create(cart_products = addcart)
            userprofile.cart_set.add(cart_item)

    cart_items = userprofile.cart_set.all()
    print cart_items
    products = []
    total = 0
    for item in cart_items:
        print "here is: ",item.cart_products
        product = Product.objects.get(productID = int(item.cart_products))
        total  = total + product.price
        products.append(product)
    categories = Category.objects.all()
    return render_to_response('cart.html',{'products':products,'categories':categories, 'total':total},context_instance = RequestContext(request))
    
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
    categories = Category.objects.all()
    return render_to_response('login.html',{'state':state, 'username': username,'categories':categories},context_instance=RequestContext(request))

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username,email,password)
        user.save()

        state = "Your account is active. Please login to verify."
    categories = Category.objects.all()
    return render_to_response('login.html',{'state':state,'categories':categories},context_instance = RequestContext(request))

def subscribe(request):
    state = "Please enter your email ID below"
    if request.method == "POST":
        subscriber = request.POST.get('subscriber')
        print subscriber
        state = "You have subscribed to the mailing list. Thank you!"
        mail = Mailinglist.objects.create(mail = subscriber)
        mail.save()
    categories = Category.objects.all()  

    newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
    products = newarrivals.product_set.all()
    return render_to_response('index.html', {'state' :state, 'categories' : categories, 'products':products},context_instance = RequestContext(request))

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
        categories = Category.objects.all()
        return render_to_response('shop.html', {'products' : products,'categories':categories}, context_instance = RequestContext(request))


    state = "Please enter your email ID below"
    categories = Category.objects.all() 
    newarrivals  = SubCategory.objects.get(SubCategoryID = 71)
    products = newarrivals.product_set.all()
    return render_to_response('index.html', {'state' :state, 'categories' : categories, 'products':products},context_instance = RequestContext(request))

def aboutus(request):
    return render_to_response('about-us.html',context_instance = RequestContext(request))

@login_required(login_url = '/user/login/')
def cart_delete(request):
    if request.method == "POST":
        productID = request.POST.get("delete")
        print productID
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        cart_item = userprofile.cart_set.all()
        for item in cart_item:
            if item.cart_products == productID:
                userprofile.cart_set.remove(item)

    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    cart_items = userprofile.cart_set.all()
    products = []
    total = 0
    for item in cart_items:
        print item.cart_products
        product = Product.objects.get(productID = int(item.cart_products))
        total = total + product.price
        products.append(product)
    categories = Category.objects.all()
    return render_to_response('cart.html',{'products':products,'categories':categories,'total':total},context_instance = RequestContext(request))
   
@login_required(login_url = '/user/login') 
def wish_delete(request):
    if request.method == 'POST':
        productID = request.POST.get("delete")
        print productID
        userprofile = UserProfile.objects.get_or_create(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
        cart_item = userprofile.wishlist_set.all()
        for item in cart_item:
            if int(item.wish_products) == int(productID):
                userprofile.wishlist_set.remove(item)

    userprofile = UserProfile.objects.get_or_create(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    cart_items = userprofile.wishlist_set.all()
    products = []
    for item in cart_items:
        print item
        product = Product.objects.get(productID = int(item.wish_products))
        products.append(product)
    categories = Category.objects.all()
    return render_to_response('user-wishlist.html',{'products':products,'categories':categories},context_instance = RequestContext(request))
   



def savedress(request):
    if request.method == "POST":
        img_string = request.POST.get('myvar', '')
        img_string = img_string.split(',')
        name_string = request.POST.get('name')
        name = name_string +".png"
        path = "created-dress/"+name
        f = open(path,"wb")
        f.write(base64.b64decode(img_string[1]))
        #f.write(decodestring(img_string))
        f.close()
        f = open('created-dress/orders_placed.csv','ab')
        writer = csv.writer(f)
        time = strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([request.user.username,name_string,time])

        return render_to_response('blank.html',context_instance = RequestContext(request))

    else:
        raise Http404