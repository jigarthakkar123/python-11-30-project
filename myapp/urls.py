from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('performer/',views.performer,name='performer'),
    path('Program/',views.Program,name='Program'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('venue/',views.venue,name='venue'),
    path('elements/',views.elements,name='elements'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('profile/',views.profile,name='profile'),
    path('artist-profile/',views.artist_profile,name='artist-profile'),
    path('artist-details/<int:pk>/',views.artist_details,name='artist-details'),
    path('book-artist/<int:pk>/',views.book_artist,name='book-artist'),
    path('mybookings/',views.mybookings,name='mybookings'),
    path('confirm-booking/<int:pk>/',views.confirm_booking,name='confirm-booking'),
    path('create-checkout-session/', views.create_checkout_session, name='payment'),
    path('success.html/',views.success,name='success'),
    path('cancel.html/',views.cancel,name='cancel'),
]