from django.db import models


class Category(models.Model): # male, famela
  category = models.CharField(max_length=100, verbose_name='Категория')

  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

  def __str__(self):
    return self.category


class Gender(models.Model): # male, famela
  gender = models.CharField(max_length=50, verbose_name='Пол')

  class Meta:
    verbose_name = 'Пол'
    verbose_name_plural = 'Пол'

  def __str__(self):
    return self.gender


class City(models.Model):
  city = models.CharField(max_length=100, verbose_name='Город')

  class Meta:
    verbose_name = 'Город'
    verbose_name_plural = 'Города'

  def __str__(self):
    return self.city


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


class HasExperience(models.Model):
  has_experience = models.CharField(max_length=50, verbose_name='Имеется ли опыт работы')

  class Meta:
    verbose_name = 'Имеется ли опыт Работы'
    verbose_name_plural = 'Имеется ли опыт Работы'

  def __str__(self):
    return self.has_experience


class ExperinceYear(models.Model): # no, 1 to 3, 3 to 6
  experience_year = models.CharField(max_length=100, verbose_name="Опыт работы")

  class Meta:
    verbose_name = 'Опыт Работы'
    verbose_name_plural = 'Опыт Работы'

  def __str__(self):
    return self.experience_year


class Education(models.Model):
  education = models.CharField(max_length=50, verbose_name='Образование')

  class Meta:
    verbose_name = 'Образование'
    verbose_name_plural = 'Образовании'

  def __str__(self):
    return self.education


class Language(models.Model):
  language = models.CharField(max_length=50, verbose_name='Языки')

  class Meta:
    verbose_name = 'Языки'
    verbose_name_plural = "Языки"

  def __str__(self):
    return self.language


class Skills(models.Model):
  skills =  models.CharField(max_length=100, verbose_name='Навыки')

  class Meta:
    verbose_name = 'Навыки'
    verbose_name_plural = "Навыки"

  def __str__(self):
    return self.skills


class Removal(models.Model):
  removal = models.CharField(max_length=50, verbose_name='Готовность к переездам')

  class Meta:
    verbose_name = 'Готовность к переездам'
    verbose_name_plural = "Готовность к переездам"

  def __str__(self):
    return self.removal


class CreateResume(models.Model):
  name = models.CharField(max_length=100, verbose_name='Имя')
  last_name = models.CharField(max_length=100, verbose_name='Фамилия')
  birth_date = models.DateField(verbose_name='Дата Рождения')
  gender = models.ForeignKey(Gender, related_name='gender_choices', on_delete=models.SET_NULL, null=True, verbose_name='Пол') #, null=True, blank=True
  city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='city_choices', verbose_name='Город', null=True)#, null=True, blank=True
  image = models.ImageField(upload_to="uploads/", blank=True, null=True, verbose_name='Фото')
  has_experience = models.ForeignKey(HasExperience, related_name='has_experience_choices', on_delete=models.SET_NULL, null=True, verbose_name='Опыт работы') #, null=True, blank=True

  title = models.CharField(max_length=100, verbose_name="Заголовок Резюме")
  category = models.ForeignKey(Category, verbose_name="Категория", related_name="category_choices", on_delete=models.CASCADE, null=True)
  salary = models.CharField(max_length=100, verbose_name='Желаемая Зароботная Плата')
  education = models.ForeignKey(Education, related_name='education_choices', on_delete=models.SET_NULL, verbose_name='Образование', null=True)#, null=True, blank=True
  language = models.ManyToManyField('Language', related_name="languages_choices", verbose_name='Языки') #on_delete=models.SET_NULL, null=True, blank=True
  skills = models.ManyToManyField('Skills', related_name='skills_choices', verbose_name='Навыки') #, on_delete=models.SET_NULL, null=True, blank=True

  last_place_work = models.CharField(max_length=100, verbose_name="Последние место работы", blank=True, null=True)
  experience_year = models.ForeignKey(ExperinceYear, related_name='experince_year', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Опыт работы годами')
  # data_begin = models.DateField(verbose_name='Начало', null=True, blank=True)
  data_finish = models.DateField(verbose_name='Конец', null=True, blank=True)
  company_name = models.CharField(max_length=100, verbose_name='Название Компании', blank=True, null=True)
  status = models.CharField(max_length=100, verbose_name='Должность предыдущий работы', blank=True, null=True)
  info = models.CharField(max_length=100, verbose_name='Рабочие обязанности', blank=True, null=True)

  travel = models.ForeignKey(Removal, related_name='removal_choices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Готовность к переездам')
  schedule = models.ForeignKey(ScheduleTime, related_name='schedule_time_choices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Режим Работы')
  time_work = models.ForeignKey(TimeWork, related_name='time_work_choices', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='График Работы')
  created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey('auth.User', related_name='worker_ids', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Резюме'
    verbose_name_plural = 'Резюме'

  def __str__(self):
    return self.title

  def get_image(self):
    if self.image:
      return 'http://127.0.0.1:8000' + self.image.url
    return ''

  def get_absolute_url(self):
    return f'/{self.category.id}/{self.id}/'