# Generated by Django 2.2.1 on 2019-05-25 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_classificacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of message.', max_length=120)),
                ('message', models.TextField(help_text="what's on your mind ...")),
            ],
        ),
    ]