# Generated by Django 5.0.6 on 2024-05-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodes', models.JSONField(default=list)),
                ('edges', models.JSONField(default=list)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]