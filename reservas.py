from datetime import datetime

from entidades import Cliente
from servicios import Servicio

from excepciones import ReservaError
from logger import logger



# CLASE RESERVA


class Reserva:

    def __init__(self, cliente, servicio, horas):

        if not isinstance(cliente, Cliente):

            raise ReservaError(
                "Cliente no válido"
            )

        if not isinstance(servicio, Servicio):

            raise ReservaError(
                "Servicio no válido"
            )

        if horas <= 0:

            raise ReservaError(
                "Las horas deben ser mayores a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def confirmar_reserva(self):

        try:

            costo = self.servicio.calcular_costo(
                self.horas
            )

        except Exception as error:

            raise ReservaError(
                "No fue posible confirmar la reserva"
            ) from error

        else:

            self.estado = "Confirmada"

            logger.info(
                f"Reserva confirmada para "
                f"{self.cliente.nombre}"
            )

            return costo

        finally:

            logger.info(
                "Proceso de confirmación ejecutado"
            )

    def cancelar_reserva(self):

        self.estado = "Cancelada"

        logger.warning(
            f"Reserva cancelada por "
            f"{self.cliente.nombre}"
        )

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )