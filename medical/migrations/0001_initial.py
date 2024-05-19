# Generated by Django 4.2.13 on 2024-05-18 22:32

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
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название отделения (например кардиология)')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время для записи на прием')),
            ],
            options={
                'verbose_name': 'Время приема',
                'verbose_name_plural': 'Время приема',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Должность (например акушер)')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medical.department', verbose_name='Отдел которому принадлежит должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адресс проживания')),
                ('blood_type', models.CharField(blank=True, choices=[('O(|) Rh-', 'One Negative'), ('O(|) Rh+', 'One Positive'), ('A(||) Rh-', 'Two Negative'), ('A(||) Rh+', 'Two Positive'), ('B(|||) Rh-', 'Three Negative'), ('B(|||) Rh+', 'Three Positive'), ('AB(|V) Rh-', 'Four Negative'), ('AB(|V) Rh+', 'Four Positive')], max_length=10, null=True, verbose_name='Группа крови')),
                ('gender', models.CharField(blank=True, choices=[('женщина', 'Female'), ('мужчина', 'Male')], max_length=7, null=True, verbose_name='Пол пациента')),
                ('place_of_work', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место работы')),
                ('hobbies', models.CharField(blank=True, max_length=255, null=True, verbose_name='Увлечения')),
                ('discount_status', models.SmallIntegerField(default=0, verbose_name='Скидка пациента на услуги')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1500, verbose_name='Отзыв о центре медицинской диагностики')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать отзыв о клинике')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Отзыв клиента (пациента)',
                'verbose_name_plural': 'Отзывы клиентов (пациентов)',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=255, null=True, verbose_name='Образование')),
                ('awards', models.CharField(blank=True, max_length=255, null=True, verbose_name='Награды')),
                ('experience', models.DateField(blank=True, null=True, verbose_name='Стаж с "дата"')),
                ('status_appointment', models.BooleanField(blank=True, default=True, null=True, verbose_name='Статус врача, True - можно записаться на прем')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medical.post', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата приема')),
                ('status', models.CharField(choices=[('Активный', 'Active'), ('Отменён', 'Cancel'), ('Завершен', 'Completed')], default='Активный', max_length=8, verbose_name='Статус записи на прием')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_name', to='medical.doctor', verbose_name='Врач')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medical.time', verbose_name='Время приема')),
            ],
            options={
                'verbose_name': 'Запись на прием',
                'verbose_name_plural': 'Записи на прием',
            },
        ),
    ]