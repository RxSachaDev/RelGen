# Generated by Django 4.2.7 on 2024-01-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourates', '0011_christ_delete_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epiphanie', models.DateField()),
                ('chandeleur', models.DateField()),
                ('careme', models.DateField()),
                ('mercredi', models.DateField()),
                ('paques', models.DateField()),
                ('ascension', models.DateField()),
                ('pentecote', models.DateField()),
                ('fete', models.DateField()),
                ('toussaint', models.DateField()),
                ('noel', models.DateField()),
            ],
        ),
    ]
