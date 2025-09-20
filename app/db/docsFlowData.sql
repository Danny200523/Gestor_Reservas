INSERT INTO
  Salas (nombre, sede, capacidad, recursos)
VALUES
  (
    'Sala Principal',
    'Bucaramanga',
    120,
    'Proyector, Sonido, Pizarra digital'
  ),
  (
    'Sala Ejecutiva',
    'Medellin',
    50,
    'Televisor 65", Videoconferencia, WiFi'
  ),
  (
    'Aula de Capacitacion',
    'Bogota',
    70,
    'Pizarra blanca, Proyector, Escritorios en U'
  ),
  (
    'Laboratorio de Informatica',
    'valledupar',
    80,
    'PCs de escritorio, Software especializado, WiFi'
  ),
  (
    'Sala de Innovacion',
    'cali',
    150,
    'Pizarras acrilicas, Pantalla LED, Sillas ergonomicas'
  );


INSERT INTO Reservas (id_usuario, id_sala, fecha, hora_inicio, hora_fin, estado)
VALUES
(270001, 1, '2025-09-21', '09:00:00', '10:00:00', 'Confirmado'),
(270002, 2, '2025-09-21', '11:00:00', '12:00:00', 'Pendiente'),
(270003, 3, '2025-09-22', '14:00:00', '15:00:00', 'Confirmado'),
(270004, 4, '2025-09-22', '16:00:00', '17:00:00', 'Pendiente'),
(270005, 5, '2025-09-23', '08:00:00', '09:00:00', 'Confirmado');