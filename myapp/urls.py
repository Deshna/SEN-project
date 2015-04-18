from django.conf.urls import patterns, url

from myapp import views


urlpatterns = patterns('',
    url(r'home', views.home,
        name='home',),

    url(r'about', views.aboutus,
        name='aboutus',),

    url(r'savedress', views.savedress,
        name='savedress',),

    url(r'item_cart', views.item_cart,
        name='item_cart',),

    url(r'cart_delete', views.cart_delete,
        name='cart_delete',),

    url(r'login', views.login_user,
        name='login_user',),
    url(r'register', views.register_user,
        name='register_user',),
    url(r'shop', views.shop,
        name='shop',),
    url(r'item', views.item,
        name='item',),
    url(r'subscribe', views.subscribe,
        name='subscribe',),

    url(r'search', views.search,
        name='search',),

    url(r'wish_delete', views.wish_delete,
        name='wish_delete',),
    url(r'logout', views.logout_user,
        name='logout_user',),

    url(r'review', views.review,
        name='review',),

    url(r'sizechart_update', views.sizechart_update,
        name='sizechart_update',),

    url(r'createdress', views.createdress,
        name='createdress',),

    url(r'customizedress', views.customizedress,
        name='customizedress',),

    url(r'showproducts', views.showproducts,
        name='showproducts',),

    url(r'addproduct', views.addproduct,
        name='addproduct',),

    url(r'addcategory', views.addcategory,
        name='addcategory',),

    url(r'addsubcategory', views.addsubcategory,
        name='addsubcategory',),

    url(r'admin_deleteproduct', views.deleteproduct,
        name='deleteproduct',),

    url(r'adminupload', views.adminupload,
        name='adminupload',),

    url(r'profile', views.user_profile,
        name='user_profile',),

    url(r'price', views.price,
        name='price',),

    url(r'filter_color', views.filter_color,
        name='filter_color',),

    url(r'filter_occasion', views.filter_occasion,
        name='filter_occasion',),

    url(r'address', views.user_profile_address,
        name='user_profile_address',),

    url(r'pastorders', views.user_profile_pastorders,
        name='user_profile_pastorders',),
    url(r'wishlist', views.user_profile_wishlist,
        name='user_profile_wishlist',),

    url(r'add_wish', views.add_wish,
        name='add_wish',),
    url(r'creditcard', views.user_profile_creditcard,
        name='user_profile_creditcard',),
    url(r'sizechart', views.user_profile_sizechart,
        name='user_profile_sizechart',),
)
