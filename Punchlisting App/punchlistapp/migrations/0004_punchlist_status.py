# Generated by Django 5.0.6 on 2024-06-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchlistapp', '0003_alter_punchlist_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='punchlist',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
