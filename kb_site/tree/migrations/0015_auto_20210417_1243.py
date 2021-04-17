# Generated by Django 3.1.7 on 2021-04-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0014_updatesecurity_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antivirus_about', models.TextField()),
                ('antivirus_issues', models.TextField()),
                ('bitlocker_about', models.TextField()),
                ('bitlocker_yes', models.TextField()),
                ('bitlocker_no', models.TextField()),
                ('fu_about', models.TextField()),
                ('fu_errors', models.TextField()),
                ('wu_about', models.TextField()),
                ('wu_errors', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Apps',
        ),
        migrations.DeleteModel(
            name='Devices',
        ),
        migrations.DeleteModel(
            name='NetworkInternet',
        ),
        migrations.DeleteModel(
            name='System',
        ),
        migrations.DeleteModel(
            name='TCN',
        ),
        migrations.DeleteModel(
            name='UpdateSecurity',
        ),
    ]