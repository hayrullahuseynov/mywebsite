# Generated by Django 2.0.7 on 2021-01-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210108_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='categorie',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Politics', 'Politics'), ('Business', 'Business'), ('Health', 'Health'), ('Design', 'Design'), ('Tech', 'Tech'), ('Other', 'Other')], default='O', max_length=30),
        ),
    ]
