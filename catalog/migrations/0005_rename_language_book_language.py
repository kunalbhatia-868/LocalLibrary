# Generated by Django 3.2.5 on 2021-08-02 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Language',
            new_name='language',
        ),
    ]
