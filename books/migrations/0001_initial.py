# Generated by Django 3.2.25 on 2024-12-19 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Биография')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('year', models.PositiveIntegerField(verbose_name='Год издания')),
                ('genre', models.CharField(max_length=100, verbose_name='Жанр')),
                ('category', models.CharField(choices=[('fiction', 'Художественное произведение'), ('textbook', 'учебное пособие'), ('detective', 'Детектив')], max_length=100, verbose_name='Категория')),
                ('publisher', models.CharField(max_length=100, verbose_name='Издатель')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Обложка')),
                ('book_file', models.FileField(blank=True, null=True, upload_to='books/', verbose_name='Файл книги')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author', verbose_name='Автор')),
            ],
            options={
                'unique_together': {('title', 'author', 'year', 'publisher')},
            },
        ),
    ]
