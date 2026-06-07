# 13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull

## Enunciado de la Hipótesis

**Dado** que el desarrollador ejecuta el comando `ggpl` para sincronizar su rama con el remoto,  
**Si** modificamos el método `pull` de `GitInterface` (o el flujo del comando `ggpl.py`) para que añada por defecto el parámetro `--tags` o realice un `git fetch --tags` de forma inmediata y automática tras una fusión exitosa,  
**Entonces** el espacio de trabajo local mantendrá un estado de tags 100% idéntico al remoto en cada pull, eliminando pasos manuales adicionales y asegurando la integridad del historial de versiones local.

## Justificación y Modelo Mental

Un comando de conveniencia como `ggpl` debe ofrecer un comportamiento de "sincronización total por defecto". El comportamiento nativo de Git suele separar el pull de ramas del fetch de tags para optimizar el ancho de banda, pero en la práctica moderna de desarrollo ágil esto introduce fricciones innecesarias. Esta hipótesis asume que la sincronización de etiquetas es parte del "éxito del pull" que el usuario espera instintivamente al invocar `ggpl`.

## Validación Experimental

Para probar esta hipótesis, se plantea un experimento que incluye su diseño y validación en la suite de pruebas unitarias:

- [[13d1.1 - Experimento: Implementación de descarga de tags automática en ggpl]]

## Referencias

- [[13d - El comando ggpl no obtiene las etiquetas o tags del remoto]]
- [[8 - sistema de integracion con git]]
