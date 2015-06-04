from django.contrib import admin
from caafi.models import Language, Category, Subcategory, Url, Competence, Exercise, Attendant, Reported_urls

# Register your models here.
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Url)
admin.site.register(Competence)
admin.site.register(Exercise)
admin.site.register(Attendant)
admin.site.register(Reported_urls)