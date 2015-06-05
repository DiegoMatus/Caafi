from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from caafi.models import Language, Category, Subcategory

# Create your views here.
def index(request):
	languages = Language.objects.all()

	languages_names = []
	for language in languages:
		languages_names.append(language.name)

	return render_to_response('caafi/index.html', {'languages' : languages, 'languages_names' : languages_names.sort()})

def lista_categorias(request, language_name):
	languages = Language.objects.all();
	language_id = Language.objects.filter(slug=language_name)[0].id
	language = get_object_or_404(Language, pk=language_id)
	#menu_name = language.name
	categories = language.categories.all()
	
	return render_to_response('caafi/categories.html', {'languages' : languages, 'menu' : language, 'language' : language_name, 'categories' : categories})

def lista_subcategorias(request, language_name, category_name):
	languages = Language.objects.all();
	language_id = Language.objects.filter(slug=language_name)[0].id
	language = get_object_or_404(Language, pk=language_id)
	#menu_name = language.name
	categories = language.categories.all()
	category_id = Category.objects.filter(slug=category_name)[0].id
	category = get_object_or_404(Category, pk=category_id)
	subcategories = category.subcategories.all()
	return render_to_response('caafi/subcategories.html', {'languages' : languages, 'menu' : language, 'language' : language_name, 'categories' : categories, 'category' : category.name, 'subcategories' : subcategories})

def lista_urls(request, language_name, category_name, subcategory_name):
	languages = Language.objects.all();
	language_id = Language.objects.filter(slug=language_name)[0].id
	language = get_object_or_404(Language, pk=language_id)
	#menu_name = language.name
	categories = language.categories.all()
	category_id = Category.objects.filter(slug=category_name)[0].id
	category = get_object_or_404(Category, pk=category_id)
	subcategory_id = Subcategory.objects.filter(slug=subcategory_name)[0].id
	subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
	urls = subcategory.urls2.all()
	return render_to_response('caafi/urls.html', {'languages' : languages, 'menu' : language, 'language' : language_name, 'categories' : categories, 'urls' : urls, 'subcategory' : subcategory.name})

def urls_reportadas(request):
	if request.POST:
		reported_url = request.POST.get("reported_url", '')
		ru = Reported_Urls()
		ru.address = reported_url
		ru.save()
		return JsonHttpResponse({'msj' : "Se ha reportado la URL"})