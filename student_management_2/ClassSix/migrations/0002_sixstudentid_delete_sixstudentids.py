# Generated by Django 5.1.7 on 2025-04-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassSix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SixStudentID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('FatherName', models.CharField(max_length=20)),
                ('MotherName', models.CharField(max_length=20)),
                ('roll', models.IntegerField(max_length=5)),
                ('StudentID', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='SixStudentIDS',
        ),
    ]
