from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

#---------------------------------------------------------
books = [
        {
            "id": 1,
            "imageLink": "https://m.media-amazon.com/images/I/81HqVRRwp3L._AC_UF1000,1000_QL80_.jpg",
            "title": "Eloquent JavaScript, Third Edition",
            "subtitle": "A Modern Introduction to Programming",
            "author": "Marijn Haverbeke",
            "published": "2018-12-04T00:00:00.000Z",
            "publisher": "No Starch Press",
            "pages": 472,
            "description": "JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
        },
        {
            "id": 2,
            "imageLink": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA23fZ2nI63qNfOLX9b1EzctxmzsPu1jHraMwQgRAzfQ&s",
            "title": "Practical Modern JavaScript",
            "subtitle": "Dive into ES6 and the Future of JavaScript",
            "author": "Nicolás Bevacqua",
            "published": "2017-07-16T00:00:00.000Z",
            "publisher": "O'Reilly Media",
            "pages": 334,
            "description": "To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This book provides a highly practical look at ES6, without getting lost in the specification or its implementation details.",
        },
        {
            "id": 3,
            "imageLink": "https://d2sofvawe08yqg.cloudfront.net/understanding-javascript-promises/s_featured?1712786953",
            "title": "Understanding ECMAScript 6",
            "subtitle": "The Definitive Guide for JavaScript Developers",
            "author": "Nicholas C. Zakas",
            "published": "2016-09-03T00:00:00.000Z",
            "publisher": "No Starch Press",
            "pages": 352,
            "description": "ECMAScript 6 represents the biggest update to the core of JavaScript in the history of the language. In Understanding ECMAScript 6, expert developer Nicholas C. Zakas provides a complete guide to the object types, syntax, and other exciting changes that ECMAScript 6 brings to JavaScript.",
        },
        {
            "id": 4,
            "imageLink": "https://m.media-amazon.com/images/I/51AOPRqoYTL.jpg",
            "title": "Speaking JavaScript",
            "subtitle": "An In-Depth Guide for Programmers",
            "author": "Axel Rauschmayer",
            "published": "2014-04-08T00:00:00.000Z",
            "publisher": "O'Reilly Media",
            "pages": 460,
            "description": "Like it or not, JavaScript is everywhere these days -from browser to server to mobile- and now you, too, need to learn the language or dive deeper than you have. This concise book guides you into and through JavaScript, written by a veteran programmer who once found himself in the same position.",
        },
        {
            "id": 5,
            "imageLink": "https://m.media-amazon.com/images/I/81LpyFBbo8L._AC_UF1000,1000_QL80_.jpg",
            "title": "Learning JavaScript Design Patterns",
            "subtitle": "A JavaScript and jQuery Developer's Guide",
            "author": "Addy Osmani",
            "published": "2012-08-30T00:00:00.000Z",
            "publisher": "O'Reilly Media",
            "pages": 254,
            "description": "With Learning JavaScript Design Patterns, you'll learn how to write beautiful, structured, and maintainable JavaScript by applying classical and modern design patterns to the language. If you want to keep your code efficient, more manageable, and up-to-date with the latest best practices, this book is for you.",
        },
        {
            "id": 6,
            "imageLink": "https://m.media-amazon.com/images/I/410f-bUBR3L.jpg",
            "title": "You Don't Know JS Yet",
            "subtitle": "Get Started",
            "author": "Kyle Simpson",
            "published": "2020-01-28T00:00:00.000Z",
            "publisher": "Independently published",
            "pages": 143,
            "description": "The worldwide best selling You Don't Know JS book series is back for a 2nd edition: You Don't Know JS Yet. All 6 books are brand new, rewritten to cover all sides of JS for 2020 and beyond.",
        },
        {
            "id": 7,
            "imageLink": "https://media.springernature.com/full/springer-static/cover-hires/book/978-1-4302-1834-0",
            "title": "Pro Git",
            "subtitle": "Everything you neeed to know about Git",
            "author": "Scott Chacon and Ben Straub",
            "published": "2014-11-18T00:00:00.000Z",
            "publisher": "Apress; 2nd edition",
            "pages": 458,
            "description": "Pro Git (Second Edition) is your fully-updated guide to Git and its usage in the modern world. Git has come a long way since it was first developed by Linus Torvalds for Linux kernel development. It has taken the open source world by storm since its inception in 2005, and this book teaches you how to use it like a pro.",
        },
        {
            "id": 8,
            "imageLink": "https://media.springernature.com/full/springer-static/cover-hires/book/978-1-4842-4221-6",
            "title": "Rethinking Productivity in Software Engineering",
            "subtitle": "Everythi ng you neeed to know about Software Engineering",
            "author": "Caitlin Sadowski, Thomas Zimmermann",
            "published": "2019-05-11T00:00:00.000Z",
            "publisher": "Apress",
            "pages": 310,
            "description": "Get the most out of this foundational reference and improve the productivity of your software teams. This open access book collects the wisdom of the 2017 \"Dagstuhl\" seminar on productivity in software engineering, a meeting of community leaders, who came together with the goal of rethinking traditional definitions and measures of productivity.",
        }
]


#---------------------------------------------------------

def index(request):
    data_context = {
        'data': books
    }
    return render(request, 'books/books.html', context=data_context)


def get_book(book_id):
    for book in books:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def store_books(request):
    data_context = {
        'data': books
    }
    return render(request, 'books/books.html', context=data_context)

def book_details(request, *args, **kwrgs):
    book_id = kwrgs.get('id')
    # print(book_id)
    book = get_book(book_id)
    # print(book)
    data_context = {
        'id': book.get('id'),
        'title': book.get('title'),
        'author': book.get('author'),
        'description': book.get('description'),
        'imageLink': book.get('imageLink')
    }
    return render(request, 'books/book_details.html', context=data_context)


def delete_book(request, **kwargs):
    book_id = kwargs.get('id')
    book = get_book(book_id)
    if book:
        books.remove(book)
    return redirect('books:home-books')


KNOWN_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
DEFAULT_IMAGE_URL = 'https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg'

def has_image_extension(url):
    url_lower = url.lower()
    return any(extension in url_lower for extension in KNOWN_IMAGE_EXTENSIONS)

def create_book(request):
    if request.method == 'POST':
        image_link = request.POST.get('Image')

        if not image_link or not has_image_extension(image_link):
            image_link = DEFAULT_IMAGE_URL

        new_book = {
            "id": len(books) + 1,
            "title": request.POST.get('title'),
            "imageLink": image_link,
            "subtitle": request.POST.get('subtitle'),
            "author": request.POST.get('author'),
            "published": request.POST.get('published'),
            "publisher": request.POST.get('publisher'),
            "pages": int(request.POST.get('pages')),
            "description": request.POST.get('description')
        }
        books.append(new_book)
        return redirect('books:home-books')
    return render(request, 'books/create_book.html')


def update_book(request, book_id):
    book = get_book(book_id)
    if request.method == 'POST' and book:
        book.update({
            "title": request.POST.get('title'),
            "subtitle": request.POST.get('subtitle'),
            "author": request.POST.get('author'),
            "published": request.POST.get('published'),
            "publisher": request.POST.get('publisher'),
            "pages": int(request.POST.get('pages')),
            "description": request.POST.get('description')
        })
        return redirect('books:book-details', id=book_id)
    return render(request, 'books/edit_book.html', context={'book': book})