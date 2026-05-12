from abc import ABC, abstractmethod
from datetime import datetime
import logging

# CONFIGURACIÓN DEL SISTEMA DE LOGS


logging.basicConfig(
    filename="sistema_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# EXCEPCIONES PERSONALIZADAS


class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


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
            raise ClienteError("Correo electrónico inválido")

        self.__correo = valor

    def mostrar_datos(self):
        return f"Cliente: {self.nombre} - ID: {self.identificacion}"



# CLASE ABSTRACTA SERVICIO


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        if tarifa_base <= 0:
            raise ServicioError("La tarifa debe ser mayor a cero")

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass



# SERVICIO: RESERVA DE SALAS


class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero")

        costo = self.tarifa_base * horas
        costo -= costo * descuento

        return costo

    def descripcion(self):
        return "Servicio de reserva de salas empresariales"



# SERVICIO: ALQUILER DE EQUIPOS


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        seguro = 20

        costo = (self.tarifa_base * horas) + seguro
        costo -= costo * descuento

        return costo

    def descripcion(self):
        return "Servicio de alquiler de equipos tecnológicos"


# SERVICIO: ASESORÍA ESPECIALIZADA

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Cantidad de horas inválida")

        iva = 0.19

        subtotal = self.tarifa_base * horas
        total = subtotal + (subtotal * iva)
        total -= total * descuento

        return total

    def descripcion(self):
        return "Servicio de asesoría especializada"


# CLASE RESERVA


class Reserva:

    def __init__(self, cliente, servicio, horas):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente no válido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio no válido")

        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def confirmar_reserva(self):

        try:
            costo = self.servicio.calcular_costo(self.horas)

        except Exception as error:
            raise ReservaError("No fue posible confirmar la reserva") from error

        else:
            self.estado = "Confirmada"

            logging.info(
                f"Reserva confirmada para {self.cliente.nombre}"
            )

            return costo

        finally:
            logging.info("Proceso de confirmación ejecutado")

    def cancelar_reserva(self):

        self.estado = "Cancelada"

        logging.warning(
            f"Reserva cancelada por {self.cliente.nombre}"
        )

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )



# CLASE SISTEMA


class SistemaGestion:

    def __init__(self):
        self.clientes = []
        self.reservas = []

    def agregar_cliente(self, cliente):

        try:

            if not isinstance(cliente, Cliente):
                raise ClienteError("Objeto cliente inválido")

            self.clientes.append(cliente)

            logging.info(f"Cliente agregado: {cliente.nombre}")

            print(f"Cliente registrado: {cliente.nombre}")

        except ClienteError as error:

            logging.error(error)
            print(f"Error: {error}")

    def crear_reserva(self, reserva):

        try:

            costo = reserva.confirmar_reserva()

            self.reservas.append(reserva)

            print("Reserva realizada correctamente")
            print(f"Costo total: ${costo}")

        except ReservaError as error:

            logging.error(error)
            print(f"Error en la reserva: {error}")


# SIMULACIONES DEL SISTEMA

sistema = SistemaGestion()

print("\n========== SIMULACIONES DEL SISTEMA ==========")


# 1. CLIENTE VÁLIDO

try:
    cliente1 = Cliente("Juan Pérez", "1010", "juan@gmail.com")
    sistema.agregar_cliente(cliente1)

except Exception as error:
    logging.error(error)


# 2. CLIENTE CON CORREO INVÁLIDO

try:
    cliente2 = Cliente("Ana Torres", "2020", "correo_invalido")
    sistema.agregar_cliente(cliente2)

except ClienteError as error:

    logging.error(error)
    print(f"Error detectado: {error}")


# 3. SERVICIO VÁLIDO

try:
    sala = ReservaSala("Sala de juntas", 50)
    print(sala.descripcion())

except ServicioError as error:
    logging.error(error)



# 4. SERVICIO CON TARIFA INVÁLIDA

try:
    servicio_invalido = ReservaSala("Sala inválida", -10)

except ServicioError as error:

    logging.error(error)
    print(f"Error detectado: {error}")



# 5. RESERVA EXITOSA


try:

    reserva1 = Reserva(cliente1, sala, 3)
    sistema.crear_reserva(reserva1)

except Exception as error:
    logging.error(error)



# 6. RESERVA CON HORAS INVÁLIDAS


try:

    reserva2 = Reserva(cliente1, sala, -5)
    sistema.crear_reserva(reserva2)

except ReservaError as error:

    logging.error(error)
    print(f"Error detectado: {error}")



# 7. SERVICIO DE ALQUILER


try:

    equipo = AlquilerEquipo("Portátil Gamer", 80)

    reserva3 = Reserva(cliente1, equipo, 2)

    sistema.crear_reserva(reserva3)

except Exception as error:
    logging.error(error)



# 8. SERVICIO DE ASESORÍA


try:

    asesoria = AsesoriaEspecializada("Asesoría Python", 120)

    reserva4 = Reserva(cliente1, asesoria, 4)

    sistema.crear_reserva(reserva4)

except Exception as error:
    logging.error(error)



# 9. CANCELACIÓN DE RESERVA


try:

    reserva4.cancelar_reserva()

    print("Reserva cancelada correctamente")

except Exception as error:
    logging.error(error)



# 10. RESERVA CON CLIENTE INVÁLIDO


try:

    reserva5 = Reserva("cliente falso", sala, 2)

except ReservaError as error:

    logging.error(error)
    print(f"Error detectado: {error}")




# 11. RESERVA CON SERVICIO INVÁLIDO


try:

    reserva6 = Reserva(cliente1, "servicio falso", 2)

except ReservaError as error:

    logging.error(error)
    print(f"Error detectado: {error}")



# 12. POLIMORFISMO


servicios = [sala, equipo, asesoria]

print("\n========== POLIMORFISMO ==========")

for servicio in servicios:

    try:

        print(servicio.descripcion())

        costo = servicio.calcular_costo(2, descuento=0.10)

        print(f"Costo calculado: ${costo}\n")

    except Exception as error:

        logging.error(error)



# MOSTRAR RESERVAS


print("\n RESERVAS REGISTRADAS ")

for reserva in sistema.reservas:
    print(reserva.mostrar_reserva())


print("\nSistema ejecutado correctamente")
print("Revisar archivo sistema_logs.txt para ver eventos y errores")


