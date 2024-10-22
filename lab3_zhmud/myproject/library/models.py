# app/models.py
from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)

class Reader(models.Model):
    city = models.CharField(max_length=255, null=False)
    street = models.CharField(max_length=255, null=False)
    house_number = models.CharField(max_length=10, null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=10, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    publication_year = models.IntegerField(null=False)

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_year = models.IntegerField(null=False)
    death_year = models.IntegerField(null=True)  # Це поле може бути пустим

class BookAtLibrary(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class BookByAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class BookCategory(models.Model):
    name = models.CharField(max_length=100, null=False)

class BookByCategory(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class LibraryMember(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)

class BorrowHistory(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=False)
    return_date = models.DateField(null=True)  # Це поле може бути пустим

class LoanStatus(models.Model):
    status_name = models.CharField(max_length=50, null=False)
