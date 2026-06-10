# PASOS SEGUIDOS 

1. LEVANTAR EL PROYECTO DJANGO:
- UBICARSE EN LA CARPETA DEL PROYECTO Y VERIFICAR QUE EXISTA `MANAGE.PY` Y LUEGO VERIFICAR QUE EL SERVIDOR INICIE SIN ERRORES.
---

2. LEVANTA BASE DE DATOS POSTGRESQL:
- USAR DOCKER COMPOSE PARA LEVANTAR POSTGRESQL Y PGADMIN, CREANDO UN CONTENEDOR POSTGRESQL CON:

- Base de datos: `relacionesdb`
- Usuario: `usuario`
- Contraseña: `1234`
- Puerto: `localhost`
---

3. CONFIGURAR ACCESO EN `SETTINGS.PY`

EN `CONFIG/SETTINGS.PY` SE DEFINE LA CONEXIÓN:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "relacionesdb",
        "USER": "usuario",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

SE TIENE QUE INSTALAR `psycopg2-binary` EN `requirements.txt`.
---

4. CREAR MODELOS 

EN `RELACIONES/MODELS.PY` SE AGREGAN LAS CLASES:

```python
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
```
----
5. MIGRAR A LA BASE DE DATOS
```bash
python manage.py makemigrations relaciones
python manage.py migrate
```
----
6. CREAR ENTRADAS Y CONSULTAS ORM
- EJECUTAR SHELL DE DJANGO
```bash
python manage.py shell
```
### CREAR COSULTAS ORM
- IMPORTAR:
```python
from relaciones.models import Usuario, Perfil 
```
- CREATE:
```python 
Usuario.objects.create(nombre="ana")
```
- READ:
```python 
perfil=Perfil.objects.get(id=3)
perfil.id
perfil.bio
```
- UPDATE:
```python
perfil.bio="me gustan los perros, la naturaleza y caminar"
```
- DELETE:
``` python
perfil.delete()
```






