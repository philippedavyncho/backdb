# Generated by Django 5.0.3 on 2024-03-08 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boutique', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=1)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit', to='boutique.produit')),
            ],
        ),
    ]
