# Generated by Django 4.1.7 on 2023-04-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('sno', models.IntegerField()),
                ('topic_name', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('player_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=30)),
                ('Email', models.EmailField(default='mm1437799@gmail.com', max_length=254)),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('Jersey_No', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=25)),
                ('player_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
