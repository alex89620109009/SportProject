# Generated by Django 4.1.3 on 2022-11-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('idPost', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Img', models.ImageField(upload_to='')),
                ('Name', models.CharField(max_length=45)),
                ('Location', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=255)),
                ('First_Date_Post', models.DateTimeField(auto_now_add=True)),
                ('Edit_Date_Post', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
