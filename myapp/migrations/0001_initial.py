# Generated by Django 3.1.2 on 2021-01-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='extract_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=50)),
                ('bill_amount', models.CharField(max_length=50)),
            ],
        ),
    ]
