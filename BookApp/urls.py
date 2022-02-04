from django.urls import path
from .views import CreateBookView,uploadBookView,allBooksView,showBookView
urlpatterns = [
    # path('add/',CreateBookView.as_view(),name='add_book'),
    path('add/',uploadBookView,name='add_book'),
    path('show/',allBooksView,name='all_books'),
    path('showbook/',showBookView,name='show_book'),
]