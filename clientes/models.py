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

