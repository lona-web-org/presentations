class ProductBase:
    instances = []

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

        self.id = len(self.instances) + 1

    def __repr__(self):
        return f'<Product(id={self.id!r}, name={self.name!r})>'

    @classmethod
    def create(cls, *args, **kwargs):
        cls.instances.append(cls(*args, **kwargs))

    @classmethod
    def all(cls):
        return cls.instances

    @classmethod
    def get(cls, id):
        for instance in cls.instances:
            if instance.id == id:
                return instance

        raise RuntimeError(f'no instance with id={id!r}')

    @classmethod
    def load_from_backup(cls):
        cls.instances.clear()

        Product.objects.create('Mouse', 'Simple Computer Mouse', 10.0)
        Product.objects.create('Keyboard', 'Simple Computer Keyboard', 30.0)
        Product.objects.create('Gaming Keyboard', 'Simple Computer Keyboard', 120.0)

    def delete(self):
        self.instances.remove(self)


class Product(ProductBase):
    objects = ProductBase


Product.objects.load_from_backup()
