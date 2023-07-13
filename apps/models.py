from django.db.models import Model, CharField, IntegerField, TextField, ForeignKey, CASCADE


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = IntegerField(default=0)
    category = ForeignKey('Category', CASCADE)
