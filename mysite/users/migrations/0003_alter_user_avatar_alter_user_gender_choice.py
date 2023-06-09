# Generated by Django 4.1.2 on 2023-03-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_avatar_user_citizen_identification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(default=None, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender_choice',
            field=models.CharField(choices=[('MN', 'Men'), ('WM', 'Phu nu'), ('TH', 'Khong xac dinh')], default='TH', max_length=2),
        ),
    ]
