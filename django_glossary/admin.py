from django.contrib import admin
from django_glossary.models import Term, Synonym

class SynonymsInline(admin.StackedInline):
    model = Synonym
    extra = 1

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title',)
    search_fields = ('title', 'description')
    inlines = [SynonymsInline]


@admin.register(Synonym)
class SynonymAdmin(admin.ModelAdmin):
    pass