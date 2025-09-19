CREATE database gestorReservas;

use gestorReservas;

-- ========================
-- Tabla Usuarios
-- ========================
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol INT NOT NULL
) ENGINE=InnoDB;

-- ========================
-- Tabla Salas
-- ========================
CREATE TABLE Salas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sede VARCHAR(100) NOT NULL,
    capacidad INT NOT NULL,
    recursos VARCHAR(255)
) ENGINE=InnoDB;

-- ========================
-- Tabla Reservas
-- ========================
CREATE TABLE Reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_sala INT NOT NULL,
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    estado ENUM ("Confirmado","Rechazado","Pendiente") DEFAULT 'Pendiente',
    -- Relaciones
    CONSTRAINT fk_reserva_usuario FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    CONSTRAINT fk_reserva_sala FOREIGN KEY (id_sala) REFERENCES Salas(id)
) ENGINE=InnoDB;
