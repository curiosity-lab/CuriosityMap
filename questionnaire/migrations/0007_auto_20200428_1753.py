# Generated by Django 2.2.12 on 2020-04-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20200428_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='questionnairesdata',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='questionnairesdata',
            name='question_number',
        ),
        migrations.AddField(
            model_name='questionnairesdata',
            name='question_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.QuestionsData'),
        ),
        migrations.AlterField(
            model_name='questionsdata',
            name='target',
            field=models.CharField(choices=[('3', 'teacher_child'), ('1', 'self'), ('2', 'parent_child')], default='1', max_length=200),
        ),
        migrations.AddField(
            model_name='questionnairesdata',
            name='answer_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.AnswersData'),
        ),
    ]