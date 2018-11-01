from django.shortcuts import render
import django.contrib.sessions
from .models import Book, Author, BookInstance, Genre
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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


"""
def book_detail_view(request,pk):
	try:
		book_id=Book.objects.get(pk=pk)
	except Book.DoesNotExist:
		raise Http404("Book does not exist")

	#book_id=get_object_or_404(Book, pk=pk)
	
	return render(
		request,
		'catalog/book_detail.html',
		context={'book':book_id,}
"""

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