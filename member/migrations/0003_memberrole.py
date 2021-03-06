# Generated by Django 4.0.3 on 2022-03-18 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'member',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='member.member'
                    ),
                ),
                (
                    'role',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='member.role'
                    ),
                ),
            ],
        ),
    ]
