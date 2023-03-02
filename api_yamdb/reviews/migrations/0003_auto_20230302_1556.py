# Generated by Django 2.2.16 on 2023-03-02 12:56

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221122_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True, validators=[reviews.validators.validate_year]),
        ),
    ]