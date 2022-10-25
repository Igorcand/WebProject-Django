from distutils.command.upload import upload
from django.db import models


class Document(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)
    
    #RELACIONAMENTO ONE TO ONE
    #Um documento só pode ser ligado a uma pessoa
    doc = models.OneToOneField(Document, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 

#RELACIONAMENTO MANY TO MANY
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    num = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    #RELACIONAMENTO ONE TO MANY - FOREING KEY 
    # Uma pessoa pode ter várias vendas
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)

    #RELACIONAMENTO MANY TO MANY
    #Várias vendas podem ter vários produtos, não importando com repetições
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.num