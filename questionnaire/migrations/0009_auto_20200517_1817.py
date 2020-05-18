# Generated by Django 2.2.12 on 2020-05-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_auto_20200504_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersdata',
            name='answer_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questionsdata',
            name='target',
            field=models.CharField(choices=[('1', 'self'), ('2', 'parent_child'), ('3', 'teacher_child')], default='1', max_length=200),
        ),
    ]