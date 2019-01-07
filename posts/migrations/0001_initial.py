# Generated by Django 2.1.4 on 2019-01-02 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=10)),
                ('post_id', models.CharField(max_length=200)),
                ('post_title', models.TextField(help_text='Contents of the post')),
                ('user_id', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=100)),
                ('comment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.TextField(blank=True, help_text='Comment for this post', null=True)),
            ],
        ),
    ]