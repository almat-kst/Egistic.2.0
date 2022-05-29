from django.db import models

class Company(models.Model):
  name = models.CharField(max_length=100, verbose_name='Названия Компании')
  category = models.ManyToManyField('Category', related_name="category_list", verbose_name="Категория Компании", blank=True)
  info = models.TextField(verbose_name='O Компании')
  vakansi = models.ManyToManyField('CreateVakansi', related_name="vakansis_list", verbose_name="Вакансии Компании", blank=True)
  address = models.CharField(max_length=100, verbose_name='Адрес Компании')
  number = models.CharField(max_length=100, verbose_name='Номер Компании')

  class Meta:
    verbose_name = 'Компания'
    verbose_name_plural = 'Компании'

  def __str__(self):
    return self.name


class Category(models.Model): # male, famela
  category = models.CharField(max_length=100, verbose_name='Категория')

  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

  def __str__(self):
    return self.category


class ScheduleTime(models.Model): # partday, fullday, valontiries, intern
  schedule = models.CharField(max_length=100, verbose_name='Режим Работы')

  class Meta:
    verbose_name = 'Режим Работы'
    verbose_name_plural = 'Режим Работы'

  def __str__(self):
    return self.schedule


class TimeWork(models.Model): #full, day/night, flex, fromHome, vaxta
  time_work = models.CharField(max_length=100, verbose_name='График Работы')

  class Meta:
    verbose_name = 'График Работы'
    verbose_name_plural = 'График Работы'

  def __str__(self):
    return self.time_work


class Removal(models.Model):
  removal = models.CharField(max_length=50, verbose_name='Готовность к переездам')

  class Meta:
    verbose_name = 'Готовность к переездам'
    verbose_name_plural = "Готовность к переездам"

  def __str__(self):
    return self.removal


class City(models.Model):
  city = models.CharField(max_length=100, verbose_name='Город')

  class Meta:
    verbose_name = 'Город'
    verbose_name_plural = 'Города'

  def __str__(self):
    return self.city


class CreateVakansi(models.Model):
  title = models.CharField(max_length=100, verbose_name="Вакансия")
  category = models.ForeignKey(Category, verbose_name="Категория", related_name="category_choices", on_delete=models.CASCADE, null=True)
  company_name = models.CharField(max_length=100, verbose_name="Компания")
  city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='city_choices', verbose_name='Город', null=True)
  salary_start =  models.CharField(max_length=100, verbose_name='Зароботная Плата От')
  salary_end = models.CharField(max_length=100, verbose_name='Зароботная Плата До', null=True, blank=True)
  travel = models.ForeignKey(Removal, related_name='removal_choices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Готовность к переездам')
  schedule = models.ForeignKey(ScheduleTime, related_name='schedule_time_choices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Режим Работы')
  time_work = models.ForeignKey(TimeWork, related_name='time_work_choices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='График Работы')
  obligations = models.TextField(verbose_name='Обязательности', null=True, blank=True)
  requirements = models.TextField(verbose_name='Требования', null=True, blank=True)
  conditions = models.TextField(verbose_name='Условия', null=True, blank=True)
  owner = models.ForeignKey('auth.User', related_name='employer_ids', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Cоздрать вакансию'
    verbose_name_plural = 'Cоздрать вакансии'

  def __str__(self):
    return self.title