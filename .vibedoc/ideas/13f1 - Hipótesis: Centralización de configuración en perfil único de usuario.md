# 13f1 - Hipótesis: Centralización de configuración en perfil único de usuario

## Enunciado de la Hipótesis

**Dado** que los alcances contextuales (repositorio y módulo) de configuración de `ggGit` rara vez se utilizan y complican la UX del desarrollador,  
**Si** simplificamos radicalmente la clase `ConfigManager` para que lea y escriba únicamente de un único perfil global a nivel de usuario (por ejemplo, en `~/.gggit/config.json`) y valores por defecto fijos,  
**Entonces** eliminaremos la complejidad accidental de resolución jerárquica en el núcleo de configuración, reduciremos en un 70% las líneas de código de `src/core/config.py`, facilitaremos la depuración conceptual del estado de la suite y habilitaremos la creación de un Wizard interactivo y sencillo de configuración de IA.

## Justificación y Modelo Mental

La sobreingeniería (overengineering) es la tentación de resolver problemas hipotéticos en lugar de problemas reales. Un usuario de terminal espera que sus comandos y alias se comporten de manera predecible y consistente a lo largo de toda su máquina de desarrollo. Mantener configuraciones duplicadas y anidadas por carpeta añade entropía. Al unificar la base en un único archivo de configuración del usuario, convertimos el sistema de configuración en algo predecible y fácil de razonar.

## Validation Experimental

Para validar la remoción segura de la lógica jerárquica de configuración y unificar los tests asociados, se propone el siguiente diseño experimental:

- [[13f1a - Experimento: Refactorización y unificación de ConfigManager en un solo nivel de usuario]]

## Referencias

- [[13f - Simplificación del alcance de configuración a nivel de usuario]]
- [[4a - analisis serie historias configuracion]]
