from django.contrib import admin
from .models import Library, Reader, Book, Author, BookAtLibrary, BookByAuthor, BookCategory, BookByCategory, LibraryMember, BorrowHistory, LoanStatus

admin.site.register(Library)
admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAtLibrary)
admin.site.register(BookByAuthor)
admin.site.register(BookCategory)
admin.site.register(BookByCategory)
admin.site.register(LibraryMember)
admin.site.register(BorrowHistory)
admin.site.register(LoanStatus)
