from typing import Any, Dict
import json
from stdnum.ar import dni
from stdnum.ar import cuit


class CUIT(str):
    @classmethod
    def __modify_schema__(cls, field_schema: dict[str, Any]) -> None:
        field_schema.update(type='string', format='cuit')

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_cuit

    @classmethod
    def validate_cuit(cls, cuit_: str) -> str:
        try:
            cuit.validate(cuit_)
        except (cuit.InvalidComponent, cuit.InvalidFormat, cuit.InvalidLength, cuit.InvalidChecksum) as e:
            raise ValueError(e)
        return cuit.format(cuit_)


class DNI(int):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_dni

    @classmethod
    def validate_dni(cls, dni_: int) -> int:
        try:
            dni.validate(str(dni_))
        except (dni.InvalidComponent, dni.InvalidFormat, dni.InvalidLength, dni.InvalidChecksum) as e:
            raise ValueError(e)
        return int(dni_)
