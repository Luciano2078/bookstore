import factory

from product.models import Product, category
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.faker('pystr')
    slug = factory.faker('pystr')
    description = factory.faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category



class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.faker('pyint')
    category = factory.lazy_attribute(CategoryFactory)
    title = factory.faker('pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)


    class Meta:
        model = Product            