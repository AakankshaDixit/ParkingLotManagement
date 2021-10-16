from enum import Enum
from django.utils.translation import ugettext_lazy as _


class Vehicle_type(Enum):
    Two_Wheeler = 'Two Wheeler'
    Four_Wheeler= 'Four Wheeler'

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return (
            (str(cls.Two_Wheeler), _('Two Wheeler')),
            (str(cls.Four_Wheeler), _('Four Wheeler')),
        )


class PriceType(Enum):
    Fixed = 'Fixed'
    Variable = 'Variable'

    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return (
            (str(cls.Fixed), _('Fixed')),
            (str(cls.Variable), _('Variable')),
        )