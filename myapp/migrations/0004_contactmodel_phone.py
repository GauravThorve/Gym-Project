from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_massagebookingmodel_massage_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]