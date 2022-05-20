# Generated by Django 4.0.4 on 2022-05-20 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0004_delete_album'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='musicians',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musicians.musician'),
        ),
    ]
