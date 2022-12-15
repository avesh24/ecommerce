from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *

urlpatterns = [
    path("",views.home),
    path("about/",views.about,name="about"),
    path("contact/",views.contact_view,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("profile/",views.ProfileView.as_view(),name='profile'),
    path("address/",views.address,name='address'),
    path("updateAddress/<int:pk>",views.UpdateAddressView.as_view(),name="updateAddress"),
    path("add-to-cart/",views.add_to_cart,name='add_to_cart'),
    path("cart/",views.show_cart,name='showcart'),
    path("checkout/",views.Checkout.as_view(),name='checkout'),
    path("pluscart/",views.plus_cart),
    path("minuscart/",views.minus_cart),
    path("removecart/",views.remove_cart),
    path("pluswishlist/",views.plus_wishlist),
    path("minuswishlist/",views.minus_wishlist),
    
    
    
    # logIn 
    path("signUp/",views.CustomerSignUpView.as_view(),name="signUp"),
    path('login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form = LoginForm),name='login'),

    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name="passwordchange"),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name="passwordchangedone"),
    path("logout/",auth_view.LogoutView.as_view(next_page='login'),name="logout"),
    
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confrim/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confrim.html',form_class=MySetPasswordForm),name="password_reset_confrim"),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name="password_reset_complete"),
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)