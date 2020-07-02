# Generated by Django 2.0.1 on 2019-12-26 05:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0004_course_content_db_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_course_category_db',
            name='image',
            field=models.FileField(default=datetime.datetime(2019, 12, 26, 5, 44, 55, 490678, tzinfo=utc), upload_to='category_image'),
            preserve_default=False,
        ),
    ]
