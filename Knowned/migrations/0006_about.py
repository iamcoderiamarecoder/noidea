# Generated by Django 4.0.4 on 2022-05-02 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Knowned', '0005_alter_investors_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('about_desc', models.TextField(default='')),
            ],
        ),
    ]
