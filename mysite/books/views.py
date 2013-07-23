from django.shortcuts import render
from mysite.books.models import Book


SearchKey = 'queryText'
BooksKey = 'books'
Get = 'GET'


def search(request):
    content, view = getSearchContentAndView(request)
    return render(request, view, content)


def getSearchContentAndView(request):
    errors = list()
    if SearchKey in request.GET:
        searchString = request.GET.get(SearchKey, "")
        if searchString == "":
            errors.append(enterA('search term'))
        elif len(searchString) > 20:
            errors.append(enterA('search term with less than 20 characters'))
        else:
            return getSearchResults(searchString)
    return {'errors': errors}, 'search_form.html'


def enterA(value):
    return 'Enter a %s.' % value


def getSearchResults(searchString):
    books = Book.objects.filter(title__icontains=searchString)
    view = 'search_results.html'
    content = {BooksKey: books, SearchKey: searchString}
    return content, view
