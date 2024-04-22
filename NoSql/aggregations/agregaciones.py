db.estudiante.aggregate([
    {"$group": {"_id": "$género", "total": {"$sum": 1}}}
])


db.estudiante.aggregate([
    {"$unwind": "$historialAcadémico"},
    {"$unwind": "$historialAcadémico.materias"},
    {"$group": {"_id": "$historialAcadémico.materias.nombre", "promedio": {"$avg": "$historialAcadémico.materias.nota"}}}
])


db.estudiante.aggregate([
    {"$unwind": "$historialAcadémico"},
    {"$group": {"_id": {"año": {"$year": "$historialAcadémico.fechaGraduacion"}}, "total": {"$sum": 1}}}
])


db.estudiante.aggregate([
    {"$unwind": "$historialAcadémico"},
    {"$group": {"_id": "$historialAcadémico.programa", "promedio": {"$avg": "$historialAcadémico.materias.nota"}}}
])


db.estudiante.aggregate([
    {"$group": {"_id": "$estrato", "total": {"$sum": 1}}}
])


db.estudiante.aggregate([
    {"$unwind": "$historialAcadémico"},
    {"$group": {"_id": "$historialAcadémico.facultad", "promedio": {"$avg": "$historialAcadémico.materias.nota"}}}
])


db.estudiante.aggregate([
    {"$unwind": "$proyectoGraduación"},
    {"$group": {"_id": "$proyectoGraduación.tipo", "total": {"$sum": 1}}}
])


db.estudiante.aggregate([
    {"$group": {"_id": "$historialAcadémico.programa", "promedioEdad": {"$avg": {"$year": "$fechaNacimiento"}}}}
])


db.estudiante.aggregate([
    {"$unwind": "$proyectoGraduación"},
    {"$match": {"proyectoGraduación.tipo": "bapi"}},
    {"$group": {"_id": "$proyectoGraduación.pais", "total": {"$sum": 1}}}
])


db.estudiante.aggregate([
    {"$unwind": "$proyectoGraduación"},
    {"$group": {"_id": "$proyectoGraduación.tipo", "notas": {"$push": "$proyectoGraduación.nota"}}}
])


[
    {"$unwind": "$historialAcadémico"},
    {"$match": {
        "$expr": {
            "$and": [
                {"$gte": [{"$year": "$historialAcadémico.fechaGraduacion"}, {{Min_year}}]},
                {"$lte": [{"$year": "$historialAcadémico.fechaGraduacion"}, {{Max_year}}]}
            ]
        }
    }},
    {"$group": {"_id": {"$year": "$historialAcadémico.fechaGraduacion"}, "total": {"$sum": 1}}}
]