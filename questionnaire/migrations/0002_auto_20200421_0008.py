# Generated by Django 2.2.12 on 2020-04-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IDLinks',
        ),
        migrations.AlterField(
            model_name='questionsdata',
            name='name_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
