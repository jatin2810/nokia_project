# Generated by Django 3.1.3 on 2020-11-28 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=300)),
                ('small', models.BooleanField(default=False)),
                ('medium', models.BooleanField(default=True)),
                ('large', models.BooleanField(default=False)),
                ('extralarge', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSizeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcolor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productsize')),
            ],
        ),
    ]