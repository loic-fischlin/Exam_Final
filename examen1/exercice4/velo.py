from dataclasses import dataclass


@dataclass
class Velo:
    _marque:str

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, value):
        self._marque=value

    def __str__(self):
        return f"Vélo traditionnel de marque {self._marque}"

@dataclass
class VeloElectrique(Velo):
    __type_assistance:str

    def __str__(self):
        return f"Vélo électrique de marque {self._marque} assistance {self.__type_assistance}"

    @property
    def type_assistance(self):
        return self.__type_assistance

    @type_assistance.setter
    def type_assistance(self, value):
        self.__type_assistance = value



