__author__ = 'shawn'
from django.contrib import admin
from mysite.books.models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = (Author.FirstName, Author.LastName, Author.EMail)
    search_fields = (Author.FirstName, Author.LastName)


class BookAdmin(admin.ModelAdmin):
    list_display = (Book.Title, Book.Publisher, Book.PublicationDate, )
    list_filter = (Book.PublicationDate, )
    date_hierarchy = Book.PublicationDate
    ordering = ('-' + Book.PublicationDate, )
    filter_horizontal = (Book.Authors, )
    raw_id_fields = (Book.Publisher, )


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
