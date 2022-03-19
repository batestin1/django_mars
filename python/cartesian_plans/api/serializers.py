                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: serializers.py                                                     #
                        #   created: 2022-03-19                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#


# django library

# third library
from rest_framework import serializers

# my library
from cartesian_plans import models


class CartesianPlansSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartesianPlans
        fields = '__all__'
