from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        superuser = User.objects.create_superuser(
            username='iscs',
            email='mikaela.tan@obf.ateneo.edu',
            password='admin12345')

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
