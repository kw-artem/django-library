from django.shortcuts import render
import django.contrib.sessions

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Author, BookInstance, Genre
from .forms  import AddNewAuthorForm

def index(request):
	
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.all().count()
	
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1
	
	return render(
		request,
		'index.html',
		context={'num_books':num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_available, 'num_authors':num_authors, 'num_visits':num_visits},
	)

class AuthorListView(ListView):
	model = Author

class AuthorDetailView(DetailView):
	model = Author

class BookListView(ListView):
	model = Book

class BookDetailView(DetailView):
	model = Book

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
	model = BookInstance
	template_name ='catalog/bookinstance_list_borrowed_user.html'
	paginate_by = 10
	
	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

def add_new_author(request):

	form = AddNewAuthorForm(request.POST)

	if form.is_valid():
		form.save()

	return render(
		request,
		'catalog/add_new_author.html',
		context={'form': form},
	)

def add_new_book(request):

	form = AddNewBookForm(request.POST)

	if form.is_valid():
		form.save()

	return render(
		request,
		'catalog/add_new_book.html',
		context={'form': form},
	)	