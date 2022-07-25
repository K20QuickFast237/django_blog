from distutils.command.upload import upload
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your models here.

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='titre')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Auteur')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Modifié le')
    created_on = models.DateField(blank=True, null=True, verbose_name='Créé le')
    published = models.BooleanField(default=False, verbose_name='Publié')
    content = models.TextField(blank=True, verbose_name='contenu')
    tumbnail = models.ImageField(blank=True, upload_to='blog')

    @property
    def author_or_default(self):
        return self.author.username if self.author else 'Un Auteur Inconnu'


    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:home')   # posts est l'espace de nomage défini par app_name = "posts" dans le fichier urls du dossior posts. Il permet d'avoir le meme nom d'urls pour des chemins différents
        