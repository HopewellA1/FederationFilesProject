# Generated by Django 4.1.2 on 2023-03-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheFiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='federation',
            name='yearUpdate',
            field=models.CharField(default='2023', max_length=4),
        ),
        migrations.AlterField(
            model_name='federation',
            name='superID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
