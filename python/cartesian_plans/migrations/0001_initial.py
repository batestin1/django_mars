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


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartesianPlans',
            fields=[
                ('id_cartesian_plan', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('axis_x', models.IntegerField()),
                ('axis_y', models.IntegerField()),
            ],
            options={
                'db_table': 'cartesian_plans',
                'managed': True,
            },
        ),
    ]
