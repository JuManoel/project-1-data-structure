# project-1-data-structure

## Descripción del Proyecto
Este proyecto se centra en la implementación y manipulación de estructuras de datos, específicamente árboles. Se exploran conceptos como árboles binarios, productos organizados en estructuras de árbol, y árboles AVL (Adelson-Velsky y Landis). El ensenario para eso es duna tienda

## Contenido del Proyecto
- **Árboles Binarios**: Implementación básica de árboles binarios y sus operaciones fundamentales.
- **Productos en Árboles**: Organización y gestión de productos utilizando estructuras de árbol para optimizar búsquedas y almacenamiento.
- **Árboles AVL**: Implementación de árboles AVL, un tipo de árbol binario auto-balanceado que mantiene su altura mínima para mejorar la eficiencia de las operaciones.

## Requisitos del Sistema
- Lenguaje de programación: python 3
- pygame, pandas, numpy

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/project-1-data-structure.git

## Estudianes que lo hicieron:
1. <a href = "https://github.com/Cristian46310">Cristian David Grisales</a>
2. <a href = "https://github.com/JuManoel">Juan Manoel Miranda Gómez</a>

## Agradecimientos especiales
1. ChatGPT, TabNine
2. Sabryna
3. Jairo y Cesar

## Forma de organizacion
1. Cristian: todo lo que esta en la carpeta ./front es de cristian
2. Juan: Todo lo que esta en la carpeta ./back es de Juan

## Dificuldades encontradas
1. Pygame: pygame es una libreria muy nueva para nosostros, nunca habiamos trabado con
lo que genero unas cierta dificuldades principalmente en la hora de hacer screen bonita
2. Coneccion con el front: como estamos trabajando con un modelo estilo API la idea era que 
lo que funciona aca, tiene que funcionar con otro motor grafico. Pero hacer siempre la
primera connecion no es lo mas facil, lo que genero algunas horas de debug

## Logica de guardado del Arbol (ok)
No guardamos el arbol como tal, si no que guardamos los productos
si no que guardamos como una lista de productos en un csv llamado
./productos.csv Elejomos de esa manera por ser mas simple y mas facil
mantenimiento y actualizacion.

id,nombre,precio,stock,categoria
2,queso,15000.0,20,lacteos
3,pan,15000.0,20,trigo y derivados
4,arepas,5000.0,30,maiz

## Logica para adicionar productos (ok)
La logica para eso hicimos 3 passos.
1. Recibimos los datos de los productos
2. creamos el producto y lo insertamos en el arbol
3. guardamos la lista de todos los productos
Durante el processo de inserccion hacemos las rotaciones y vamos guardando
todos los estados de rotacion en una variable Estados. Esa variable tendra la 
funcion de guardar "los frames" de las rotaciones de los arboles
retornamos el arvol y los estados.
El metodo valida tambien si los datos del producto estan correctos, o sea
si no hay precios o cantidad menores que 0

## Logica para buscar producto por ID (ok)
Por ser un arbol binario de busqueda lo hacemos es recorrer todos los nodos
como en inorden, y vamos activando y desactivando los nodos para que lo veamos cambiando
de color y indentifique cual es nodo que buscamos

## Borrar un nodo (ok)
Para borrar el nodo lo que hacemos es primero borrar el de la base de datos
y despues rearmar el arbol con la nueva base de datos.
Elejimos eso para que no nos difilcultara con la parte de rotaciones y con miedo de
perder algun nodo o insertar en un ludar indevido.
Pensava en un otro modo donde lo borramos de una vez en el arbol
Funcionaria asi: 
1. cojiamos el nodo padre (1)
2. guardariamos los hijos del nodo (2,3)
3. cambiarimaos el cojiamos del hijo de (1) que queremos borrar y 
pondriamos (2) o (3) como nuevo hijo.
4. el hijo sobrande lo volveriamos a insertar.

Pero como dije, me dava algo de miedo que de la nada se perdiera un nodo
entonces por mantener la integridad del arbol prefiero re hacer todo el arbol

## Modificar un nodo (ok)
Primero el usuario tiene que elejir el Id del nodo que el quiere y despues poner
los datos que quieres cambiar, como se fuera crear un nuevo producto
el hace la busqueda en el arbol, y cambia las referencias de los hijos y los
otros datos del nodo
Cuando el nodo es tiene la cantidad = 0 simplemente va a borrar el producto.
Y cuando el producto tiene datos incorrectos el no hace ninguna modificacion en el arbol

## Busqueda Avanzada (ok)
El usuario tendra que ingresar datos como nombre, precio minimo, maximo y categoria
despues el utiliza un recorido RID para ir cambiando los nodos
