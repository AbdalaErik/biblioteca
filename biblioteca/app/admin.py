from django.contrib import admin
from app.models import *

# Register your models here.

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Categoria)
admin.site.register(Livro)
admin.site.register(Cidade)
admin.site.register(Emprestimo)
admin.site.register(Leitor)