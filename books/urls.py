from django.urls import path
from books import views

urlpatterns=[
    # /books/
    path('',views.BooksModelView.as_view(),name="index"),
    # /books/book/
    path('book/',views.BookList.as_view(),name='book_list'),
    # /books/book/2/
    path('book/<int:pk>/',views.BookDetail.as_view(),name="book_detail"),
    path('author/',views.AuthorList.as_view(),name='author_list'),
    path('author/<int:pk>/',views.AuthorDetail.as_view(),name='author_detail'),
    path('publisher/',views.PublisherList.as_view(),name='publisher_list'),
    path('publisher/<int:pk>/',views.PublisherDetail.as_view(),name='publisher_detail'),
]