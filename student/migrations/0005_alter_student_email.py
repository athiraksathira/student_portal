# Generated by Django 4.0.2 on 2022-05-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
