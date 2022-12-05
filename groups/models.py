from django.db import models


class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    pets = models.ForeignKey(
        "pets.Pet", on_delete=models.CASCADE, related_name="Groups"
    )


def __repr__(self) -> str:
    return f"<Group [{self.id}] - [{self.scientific_name} [{self.created_at}>"
