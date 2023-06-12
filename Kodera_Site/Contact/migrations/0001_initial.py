# Generated by Django 3.0 on 2023-06-12 19:18

import Contact.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('graduation_year', Contact.models.YearField(validators=[django.core.validators.MinValueValidator(2010), django.core.validators.MaxValueValidator(2028)])),
                ('contacted_at', models.DateTimeField(auto_now_add=True)),
                ('job_title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Contact.Job')),
            ],
        ),
    ]