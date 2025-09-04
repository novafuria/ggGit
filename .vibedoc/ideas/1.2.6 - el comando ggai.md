# el comando ggai

## Idea
Vamos a implementar el comando ggai.

El comando ggai es el comando que se encargara de la gestion de la IA en ggGit.

Este comando requiere una discusión mas profunda sobre su diseño y funcionalidad. Si bien parece que la idea es que se ejecute una instrucción y una vez finalizada la instrucción el comando termine, en la practica esto puede que no sea asi. El comando ggai podría ser un comando conversacional y permitir hacer preguntas a la IA.

Se cruzan dos tipos de funcionalidades:

1. Una funcionalidad conversacional
2. Una funcionalidad ejecutiva

La funcionalidad conversacional se encargara de hacer preguntas a la IA y de realizar una conversación con la IA.

La funcionalidad ejecutiva se encargara de realizar una tarea compleja.

Que ocurre cuando se ejecuta el comando ggai sin argumentos?
