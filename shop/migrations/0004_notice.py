# Generated by Django 3.2.5 on 2021-08-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_a_question_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_title', models.CharField(max_length=200)),
                ('n_text', models.TextField()),
                ('n_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]