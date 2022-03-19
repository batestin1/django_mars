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
        ('probes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id_instruction', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('instruct', models.CharField(choices=[('M', 'Move'), ('R', 'Right'), ('L', 'Left')], max_length=1)),
                ('id_probe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probes.Probes')),
            ],
            options={
                'db_table': 'instructions',
                'managed': True,
            },
        ),
    ]
