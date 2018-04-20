# Generated by Django 2.0.4 on 2018-04-19 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='paid_boolean',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.Product'),
            preserve_default=False,
        ),
    ]