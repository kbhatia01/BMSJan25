# Generated by Django 4.2.18 on 2025-01-24 15:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('row_number', models.IntegerField()),
                ('col_number', models.IntegerField()),
                ('number', models.CharField(max_length=50)),
                ('seat_type', models.TextField(choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('PLATINUM', 'Platinum')])),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.screen')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.feature')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.screen')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowSeat',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('show_seat_status', models.TextField(choices=[('AVAILABLE', 'Available'), ('MAINTENANCE', 'Maintenance'), ('RESERVED', 'Reserved'), ('LOCKED', 'Locked')])),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('booking_status', models.CharField(max_length=50)),
                ('booking_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.show')),
                ('show_seats', models.ManyToManyField(to='bookmyshow.showseat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowSeatType',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('seat_type', models.CharField(choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('PLATINUM', 'Platinum')], max_length=100)),
                ('price', models.IntegerField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.theatre'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ref_number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('mode', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
