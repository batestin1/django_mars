                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: models.py                                                          #
                        #   created: 2022-03-19                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#

from django.db import models

from probes.models import Probes


class Instructions(models.Model):

    INSTRUCTIONS = [
        ('M', 'Move'),
        ('R', 'Right'),
        ('L', 'Left'),
    ]

    id_instruction = models.AutoField(primary_key=True, unique=True)
    instruction = models.CharField(
        choices=INSTRUCTIONS, max_length=1, blank=False, null=False)
    id_probe = models.ForeignKey(
        Probes, related_name='instructions', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'instructions'
