from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

# The request parameter is automatically provided by Django whenever a view function is called in response to an
# incoming HTTP request. This means that if django matches the url to the view function in urls.py, it automatically
# passes an instance of an HTTP request to the view
def signup(request):
    # If request.method == 'POST' then we know that the form has been submitted.
    if request.method == 'POST':
        # Gather all the information from the form
        form = SignupForm(request.POST)

        if form.is_valid():
            # If the form is valid, the user will be created in the database.
            form.save()

            return redirect('/login/')
    # When the user just visits the 'sign in' page, the request is always 'GET'
    else:
        form = SignupForm()


    return render(request, 'core/signup.html', {
        'form': form
    })