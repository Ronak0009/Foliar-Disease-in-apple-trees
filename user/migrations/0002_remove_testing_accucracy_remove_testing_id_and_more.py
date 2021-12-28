# Generated by Django 4.0 on 2021-12-11 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testing',
            name='accucracy',
        ),
        migrations.RemoveField(
            model_name='testing',
            name='id',
        ),
        migrations.RemoveField(
            model_name='testing',
            name='result',
        ),
        migrations.AddField(
            model_name='testing',
            name='test_id',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='TestId'),
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(default='', max_length=100, verbose_name='Result')),
                ('accuracy', models.CharField(default='', max_length=20, verbose_name='Accuracy')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.testing')),
            ],
        ),
    ]