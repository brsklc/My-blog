# Generated by Django 2.0.3 on 2018-03-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180319_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
