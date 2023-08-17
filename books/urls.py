from django.urls import path
from. import views
from books.views import store_book,show_book,edit_book


urlpatterns = [
    path('',views.home),
    path('new_book_store/',views.store_book,name ='store_book'),
    path('show_book_store/',views.show_book,name ='show_book'),
    path('edit_book/<int:id>',views.edit_book,name ='edit_book'),
    path('delete_book/<int:id>',views.delete_book,name='delete_book')
]
