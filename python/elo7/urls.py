                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: urls.py                                                            #
                        #   created: 2022-03-19                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#

# django library
from django.contrib import admin
from django.urls import path, include

# third library
from rest_framework import routers

# my libraries
from cartesian_plans.api import viewsets as cartesian_plansviewsets
from instructions.api import viewsets as instructionsviewsets
from probes.api import viewsets as probesviewsets

router = routers.DefaultRouter()

router.register(
    r'cartesian_plan', cartesian_plansviewsets.CartesianPlansViewSet, basename='Cartesian_Plan')
router.register(r'instructions',
                instructionsviewsets.InstructionsViewSet, basename='Instructions')
router.register(r'probes', probesviewsets.ProbesViewSet,
                basename='Probes')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
