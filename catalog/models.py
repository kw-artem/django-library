from django.db import models
import uuid

class Genre(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Language(models.Model):

    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True) #!
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')
    
    class Meta:
        ordering = ["due_back"]
    
    def __str__(self):
        return '%s - %s' % (self.id, self.book.title) # format py3


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
        
    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name) # format py3
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

