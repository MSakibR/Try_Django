from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='dmapp\home.html')

def product(request):
    return render(request,template_name='dmapp\ppp.html')

def productdetails(request):
    return render(request,template_name='dmapp\ddd.html')

