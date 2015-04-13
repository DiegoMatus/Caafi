from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from caafi.models import Language, Category, Subcategory

# Create your views here.
def index(request):
	languages = Language.objects.all()
	return render_to_response('caafi/index.html', {'languages' : languages})

def catalog(request, language_name):
	language_id = Language.objects.filter(slug=language_name)[0].id
	language = get_object_or_404(Language, pk=language_id)
	categories = language.categories.all()
	return render_to_response('caafi/catalogo.html', {'language': language_name, 'categories' : categories})

def catalog_categories(request, language_name, category_name):
	language_id = Language.objects.filter(slug=language_name)[0].id
	language = get_object_or_404(Language, pk=language_id)
	category_id = Category.objects.filter(slug=category_name)[0].id
	category = get_object_or_404(Category, pk=category_id)
	subcategories = category.subcategories.all()
	return render_to_response('caafi/lista.html', {'language' : language_name, 'category' : category_name, 'subcategories' : subcategories})

def catalog_subcategories(request, language_name, category_name, subcategory_name):
	language_id = Language.objects.filter(slug=language_name)[0].id
	language = get_object_or_404(Language, pk=language_id)
	category_id = Category.objects.filter(slug=category_name)[0].id
	category = get_object_or_404(Category, pk=category_id)
	subcategory_id = Subcategory.objects.filter(slug=subcategory_name)[0].id
	subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
	urls = subcategory.urls2.all()
	return render_to_response('caafi/lista2.html', {'urls' : urls, 'subcategory' : subcategory_name})

def search(request):
	return HttpResponse('Resultados de búsqueda :3333')