from django.db import models

# Create your models here.

#1 A MUCHOS

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
#MUCHOS A 1

class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)

    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nombre

#1 A 1 

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Perfil(models.Model):
    bio = models.TextField()
    
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return f"este es el perfil de: {self.usuario.nombre}"
    




