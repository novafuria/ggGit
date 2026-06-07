# 13f - Simplificación del alcance de configuración a nivel de usuario

## Contexto y Problema

Actualmente, `ggGit` hereda un sistema de configuración jerárquico y contextual de alta complejidad que evalúa cuatro niveles de alcance: repositorio local > módulo específico > perfil de usuario > valores por defecto (configuración por defecto). 

Aunque esta jerarquía suena sofisticada en papel, en la práctica del desarrollador real introduce problemas innecesarios:
1.  **Falta de Uso Real**: El 99% de los usuarios solo configuran sus preferencias de Git y sus credenciales de IA una única vez de forma global (en su carpeta de usuario `~/.gggit` o similar). La necesidad de perfiles específicos de IA "por carpeta de módulo" o "por repositorio local" es prácticamente inexistente en flujos reales de alias Git.
2.  **Complejidad de Depuración**: Cuando algo falla (por ejemplo, el prompt dice *"IA no configurada"*), rastrear qué archivo de configuración intermedio (de los 4 alcances) está sobreescribiendo el endpoint de IA o el token es confuso y requiere un análisis manual complejo.
3.  **Bloqueo de la UX Simplificada**: Esta jerarquía y multiplicidad de alcances es el principal stopper para poder crear un asistente interactivo amigable (Wizard de configuración) que configure todo de un plumazo, ya que el asistente tendría que lidiar con la toma de decisiones complejas sobre dónde escribir y de dónde leer cada propiedad.

## Evolución e Hipótesis

Para unificar la lectura de configuración y simplificar radicalmente la arquitectura de `ConfigManager`, planteamos la siguiente hipótesis:

- [[13f1 - Hipótesis: Centralización de configuración en perfil único de usuario]]

## Referencias

- [[4 - sistema de configuracion jerarquica]]
- [[7 - sistema de validacion y esquemas]]
