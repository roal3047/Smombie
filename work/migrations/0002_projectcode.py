# Generated by Django 3.0.5 on 2020-05-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCode',
            fields=[
                ('pcode', models.CharField(db_column='PCODE', max_length=4, primary_key=True, serialize=False)),
                ('pname', models.CharField(db_column='PNAME', max_length=100)),
            ],
            options={
                'db_table': 'project_code',
                'managed': False,
            },
        ),
    ]
