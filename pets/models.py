from django.db import models


class SexChoice(models.TextChoices):
    MALE = "Macho"
    FEMALE = "Fêmea"
    NOT_INFORMED = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=SexChoice.choices, default=SexChoice.NOT_INFORMED
    )


    traits = models.ManyToManyField("traits.Trait", related_name="Pets", default=None)

def __repr__(self) -> str:
    return f"<Pet [{self.id}] - [{self.name} [{self.age} [{self.weight} [{self.sex}>"
