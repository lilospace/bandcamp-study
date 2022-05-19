# Generated by Django 4.0.4 on 2022-05-18 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.musician')),
            ],
        ),
    ]