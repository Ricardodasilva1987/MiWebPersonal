from tabnanny import verbose
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description =models.TextField(verbose_name='Descripcion')   
    image =models.ImageField(verbose_name='Imagen', upload_to='projects')#todas las imagenes que se suban se van a guardar en la carpeta media/projects
    link=models.URLField(verbose_name= 'Mas informacion',null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated =models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion') 

    class Meta:  #Se utiliza para dar detalees extendidos a la clase, ejemplo modificar el nombre project por proyecto, etc.
        verbose_name = "Proyecto"
        verbose_name_plural= "Proyectos"
        ordering = ["-created"]   # el guion delante hace que sea invertido la ordenacion

    def __str__(self) :
        return self.title
