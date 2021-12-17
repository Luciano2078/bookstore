import factory

from django.contrib.auth.models import User
from product.factories import ProductFactory

from order.models import Order
from product.models import product

class UserFactory(factory.django.DjangoModelFactory):
    email = factory.faker('pystr')
    username = factory.faker('pystr')

    class Meta:
        model = User



class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.product.add(product)

    class Meta:
        model = Order
        