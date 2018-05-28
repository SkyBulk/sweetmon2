# Generated by Django 2.0.5 on 2018-05-28 15:23

import api.models
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_crash_parent_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnetimeUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=api.models.generate_api_key, max_length=256)),
                ('file', models.FileField(upload_to='')),
                ('is_expired', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='crash',
            name='crash_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/Users/sweetchip/PycharmProjects/sweetmon2/file/crash/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='fuzzer',
            name='crash_cnt',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
