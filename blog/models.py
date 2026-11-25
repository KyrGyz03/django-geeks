from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите название блога')
    image = models.ImageField(upload_to='blog/', verbose_name='Загрузите фото')
    description = models.TextField(verbose_name='Укажите описание блога', blank=True)
    GENRE = (
        ('Животные', 'Животные'),
        ('Морские обитатели','Морские обитатели'),
        ('Домашние животные', 'Домашние животные'),
    )
    genre = models.CharField(max_length=100, choices=GENRE, default='Животные', verbose_name='Выберите жанр')
    created = models.DateTimeField(auto_now_add=True)

    video_url = models.URLField(null=True,blank=True, verbose_name='Укажите ссылку на видео')

    def __str__(self):
        return f'{self.title} - {self.created}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'