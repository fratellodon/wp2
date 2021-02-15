from django.db import models

class Document(models.Model):
    page_number = models.IntegerField ('Номер страницы')
    main_field = models.TextField('Главное поле')
    name1 = models.CharField('Первое имя', max_length=50)
    surname1 = models.CharField('Первая фамилия', max_length=50)
    date1 = models.CharField('Первая дата', max_length=10)
    name2 = models.CharField('Второе имя', max_length=50)
    surname2 = models.CharField('Вторая фамилия', max_length=50)
    date2 = models.CharField('Вторая дата', max_length=10)
    name3 = models.CharField('Третье имя', max_length=50)
    surname3 = models.CharField('Третья фамилия', max_length=50)
    date3 = models.CharField('Третья дата', max_length=10)
    name4 = models.CharField('Четвертое имя', max_length=50)
    surname4 = models.CharField('Четвертое фамилия', max_length=50)
    date4 = models.CharField('Четвертая дата', max_length=10)
    add_field = models.TextField('Поле для спец обозначений')
    text_field = models.TextField('Дополнительное поле')
    company = models.CharField('Название компании', max_length=200)

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'БД'