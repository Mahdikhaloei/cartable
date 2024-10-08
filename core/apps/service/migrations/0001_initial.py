# Generated by Django 5.1 on 2024-09-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(db_index=True, default=0, verbose_name='order')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Service Step',
                'verbose_name_plural': 'Service Steps',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ServiceStepValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/step_values', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Service Step Value',
                'verbose_name_plural': 'Service Step Values',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(db_index=True, default=0, verbose_name='order')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('excerpt', models.CharField(blank=True, max_length=255, null=True, verbose_name='excerpt')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='image')),
                ('steps', models.ManyToManyField(blank=True, related_name='services', to='service.servicestep', verbose_name='steps')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='servicestep',
            name='values',
            field=models.ManyToManyField(blank=True, related_name='steps', to='service.servicestepvalue', verbose_name='values'),
        ),
    ]
