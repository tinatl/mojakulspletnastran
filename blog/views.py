from django.shortcuts import render
from blog.models import Page

# Create your views here.
def prva_stran(request):
    return render(request, 'prva.html', {})
    
    
def talepsa(request):
    strani = Page.objects.all() 
    
    return render(request, 'index.html', {"strani":strani})
	