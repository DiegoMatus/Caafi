from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
	'''Se puede registrar cualquier cantidad de idiomas.'''
	name = models.CharField('Nombre', max_length=50)
	#image = models.ImageField(upload_to="/images")
	slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unicode(self.name))
		super(Language, self).save()

	def get_absolute_url(self):
		return "/tag/%s/" % (self.slug)

	def __str__(self):
		return self.name

class Attendant(models.Model):
	name = models.OneToOneField(User)
	language = models.ManyToManyField(Language, verbose_name='Idioma')

	def __str__(self):
		return  self.name.username

class Category(models.Model):
	'''Una categoría puede pertenecer a varios idiomas y de igual forma un idioma puede contener una o varias categorías registradas.'''
	name = models.CharField('Nombre', max_length=50)
	languages = models.ManyToManyField(Language, verbose_name='Idioma', related_name='categories')

	def __str__(self):
		return self.name
		

class Subcategory(models.Model):
	'''Cada categoría cuenta debería contar con varias subcategorías y estás a su vez sólo deben estar disponibles en los idiomas a los que se le asocie.'''
	name = models.CharField('Nombre', max_length=50)
	category = models.ForeignKey(Category, verbose_name='Categoria', related_name='subcategories')
	language = models.ManyToManyField(Language, verbose_name='Idioma', related_name='subcategories')

	def __str__(self):
		return self.name

class Competence(models.Model):
	'''Catálogo de competencias que podrán ser seleccionadas al registrar una nueva URL'''
	name = models.CharField('Nombre', max_length=50)

	def __str__(self):
		return self.name

class Exercise(models.Model):
	'''Catálogo de los diferentes tipos de ejercicio que podrán ser seleccionadas al registrar una nueva URL'''
	name = models.CharField('Nombre', max_length=50)

	def __str__(self):
		return self.name

class Url(models.Model):
	'''Una URL está registrada dentro de una o varias subcategorías pertenecientes a una misma categoría de un idioma'''
	CORRECTIONS= (
		('SI', 'Tiene correción'),
		('SI+', 'Tiene correción más explicación'),
		('NO', 'No tiene correción'),
		('NA', 'No aplica')
	)	
	ITEMS= (
		('EJE', 'Ejemplos'),
		('MIN', 'Minutos'),
		('PAG', 'Páginas'),
		('REA', 'Reactivos'),
		('SEG', 'Segundos')
	)
	LEVELS= (
		('A1', 'A1 - Principiante'),
		('A2', 'A2 - Intermedio bajo'),
		('B1', 'B1 - Intermedio'),
		('B2', 'B2 - Intermedio alto'),
		('C1', 'C1 - Avanzado'),
		('C2', 'C2 - Perfeccionamiento')
	)

	address = models.URLField('Dirección', max_length=200)
	description = models.TextField('Descripción', default='Escribe una descripción')
	language = models.ForeignKey(Language, verbose_name='Idioma', related_name='urls', default=0)
	category = models.ForeignKey(Category, verbose_name='Categoría', related_name='urls1', default=0)
	subcategories = models.ManyToManyField(Subcategory, verbose_name='Subcategorías', related_name='urls2')
	level = models.CharField('Nivel', max_length=2, choices=LEVELS, blank=False, default='---------')
	primary_competence = models.ForeignKey(Competence, verbose_name='Competencia primaria', related_name='urls3')
	secondary_competence = models.ForeignKey(Competence, verbose_name='Competencia secundaria', related_name='urls4')
	kind_exercise = models.ForeignKey(Exercise, verbose_name='Tipo de ejercicio', related_name='urls5')
	kind_item = models.CharField('Tipo de item', max_length=3, choices=ITEMS, blank=False, default='---------')
	number_items = models.IntegerField('Número de items/ Duración')
	kind_correction = models.CharField('Tipo de correción', max_length=3, choices=CORRECTIONS, blank=False, default='---------')
	status = models.BooleanField('Disponible', default=True)
	published = models.DateTimeField(auto_now_add=True, default=timezone.now().date())
	
	def __str__(self):
		return self.address