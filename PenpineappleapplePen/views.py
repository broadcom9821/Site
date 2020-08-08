from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'app/index.html')

def EGE_I_GIA(request):
	return render(request,'app/About/EGE_I_GIA.html')
def Mattex_obesp(request):
	return render(request,'app/About/Mattex_obesp.html')
def Obr_model(request):
	return render(request,'app/About/Obr_model.html')
def Obr_stand(request):
	return render(request,'app/About/Obr_stand.html')
def Dop_obraz(request):
	return render(request,'app/About/Dop_obraz.html')
def about(request):
	return render(request, 'app/About/about.html')
def contact(request):
	return render(request, 'app/About/contact.html')
def Gallery(request):
	return render(request, 'app/About/Gallery.html')
def History(request):
	return render(request, 'app/About/History.html')
def SMI(request):
	return render(request, 'app/About/SMI.html')
def Team(request):
	return render(request, 'app/About/Team.html')
def fullwidth(request):
	return render(request,'app/full-width.html')
def sidebar(request):
	return render(request,'app/sidebar.html')
def faq(request):
	return render(request,'app/faq.html')
def error(request):
	return render(request,'app/404.html')

def services(request):
	return render(request,'app/services.html')