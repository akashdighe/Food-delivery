# Generated by Django 4.0 on 2021-12-20 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menuitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.category')),
            ],
        ),
        migrations.CreateModel(
            name='ordernow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_creat', models.DateTimeField(verbose_name=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('item', models.ManyToManyField(blank=True, related_name='order', to='order.Menuitem')),
            ],
        ),
    ]
