# Generated by Django 2.1.5 on 2019-01-12 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evalution',
            fields=[
                ('evalID', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this evaluation.', primary_key=True, serialize=False)),
                ('grade', models.IntegerField(help_text='Enter a food price:')),
                ('evalDate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodFeat', models.CharField(help_text='Enter a food feature name:', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matName', models.CharField(help_text='Enter a food material name:', max_length=200)),
                ('matFrom', models.CharField(help_text='Enter a food material source:', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WayToCook', models.CharField(help_text='Enter how a food was cooked:', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this order.', primary_key=True, serialize=False)),
                ('orderDate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(help_text='Enter a food price:'),
        ),
        migrations.AddField(
            model_name='order',
            name='foodID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Food'),
        ),
        migrations.AddField(
            model_name='order',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='make',
            name='foodID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Food'),
        ),
        migrations.AddField(
            model_name='make',
            name='matID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.FoodMaterial'),
        ),
        migrations.AddField(
            model_name='foodfeature',
            name='foodID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Food'),
        ),
        migrations.AddField(
            model_name='evalution',
            name='foodID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Food'),
        ),
        migrations.AddField(
            model_name='evalution',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]