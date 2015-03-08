from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from caafi.models import Language, Category, Subcategory

# Create your views here.
def index(request):
	languages = Language.objects.all()
	return render_to_response('caafi/index.html', {'languages' : languages})

def catalog(request, language_id):
	language = get_object_or_404(Language, pk=language_id)
	categories = language.categories.all()
	subcategories = language.subcategories.all()
	#return HttpResponse('Soy una lista de Url\'s :33')
	return render_to_response('caafi/catalogo.html', {'categories' : categories, 'subcategories' : subcategories})

def url_list(request):
	return HttpResponse('Soy una lista de Url\'s :33')

def search(request):
	return HttpResponse('Resultados de búsqueda :3333')