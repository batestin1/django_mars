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
from probes import models
from instructions.models import Instructions
from cartesian_plans.models import CartesianPlans
from instructions.api.serializers import InstructionsSerializer
from cartesian_plans.api.serializers import CartesianPlansSerializer


class ProbesSerializer(serializers.ModelSerializer):
    instructions = InstructionsSerializer(many=True, read_only=True)
    # cartesian_plan = CartesianPlansSerializer(read_only=True)
    local = serializers.SerializerMethodField()

    class Meta:
        model = models.Probes
        fields = [
            'id_probe',
            'init_x',
            'init_y',
            'direction',
            'instructions',
            'id_cartesian_plan',
            'local'
        ]

    def get_local(self, obj):
        local = {}

        wind_rose = ['N', 'E', 'S', 'W']

        x = obj.init_x
        y = obj.init_y
        direction = obj.direction

        id_cartesian_plan = obj.id_cartesian_plan.id_cartesian_plan
        cartesian_plan = CartesianPlans.objects.filter(
            id_cartesian_plan=id_cartesian_plan)[0]

        def move(instruction, direction, x, y):
            if instruction == 'R':
                index_direction = wind_rose.index(direction) + 1
                if index_direction == 4:
                    index_direction = 0
                direction = wind_rose[index_direction]

            if instruction == 'L':
                index_direction = wind_rose.index(direction) - 1
                if index_direction == -1:
                    index_direction = 3
                direction = wind_rose[index_direction]

            if not int(y) >= int(cartesian_plan.axis_y):
                if instruction == 'M' and direction == 'N':
                    y += 1

            if not int(x) >= int(cartesian_plan.axis_x):
                if instruction == 'M' and direction == 'E':
                    x += 1

            if not int(y) <= 0:
                if instruction == 'M' and direction == 'S':
                    y -= 1

            if not int(x) <= 0:
                if instruction == 'M' and direction == 'W':
                    x -= 1

            return x, y, direction

        for instruction in Instructions.objects.filter(id_probe=obj.id_probe):
            x, y, direction = move(instruction.instruction, direction, x, y)

        local = {
            'x': x,
            'y': y,
            'direction': direction
        }

        return local
