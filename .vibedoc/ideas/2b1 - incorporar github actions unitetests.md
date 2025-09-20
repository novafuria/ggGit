# incorporar github actions para unitetests

## Idea
Algo que surge de [2b - implementacion abstracciones](1.2.2 - implementacion de abstracciones.md) es la necesidad de realizar pruebas unitarias. Vamos a incorporar github actions para ejecutar esas pruebas unitarias en la nube para que se corran con cada actualización de una pull request sobre main.

Luego tendremos que agregar los tests unitarios a la documentación, pero tambien configurar el repositorio en GitHub para que se ejecuten las pruebas unitarias y bloquee el mergeo protegiendo la rama main.
