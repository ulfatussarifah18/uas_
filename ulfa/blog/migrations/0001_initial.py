# Generated by Django 4.1.3 on 2022-12-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hoby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Makanan', models.CharField(max_length=50)),
                ('Minuman', models.CharField(max_length=50)),
                ('warna', models.CharField(max_length=50)),
            ],
        ),
    ]