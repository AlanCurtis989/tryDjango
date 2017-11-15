from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based view
def home(request):
    #return HttpResponse("This is home page LLLLLLL")
    return render(request, "home.html", {"myVar":"I am a variable"})#response

def about(request):
    return render(request, "about.html", {"myVar":"Home2"})#response

def contact(request):
    return render(request, "contact.html", {"myVar":"HOME3"})#response