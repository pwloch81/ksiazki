# Generated by Django 3.2 on 2022-02-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ksiazki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytuł', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('strony', models.DecimalField(decimal_places=0, max_digits=4)),
                ('jezyk', models.CharField(max_length=20)),
                ('link', models.TextField(max_length=100)),
            ],
        ),
    ]
