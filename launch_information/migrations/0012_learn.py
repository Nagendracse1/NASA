# Generated by Django 2.2.5 on 2019-09-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch_information', '0011_facts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(default='images/None/no-img.jpg', upload_to='static/images/')),
                ('des', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]