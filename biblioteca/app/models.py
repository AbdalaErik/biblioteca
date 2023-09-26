from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf =  models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.uf}'

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    preco = models.PositiveIntegerField()
    data_publicacao = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} {self.autor} {self.editora} {self.categoria} {self.preco} {self.data_publicacao} {self.status}'

class Leitor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.email} {self.cpf}'
    
class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f'{self.data_emprestimo} {self.livro} {self.leitor} {self.data_devolucao}'