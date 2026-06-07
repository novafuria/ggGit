# 13g - Interfaz interactiva de configuración de IA

## Contexto y Problema

Configurar el sistema de Inteligencia Artificial en `ggGit` es un proceso con una alta fricción técnica y cognitiva para el usuario. Actualmente, para habilitar e integrar el autocompletado de commits, un desarrollador debe ejecutar múltiples comandos manuales del tipo:
```bash
ggconfig set ai.enabled true
ggconfig set ai.provider openai
ggconfig set ai.api_key_env GGGIT_AI_KEY
ggconfig set ai.base_url http://localhost:11434
export GGGIT_AI_KEY=ollama
```
Esto requiere comprender qué propiedades se deben configurar y recordar nombres específicos, lo cual induce a errores de tipografía (typos), desalineamientos de variables de entorno y fallos de conexión que terminan con el error *"IA no configurada"*. Necesitamos simplificar drásticamente esta experiencia mediante un mecanismo guiado por la propia terminal.

## Evolución e Hipótesis

Como paso evolutivo que se apoya en la simplificación del alcance de configuración a nivel de usuario (desarrollado en [[13f1 - Hipótesis: Centralización de configuración en perfil único de usuario]]), planteamos la siguiente hipótesis de UX interactiva:

- [[13g1 - Hipótesis: Asistente Wizard interactivo de configuración de IA]]

## Referencias

- [[1c - reflexion-documentacion-configuracion-ia]]
- [[5 - sistema de interfaz de usuario cli]]
- [[13f - Simplificación del alcance de configuración a nivel de usuario]]
