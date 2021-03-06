# Generated by Django 2.0 on 2018-05-30 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookclubapp', '0003_auto_20180530_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='books',
            field=models.ManyToManyField(null=True, to='bookclubapp.Books'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookclubapp.Comment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookclubapp.Review'),
        ),
    ]
