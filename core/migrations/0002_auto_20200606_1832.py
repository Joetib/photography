# Generated by Django 3.0.7 on 2020-06-06 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='hello', upload_to='media/category/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.Category'),
        ),
    ]
