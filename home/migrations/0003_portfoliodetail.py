# Generated by Django 3.0.7 on 2021-10-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_education_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('project_url', models.URLField()),
                ('description', models.TextField()),
                ('image_1', models.ImageField(upload_to='image/%y/%m/%d')),
                ('image_2', models.ImageField(upload_to='image/%y/%m/%d')),
                ('image_3', models.ImageField(upload_to='image/%y/%m/%d')),
            ],
        ),
    ]
