# Generated by Django 3.2.13 on 2022-05-22 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Removal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removal', models.CharField(max_length=50, verbose_name='Готовность к переездам')),
            ],
            options={
                'verbose_name': 'Готовность к переездам',
                'verbose_name_plural': 'Готовность к переездам',
            },
        ),
        migrations.CreateModel(
            name='ScheduleTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=100, verbose_name='Режим Работы')),
            ],
            options={
                'verbose_name': 'Режим Работы',
                'verbose_name_plural': 'Режим Работы',
            },
        ),
        migrations.CreateModel(
            name='TimeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_work', models.CharField(max_length=100, verbose_name='График Работы')),
            ],
            options={
                'verbose_name': 'График Работы',
                'verbose_name_plural': 'График Работы',
            },
        ),
        migrations.CreateModel(
            name='CreateVakansi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Вакансия')),
                ('company_name', models.CharField(max_length=100, verbose_name='Компания')),
                ('salary_start', models.CharField(max_length=100, verbose_name='Зароботная Плата От')),
                ('salary_end', models.CharField(blank=True, max_length=100, null=True, verbose_name='Зароботная Плата До')),
                ('obligations', models.TextField(blank=True, null=True, verbose_name='Обязательности')),
                ('requirements', models.TextField(blank=True, null=True, verbose_name='Требования')),
                ('conditions', models.TextField(blank=True, null=True, verbose_name='Условия')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_choices', to='employer.category', verbose_name='Категория')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city_choices', to='employer.city', verbose_name='Город')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_ids', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_time_choices', to='employer.scheduletime', verbose_name='Режим Работы')),
                ('time_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time_work_choices', to='employer.timework', verbose_name='График Работы')),
                ('travel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='removal_choices', to='employer.removal', verbose_name='Готовность к переездам')),
            ],
            options={
                'verbose_name': 'Cоздрать вакансию',
                'verbose_name_plural': 'Cоздрать вакансии',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия Компании')),
                ('info', models.TextField(verbose_name='O Компании')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес Компании')),
                ('number', models.CharField(max_length=100, verbose_name='Номер Компании')),
                ('category', models.ManyToManyField(blank=True, related_name='category_list', to='employer.Category', verbose_name='Категория Компании')),
                ('vakansi', models.ManyToManyField(blank=True, related_name='vakansis_list', to='employer.CreateVakansi', verbose_name='Вакансии Компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
    ]
