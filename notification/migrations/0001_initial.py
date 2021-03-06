# Generated by Django 3.2.7 on 2021-10-02 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_seen', models.BooleanField(default=False)),
                ('tagged_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_user', to=settings.AUTH_USER_MODEL)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet', to='tweet.tweet')),
                ('user_who_tagged_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_tagged_me', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
