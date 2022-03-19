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


class Migration(migrations.Migration):

    dependencies = [
        ('probes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probes',
            name='direction',
            field=models.CharField(choices=[('N', 'N'), ('S', 'S'), ('W', 'W'), ('E', 'E')], max_length=1),
        ),
    ]
