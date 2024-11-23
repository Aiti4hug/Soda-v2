from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name='Категории')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименования')
    description = models.TextField(verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name='Имеется')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')

    def __str__(self):
        return f'{self.title} - {self.created}'

