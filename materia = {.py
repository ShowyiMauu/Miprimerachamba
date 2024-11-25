materia = {
    "nombre": "Programación",
    "codigo": "INFO2",
    "profesor": "Mari García",
    "horarios": ["Lunes 9:00-11:00", "Miércoles 9:00-11:00"],
    "creditos": 8,
    "nivel": "Intermedio",
    "prerequisitos": ["Computación 1"],
    "prerequisitos": ["Computación 1"],
}

print(materia ["profesor"])
alumno = {
    "nombre": "Mauricio Antonio Gastelum Reyes",
    "matricula": "A123456789",
    "edad": 17,
    "semestre": "quinto",
    "calificaciones": {
        "Matemáticas": 10,
        "Física": 8.0,
        "Programación": 10,
        "Química": 9.0
    },
    "direccion": {
        "calle": "abasolo 206",
        "ciudad": "Calera",
        "codigo_postal": "98500"
    },
    "telefono": "478-125-3307",
    "email": "maurygr2020@gmail.com"
}
print(alumno["nombre"])
print(alumno["calificaciones"])

print("La calificación del alumno en programación es:")
print(alumno ["calificaciones"] ["Programación"])
