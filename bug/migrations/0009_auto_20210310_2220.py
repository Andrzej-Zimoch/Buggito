# Generated by Django 2.2.3 on 2021-03-10 21:20

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0008_auto_20210310_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='assignee',
            new_name='assigned_team',
        ),
        migrations.AddField(
            model_name='ticket',
            name='assigned_member',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='assigned_team', chained_model_field='assigned_team', default=None, on_delete=django.db.models.deletion.CASCADE, to='bug.Profile'),
        ),
    ]
