from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    pets = models.ManyToManyField("pets.Pet", related_name="Traits")

def __repr__(self) -> str:
    return f"<Trait [{self.id}] - [{self.name}>"