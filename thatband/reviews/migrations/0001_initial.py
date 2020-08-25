# Generated by Django 3.1 on 2020-08-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=120, unique=True)),
                ('rating', models.CharField(choices=[('SUX', 'Sux'), ('MEH', 'Meh'), ('OK', 'Ok'), ('GOOD', 'Good'), ('GREAT', 'Great')], max_length=5)),
                ('genre', models.CharField(choices=[('THRASH', 'Thrash Metal'), ('BLACK', 'Black Metal'), ('DEATH', 'Death Metal'), ('INDUSTRIAL', 'Industrial Metal'), ('DOOM', 'Doom Metal'), ('PROGRESSIVE', 'Progressive Metal'), ('INSTRUMETAL', 'Instrumental Metal'), ('AMBIENT', 'Ambient'), ('ELECTRONIC', 'Electronic')], max_length=11)),
                ('description', models.TextField()),
                ('sounds_like', models.CharField(max_length=120)),
            ],
        ),
    ]