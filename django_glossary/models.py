from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Term(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('django_glossary:term-detail',
                       kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title', '-modified']


class Synonym(models.Model):
    title = models.CharField(max_length=250)
    term = models.ForeignKey(Term,
                             on_delete=models.PROTECT,
                             related_name="synonyms")

    def __str__(self):
        return f"{self.title} (synonym for {self.term.title})"

    def get_absolute_url(self):
        return reverse('django_glossary:term-detail',
                       kwargs={'slug': self.term.slug})
