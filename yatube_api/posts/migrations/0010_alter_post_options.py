# Generated by Django 3.2.16 on 2023-04-24 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20230424_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
