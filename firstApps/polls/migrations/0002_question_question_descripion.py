# Generated by Django 3.0.5 on 2020-05-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_descripion',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
