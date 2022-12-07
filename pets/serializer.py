from rest_framework import serializers
from pets.models import Pet, SexChoice
from groups.serializer import GroupSerializer
from traits.serializer import TraitSerializer
from traits.models import Trait
from groups.models import Group


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexChoice.choices, default=SexChoice.NOT_INFORMED
    )
    created_at = serializers.DateTimeField(read_only=True)
    traits_count = serializers.SerializerMethodField()

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def get_traits_count(self, target_pet: Pet):
        trait_list = Pet.objects.get(id=target_pet.id).traits.all()

        result = len(trait_list)

        return result

    def create(self, validated_data: dict) -> Pet:
        traits_list = validated_data.pop("traits")
        group_objct = validated_data.pop("group")

        group_dict = Group.objects.get_or_create(**group_objct)[0]

        pet_object = Pet.objects.create(**validated_data, group=group_dict)
        print(pet_object)

        for trait_dict in traits_list:
            trait_object = Trait.objects.get_or_create(**trait_dict)[0]
            pet_object.traits.add(trait_object)

            pet_object.save()

        return pet_object

    def update(self, instance, validated_data: dict):
        traits_list = validated_data.pop("traits", None)
        group_dict = validated_data.pop("group", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if group_dict:
            group_object = Group.objects.get_or_create(pets=instance)
            for key, value in group_dict.items():
                setattr(group_object, key, value)
            group_object.save()

        new_traints = []

        if traits_list:
            for trait_dict in traits_list:
                trait = Trait.objects.get_or_create(**trait_dict)
                new_traints.append(trait)

            instance.traits.set(new_traints)

        instance.save()

        return instance