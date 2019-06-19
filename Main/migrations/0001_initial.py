# Generated by Django 2.2.2 on 2019-06-20 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookNounIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=20)),
                ('context', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '专名索引表',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50, null=True)),
                ('translator', models.CharField(max_length=50, null=True)),
                ('ISBN', models.CharField(max_length=20, null=True)),
                ('edition', models.CharField(max_length=10, null=True)),
                ('publication_date', models.CharField(max_length=6, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '书籍表',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '专名范畴表',
            },
        ),
        migrations.CreateModel(
            name='UserClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_class_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': '用户类型表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('birthday', models.DateField(null=True)),
                ('e_mail', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('identify_code', models.CharField(max_length=20, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user_class',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.UserClass')),
            ],
            options={
                'verbose_name_plural': '用户信息表',
            },
        ),
        migrations.CreateModel(
            name='ProperNoun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Noun', models.CharField(max_length=30, null=True)),
                ('classes', models.CharField(max_length=30, null=True)),
                ('properties', models.CharField(max_length=60, null=True)),
                ('relation', models.CharField(max_length=60, null=True)),
                ('comment', models.CharField(max_length=60, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('book', models.ManyToManyField(max_length=30, through='Main.BookNounIndex', to='Main.Books')),
                ('category',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.Category')),
            ],
            options={
                'verbose_name_plural': '专名表',
            },
        ),
        migrations.AddField(
            model_name='booknounindex',
            name='Noun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.ProperNoun'),
        ),
        migrations.AddField(
            model_name='booknounindex',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Books'),
        ),
    ]
