from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/new', views.add_new_book, name='new-book'),
	path('books/all', views.BookListView.as_view(), name='books'),
	path('books/my', views.LoanedBooksByUserListView.as_view(), name='mybooks'),
	path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/new', views.add_new_author, name='new-author'),
	path('authors/all', views.AuthorListView.as_view(), name="authors"),
	path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
