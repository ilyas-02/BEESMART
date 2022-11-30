from django.db import models


class Shop(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=100)
    email = models.CharField(verbose_name='Em@il', max_length=100)
    website = models.CharField(verbose_name='Вебсайт', max_length=100)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазин'

    def __str__(self):
        return self.name


class Sale(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='Магаазин', on_delete=models.CASCADE, related_name='sales')
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    image = models.ImageField(verbose_name='Картирнка', upload_to='images/')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акция'

    def __str__(self):
        return self.name


class Lottery(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='Магаазин', on_delete=models.CASCADE, related_name='lotteries')
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    image = models.ImageField(verbose_name='Картирнка', upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Лоторея'
        verbose_name_plural = 'Лотореи'

    def __str__(self):
        return self.name


class Prize(models.Model):
    lottery = models.ForeignKey(Lottery, verbose_name='Лоторея', on_delete=models.CASCADE, related_name='prizes')
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)
    image = models.ImageField(verbose_name='Картирнка', upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Приз'
        verbose_name_plural = 'Призы'

    def __str__(self):
        return self.name
# bess
