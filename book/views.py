#from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import Emenitites, Book
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Emenitites, Book

@login_required(login_url="/login/")
def home(request):
    emenities = Emenitites.objects.all()
    books = Book.objects.all()  # Add this line to get all book objects
    context = {
        'emenities': emenities,
        'books': books  # Include the books in the context
    }
    return render(request, 'home.html', context)


@login_required(login_url="/login/")
def api_books(request):
    books_objs = Book.objects.all()

    # Search functionality
    search_query = request.GET.get('search', None)
    if search_query:
        books_objs = books_objs.filter(
            Q(book_name__icontains=search_query) | 
            Q(book_description__icontains=search_query)
        )

    # Filter by price
    price = request.GET.get('price')
    if price:
        books_objs = books_objs.filter(price__lte=price)

    # Filter by emenities
    emenities = request.GET.get('emenities')
    if emenities:
        emenities = [int(e) for e in emenities.split(',') if e.isdigit()]
        books_objs = books_objs.filter(emenities__in=emenities).distinct()

    # Prepare payload ensuring book_image is converted to URL
    payload = [{
        'book_name': book.book_name,
        'book_description': book.book_description,
        'book_image': request.build_absolute_uri(book.book_image.url) if book.book_image else None,
        'price': book.price
    } for book in books_objs]

    return JsonResponse(payload, safe=False)



def login_page(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user_obj = User.objects.filter(username=username)
			
			if not user_obj.exists():
				messages.error(request, "Username not found")
				return redirect('/login/')
			
			user_obj = authenticate(username=username, password=password)
			
			if user_obj:
				login(request, user_obj)
				return redirect('/')
			
			messages.error(request, "Wrong Password")
			return redirect('/login/')
			
		except Exception as e:
			messages.error(request, "Something went wrong")
			return redirect('/register/')
		
	return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('/register/')
        
        try:
            # Create the user with hashed password
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Account created successfully")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('/register/')
    else:
        # Handle GET requests
        return render(request, "register.html")


def custom_logout(request):
	logout(request)
	return redirect('login_page')





from django.shortcuts import render, redirect
from .models import PDF
from .forms import PDFForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PDFForm()
    return render(request, 'upload_pdf.html', {'form': form})

def pdf_list(request):
    pdfs = PDF.objects.all()
    return render(request, 'pdf_list.html', {'pdfs': pdfs})



from django.shortcuts import render, get_object_or_404
from .models import Book


def read_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  # Use pk for primary key
    return render(request, 'read_book.html', {'book': book})
