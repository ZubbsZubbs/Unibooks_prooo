# book/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Home view at the root of the 'book' app
    path('api_books/', views.api_books, name='api_books'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('pdf_list/', views.pdf_list, name='pdf_list'),
    path('books/read/<int:book_id>/', views.read_book, name='read_book'),
]
