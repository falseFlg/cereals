from rest_framework import serializers

from main.enums import StepBlockStages, StepBlockType, StepMobileBlockType


class Step1Docs(serializers.Serializer):
    for_sign = serializers.CharField()
    specification = serializers.CharField()
    bill = serializers.CharField()
    created_at = serializers.DateField()


class StepBlock(serializers.Serializer):
    type = serializers.ChoiceField(choices=tuple(key.value for key in StepBlockType))
    datetime = serializers.DateTimeField(allow_null=True)
    value = serializers.CharField(allow_null=True)


class StepWeb(serializers.Serializer):
    stage = serializers.ChoiceField(choices=tuple(key.value for key in StepBlockStages))
    blocks = StepBlock(many=True)


class StepBlockMobile(StepBlock):
    type = serializers.ChoiceField(
        choices=tuple(key.value for key in StepMobileBlockType)
    )
    status = serializers.BooleanField()
    title = serializers.CharField()
