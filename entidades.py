from abc import ABC, abstractmethod
from excepciones import ClienteError



# CLASE ABSTRACTA PERSONA

class Persona(ABC):

    def __init__(self, nombre, identificacion):

        self.nombre = nombre
        self.identificacion = identificacion

    @abstractmethod
    def mostrar_datos(self):
        pass



# CLASE CLIENTE


class Cliente(Persona):

    def __init__(self, nombre, identificacion, correo):

        super().__init__(nombre, identificacion)

        self.__correo = None
        self.correo = correo

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if "@" not in valor:

            raise ClienteError(
                "Correo electrónico inválido"
            )

        self.__correo = valor

    def mostrar_datos(self):

        return (
            f"Cliente: {self.nombre} "
            f"- ID: {self.identificacion}"
        )