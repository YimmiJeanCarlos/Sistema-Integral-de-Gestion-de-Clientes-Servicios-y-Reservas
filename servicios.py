from abc import ABC, abstractmethod
from excepciones import ServicioError



# CLASE ABSTRACTA SERVICIO

class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        if tarifa_base <= 0:

            raise ServicioError(
                "La tarifa debe ser mayor a cero"
            )

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

# RESERVA DE SALAS


class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:

            raise ServicioError(
                "Las horas deben ser mayores a cero"
            )

        costo = self.tarifa_base * horas

        costo -= costo * descuento

        return costo

    def descripcion(self):

        return (
            "Servicio de reserva "
            "de salas empresariales"
        )



# ALQUILER DE EQUIPOS


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:

            raise ServicioError("Horas inválidas")

        seguro = 20

        costo = (
            self.tarifa_base * horas
        ) + seguro

        costo -= costo * descuento

        return costo

    def descripcion(self):

        return (
            "Servicio de alquiler "
            "de equipos tecnológicos"
        )



# ASESORÍA ESPECIALIZADA


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:

            raise ServicioError(
                "Cantidad de horas inválida"
            )

        iva = 0.19

        subtotal = self.tarifa_base * horas

        total = subtotal + (subtotal * iva)

        total -= total * descuento

        return total

    def descripcion(self):

        return (
            "Servicio de asesoría especializada"
        )