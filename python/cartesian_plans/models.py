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


class CartesianPlans(models.Model):
    id_cartesian_plan = models.AutoField(primary_key=True, unique=True)
    axis_x = models.IntegerField(blank=False, null=False)
    axis_y = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'cartesian_plans'
