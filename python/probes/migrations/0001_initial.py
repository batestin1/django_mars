                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: 0001_initial.py                                                    #
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

    initial = True

    dependencies = [
        ('cartesian_plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Probes',
            fields=[
                ('id_probe', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('init_x', models.IntegerField()),
                ('init_y', models.IntegerField()),
                ('direction', models.CharField(choices=[('N', 'North'), ('S', 'Soulth'), ('W', 'West'), ('E', 'East')], max_length=1)),
                ('id_cartesian_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartesian_plans.CartesianPlans')),
            ],
            options={
                'db_table': 'probes',
                'managed': True,
            },
        ),
    ]
