from entidades import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reservas import Reserva
from gestor import SistemaGestion

from excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)

from logger import logger


# CREACIÓN DEL SISTEMA


sistema = SistemaGestion()

print(
    "\nSIMULACIONES "
    "DEL SISTEMA "
)


# 1. CLIENTE VÁLIDO


try:

    cliente1 = Cliente(
        "Juan Pérez",
        "1010",
        "juan@gmail.com"
    )

    sistema.agregar_cliente(cliente1)

except Exception as error:

    logger.error(error)

# ======================================================
# 2. CLIENTE INVÁLIDO
# ======================================================

try:

    cliente2 = Cliente(
        "Ana Torres",
        "2020",
        "correo_invalido"
    )

    sistema.agregar_cliente(cliente2)

except ClienteError as error:

    logger.error(error)

    print(f"Error detectado: {error}")


# 3. SERVICIO VÁLIDO


try:

    sala = ReservaSala(
        "Sala de juntas",
        50
    )

    print(sala.descripcion())

except ServicioError as error:

    logger.error(error)


# 4. SERVICIO INVÁLIDO


try:

    servicio_invalido = ReservaSala(
        "Sala inválida",
        -10
    )

except ServicioError as error:

    logger.error(error)

    print(f"Error detectado: {error}")


# 5. RESERVA EXITOSA


try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    sistema.crear_reserva(reserva1)

except Exception as error:

    logger.error(error)


# 6. RESERVA INVÁLIDA


try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -5
    )

    sistema.crear_reserva(reserva2)

except ReservaError as error:

    logger.error(error)

    print(f"Error detectado: {error}")


# 7. ALQUILER DE EQUIPOS


try:

    equipo = AlquilerEquipo(
        "Portátil Gamer",
        80
    )

    reserva3 = Reserva(
        cliente1,
        equipo,
        2
    )

    sistema.crear_reserva(reserva3)

except Exception as error:

    logger.error(error)


# 8. ASESORÍA ESPECIALIZADA


try:

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        120
    )

    reserva4 = Reserva(
        cliente1,
        asesoria,
        4
    )

    sistema.crear_reserva(reserva4)

except Exception as error:

    logger.error(error)


# 9. CANCELACIÓN DE RESERVA


try:

    reserva4.cancelar_reserva()

    print(
        "Reserva cancelada correctamente"
    )

except Exception as error:

    logger.error(error)


# 10. CLIENTE INVÁLIDO EN RESERVA


try:

    reserva5 = Reserva(
        "cliente falso",
        sala,
        2
    )

except ReservaError as error:

    logger.error(error)

    print(f"Error detectado: {error}")


# 11. SERVICIO INVÁLIDO EN RESERVA


try:

    reserva6 = Reserva(
        cliente1,
        "servicio falso",
        2
    )

except ReservaError as error:

    logger.error(error)

    print(f"Error detectado: {error}")


# POLIMORFISMO


servicios = [
    sala,
    equipo,
    asesoria
]

print(
    "\nPOLIMORFISMO "
)

for servicio in servicios:

    try:

        print(servicio.descripcion())

        costo = servicio.calcular_costo(
            2,
            descuento=0.10
        )

        print(
            f"Costo calculado: ${costo}\n"
        )

    except Exception as error:

        logger.error(error)


# MOSTRAR RESERVAS


print(
    "\nRESERVAS "
    "REGISTRADAS "
)

for reserva in sistema.reservas:

    print(
        reserva.mostrar_reserva()
    )

print(
    "\nSistema ejecutado correctamente"
)

print(
    "Revisar archivo sistema_fj.log"
)