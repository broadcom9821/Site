from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'app/index.html')
def contact(request):
	return render(request,'app/contact.html')
def fullwidth(request):
	return render(request,'app/full-width.html')
def sidebar(request):
	return render(request,'app/sidebar.html')
def faq(request):
	return render(request,'app/faq.html')
def error(request):
	return render(request,'app/404.html')
def about(request):
	return render(request,'app/about.html')
def services(request):
	return render(request,'app/services.html')