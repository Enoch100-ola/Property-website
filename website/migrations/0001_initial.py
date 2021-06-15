# Generated by Django 3.1.1 on 2021-06-15 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=150)),
                ('profile', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('property_img1', models.ImageField(blank=True, null=True, upload_to='uploads/properties', verbose_name='Property Image 1')),
                ('property_img2', models.ImageField(blank=True, null=True, upload_to='uploads/properties', verbose_name='Property Image 2')),
                ('property_img3', models.ImageField(blank=True, null=True, upload_to='uploads/properties', verbose_name='Property Image 3')),
                ('prize', models.DecimalField(decimal_places=2, max_digits=9)),
                ('property_address', models.TextField(blank=True, null=True)),
                ('property_description', models.TextField(blank=True, null=True)),
                ('rooms', models.PositiveIntegerField()),
                ('offer_type', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale'), ('', 'Choose An Offer Type')], default='', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('approve', models.BooleanField(default=False)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_agent', to=settings.AUTH_USER_MODEL)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_location', to='website.location')),
                ('property_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_type', to='website.propertytype')),
            ],
            options={
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='MoreProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17)),
                ('website', models.URLField(blank=True, null=True)),
                ('profile', models.FileField(blank=True, null=True, upload_to='uploads/profile')),
                ('biography', models.TextField()),
                ('address', models.TextField()),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Agent')),
            ],
            options={
                'verbose_name_plural': 'More Profile',
            },
        ),
        migrations.CreateModel(
            name='ContactAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.location')),
            ],
        ),
    ]
