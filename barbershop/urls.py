from django.urls import path
from. import views

urlpatterns = [

    path('create_book/', views.createBook, name='create_book'),
    path('create_barber/', views.createBarbershop, name='create_barber'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('bookings/', views.Bookings, name='bookings'),
    #path('customer/<str:ok>/', views.customer, name='customer'),
    path('', views.home, name='barbershop-home'),
    path('about/', views.about, name='barbershop-about'),
    #path('barbershop/<str:pk>/', views.searchbarber, name='barbershop-searchbarber'),
]
