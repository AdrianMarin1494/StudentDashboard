# Generated by Django 4.1.5 on 2023-04-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_timetable_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='timetable',
            constraint=models.UniqueConstraint(fields=('day', 'hour', 'class_id'), name='unique_classroom_assignment'),
        ),
    ]
