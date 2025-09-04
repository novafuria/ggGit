# soporte para conda e instalacion de dependencias

## Idea

Necesitamos mejorar la experiencia de instalacion de dependencias con conda. Como toda aplicación de python usar ambientes virtuales para instalar las dependencias es lo recomendable. ggGit no es la excepción.

Entre las diferentes propuestas tenemos venv, uv y conda. Considerando que vamos a utilizar ggGit en Novafuria un laboratorio de Investigación y Desarrollo, la mejor opción es conda/mamba.

Ultimamente en Novafuria se esta utilizando mamba para instalar las dependencias de los proyectos. Es una herramienta que se ha ganado el corazon de los usuarios y es muy popular. Es compatible con conda y es muy rapida.

Hasta donde experimentamos, es posible crear un archivo yaml que levante el ambiente virtual de un proyecto para conda. Habra que investigar si este mismo archivo es posible utilizarlo con mamba, si requiere otro diferente o si es posible utilizarlo con ambas herramientas.

El ambiente al igual que el proyecto debe soportar Python 3.12, que es la ultima version estable de Python. Probablemente haya que especificar esto en la documentacion de arquitectura y otros documentos.

Otra cuestion que quizas corresponde tratarlo en ese mismo archivo de configuracion de ambiente es la instalacion de las dependencias. Por lo general, acostumbro a crear el ambiente en conda/mamba, activarlo y luego ejecutar `pip install -r requirements.txt` para instalar las dependencias. Usar pip es bastante popular, pero quizas con mamba existan propuestas diferentes. Es algo a investigar y debatir. Se que puede haber problemas con los registros de paquetes, mamba usa registro diferentes a los de conda, y otros sistemas como uv tambien usa registros diferentes. Es otra cuestion a investigar y debatir.

Consideremos tambien cual es el estado de arte de instalacion de dependencias del proyecto al momento de analizar esta idea.
