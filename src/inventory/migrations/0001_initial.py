# Generated by Django 3.1.4 on 2021-07-31 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Available', 'Item is Stock'), ('In_Production', 'Being used in Production'), ('Restocking', 'Item is being shipped')], default='Available', max_length=50)),
                ('issues', models.CharField(choices=[('No_Issues', 'Product is fine'), ('Bad', 'Quality of the Product is not good'), ('Good', 'Product is good')], default='No_Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Available', 'Item is Stock'), ('In_Production', 'Being used in Production'), ('Restocking', 'Item is being shipped')], default='Available', max_length=50)),
                ('issues', models.CharField(choices=[('No_Issues', 'Product is fine'), ('Bad', 'Quality of the Product is not good'), ('Good', 'Product is good')], default='No_Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Available', 'Item is Stock'), ('In_Production', 'Being used in Production'), ('Restocking', 'Item is being shipped')], default='Available', max_length=50)),
                ('issues', models.CharField(choices=[('No_Issues', 'Product is fine'), ('Bad', 'Quality of the Product is not good'), ('Good', 'Product is good')], default='No_Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
