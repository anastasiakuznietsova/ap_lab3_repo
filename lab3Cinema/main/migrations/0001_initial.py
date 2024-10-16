# Generated by Django 5.1.2 on 2024-10-12 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRestrictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restriction', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'AgeRestrictions',
            },
        ),
        migrations.CreateModel(
            name='AnimationFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anima_format', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'AnimationFormat',
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'MovieGenre',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
            ],
            options={
                'db_table': 'Room',
            },
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
            ],
            options={
                'db_table': 'Viewer',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('mov_length', models.IntegerField()),
                ('premiere', models.DateField()),
                ('mvdescription', models.CharField(max_length=100)),
                ('ageRestrictionsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.agerestrictions')),
                ('animationFormatID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.animationformat')),
                ('movieGenreID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.moviegenre')),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_num', models.IntegerField()),
                ('isAvailable', models.BooleanField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
            ],
            options={
                'db_table': 'Seat',
            },
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('startsAt', models.TimeField()),
                ('endsAt', models.TimeField()),
                ('movieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
                ('roomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
            ],
            options={
                'db_table': 'Showtime',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showtimeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.showtime')),
                ('viewerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.viewer')),
            ],
            options={
                'db_table': 'Ticket',
            },
        ),
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seat')),
                ('ticketID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ticket')),
            ],
            options={
                'db_table': 'MovieSession',
            },
        ),
    ]
