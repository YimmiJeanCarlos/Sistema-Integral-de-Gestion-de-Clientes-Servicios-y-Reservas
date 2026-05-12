from entidades import Cliente
from excepciones import ClienteError, ReservaError
from logger import logger



# CLASE GESTOR DEL SISTEMA


class SistemaGestion:

    def __init__(self):

        self.clientes = []
        self.reservas = []

    def agregar_cliente(self, cliente):

        try:

            if not isinstance(cliente, Cliente):

                raise ClienteError(
                    "Objeto cliente inválido"
                )

            self.clientes.append(cliente)

            logger.info(
                f"Cliente agregado: "
                f"{cliente.nombre}"
            )

            print(
                f"Cliente registrado: "
                f"{cliente.nombre}"
            )

        except ClienteError as error:

            logger.error(error)

            print(f"Error: {error}")

    def crear_reserva(self, reserva):

        try:

            costo = reserva.confirmar_reserva()

            self.reservas.append(reserva)

            print(
                "Reserva realizada correctamente"
            )

            print(f"Costo total: ${costo}")

        except ReservaError as error:

            logger.error(error)

            print(
                f"Error en la reserva: "
                f"{error}"
            )