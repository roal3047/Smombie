# Generated by Django 3.0.5 on 2020-05-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='smombie',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('pcode', models.CharField(max_length=4)),
                ('user_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('is_complete', models.BooleanField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'smombie',
                'managed': False,
            },
        ),
    ]