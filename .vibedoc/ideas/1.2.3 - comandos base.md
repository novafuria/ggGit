# comandos base

## Idea
Una vez que contamos con las abstracciones base, podemos avanzar con los comandos base.

Los comandos base son los comandos que se encargan de la logica general de ggGit. Estos comandos deben ser reutilizables y deben ser lo mas independientes posibles.

No es la idea que estos comandos sean accesibles directamente por el usuario, sino que sean utilizados por los comandos específicos.

Vamos a seguir la estructura de directorios python [1.2.1 - estructura de directorios python](1.2.1 - estructura de directorios python.md) y vamos a implementar los comandos base en el archivo `base_commands/base.py`.

Los comandos base son:

1. `base.py`
2. `commit.py`
3. `config.py`

Posiblemente debamos ser cautelosos con estas implementaciones, asi que optar por una planificacion gradual e incremental es lo mejor. Cada implementación debera tener las pruebas unitarias correspondientes y ser incorporadas a los github actions.
