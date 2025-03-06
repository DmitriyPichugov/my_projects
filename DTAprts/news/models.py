from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Apartment(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
