from django_faker import Faker
from caafi.models import Language, Competence, Exercise, Category, Subcategory
#this Populator is only a function thats return a django_faker.populator.Populator insta
#correctly initialized with a faker.generator, Generator instance, configured as above

class Populator(self):
	populator = Faker.getPopulator()

	populator.addEntity(Language, 5)
	populator.addEntity(Competence, 10)
	populator.addEntity(Exercise, 10)
	populator.addEntity(Category, 5)
	populator.addEntity(Subcategory, 30)

	insertedPks = populator.execute()