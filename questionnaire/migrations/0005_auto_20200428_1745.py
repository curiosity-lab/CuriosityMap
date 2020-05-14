# Generated by Django 2.2.12 on 2020-04-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_questionnaireexplanation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnairesdata',
            name='question',
        ),
        migrations.AddField(
            model_name='questionnairesdata',
            name='question_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionsdata',
            name='question_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionsdata',
            name='target',
            field=models.CharField(choices=[('1', 'בכלל לא מתאר אותי'), ('2', 'מתאר אותי במידה מעטה מאוד'), ('3', 'מתאר אותי במידה מעטה'), ('4', 'מתאר אותי במידה בינונית'), ('5', 'מתאר אותי במידה רבה'), ('6', 'מתאר אותי במידה רבה מאוד'), ('7', 'מתאר אותי באופן מלא (לגמרי אני)')], default='1', max_length=200),
        ),
    ]