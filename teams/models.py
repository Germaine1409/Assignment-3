from django.db import models
from dataclasses import dataclass

# Create your models here.
@dataclass
class Team:
    name:str
    description:str
    members: list[str]