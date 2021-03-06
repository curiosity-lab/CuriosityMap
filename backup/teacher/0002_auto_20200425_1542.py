# Generated by Django 2.2.12 on 2020-04-25 12:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherdata',
            name='city_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='name_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='school_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='teacher_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='topic',
            field=models.CharField(default='', max_length=200),
        ),
    ]
