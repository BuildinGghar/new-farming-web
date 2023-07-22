
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view
from . forms import *
from django.contrib.auth import views as auth_views
from app.forms import MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path('', views.home, name='index'),
    path('city_product/<str:city_name>/', views.product, name='product'),
    path('product-detail/<int:id>/', views.product_details, name="product-detail"),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    
    # login
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address_view, name='address'),
    path('update_address/<int:pk>', views.updateAddress.as_view(), name='update_address'),
    path('address/<int:pk>/delete/', views.delete_address, name='delete_address'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('wishlist/', views.show_wishlist, name='wishlist'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    
    path('search/', views.search_results, name='search_results'),
    
    path('pluscart', views.plus_cart, name='plus_cart'),
    path('minuscart', views.minus_cart, name='minus_cart'),
    path('removecart', views.remove_cart, name='remove_cart'),
    path('pluswishlist/', views.plus_wishlist,),
    path('minuswishlist/', views.minus_wishlist,),
    
    
    path('customer_registration', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='app/password_change.html',form_class=MyPasswordChangeForm, success_url='/password-change-done'), name='password_change'),
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'), name='password_change_done'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    