                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: 0002_auto_20200730_0005.py                                         #
                        #   created: 2022-03-19                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('probes', '0002_auto_20200730_0005'),
        ('instructions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructions',
            old_name='instruct',
            new_name='instruction',
        ),
        migrations.AlterField(
            model_name='instructions',
            name='id_probe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='probes.Probes'),
        ),
    ]
