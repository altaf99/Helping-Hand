# Generated by Django 2.0.7 on 2018-09-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=250)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'Container'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='black', max_length=50)),
                ('mobile_no', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=250)),
                ('hospital', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
