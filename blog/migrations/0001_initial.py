# Generated by Django 2.1.1 on 2018-09-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, db_index=True, verbose_name='Тело поста')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
