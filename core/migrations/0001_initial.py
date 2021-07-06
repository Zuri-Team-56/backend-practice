# Generated by Django 3.2.4 on 2021-07-06 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CareerQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('student', models.CharField(max_length=255)),
                ('answer', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavedSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
