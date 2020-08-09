# Atletas

**Atletas** fue el proyecto final para la materia optativa de _Desarrollo Seguro de Aplicaciones_ en la _Facultad de Informática_ de la _Universidad Nacional de La Plata_ (**UNLP**) a la que asistí durante mi estancia de intercambio en la primer mitad del 2020.
Este proyecto es una aplicación web vulnerable enfocada a ser usada en un CTF que formó parté del curso.

## Elaborado por                                                                                                                                                                                                

* Ballesteros Guillermo [/babiloneos](https://github.com/babiloneos)
* Ramos Esteban [/estebanramos](https://github.com/estebanramos)


## Para el ctf                                                                                                                                                                                               
~                                                                                                                                                                                                                  
```                                                                                                                                                                                                                
Título: Atletas                                                                                                                                                                                             
~                                                                                                                                                                                                                  
Descripción: Casi dioses entre los mortales.
```                                                                                                                                                                                                                
~                                                                                                                                                                                                                  
## Descripción                                                                                                                                                                                                     
~                                                                                                                                                                                                                  
La aplicación web emula la funcionalidad de un buscador que requiere loguin.
~                                                                                                                                                                                                                  
El objetivo es bruteforcear el login y lograr una inyección en la búsqueda para listar todas las imágenes, y encontrar información oculta en estas.   

#### Hint 1:
https://www.youtube.com/watch?v=-tJYN-eG1zk

#### Hint 2:
¿Qué opinas del 420, y del 69? A los admin del proyecto les gustan esos números.

#### Hint 3:
¡Malditas inyecciones! Tan fácil que sería poner la flag en una página sin más.

~ 

_Los hints, por si es necesario aclararlo, estarían mejor a cambio de puntos en el CTF._                                                                                                                                                                                                                  

## Dificultad                                                                                                                                                                                                      
~                                                                                                                                                                                                                  
Medio                                                                                                                                                                                                            
~                                                                                                                                                                                                                  
## Cómo deployarlo                                                                                                                                                               

Basta con ejecutar el container de docker despues de buildear la imagen con Dockerfile: docker run -p 1986:5000 --name atletas atletas:[TAG]                             
~                                                                                                                                                                                                                  
                                                                                                                                                                                                           
#### Build                                                                                                                                                         

Para buildear el reto: 
-git checkout Vulnerable
-docker build atletas:vulnerable

Para buildear el reto parcheado:
-git checkout Seguro
-docker build atletas:seguro

### Cómo cambiar la flag

- Ejecutar el script set_flag.sh mientras el container esté corriendo o con docker exec atletas bash set_flag.sh

- Ejecutar el container con el parametro -e FLAG=flag_a_setear y correr set_flag.sh

- Directamente meter el archivo flag.txt con la flag dentro a el archivo app/static/img/maradona.jpg con steghide sin password.

## Cómo resolverlo - Writeup

El método recomendado es:

- Romper el Loguin con Hydra usando rockyou y con usuario admin.
- Dentro del buscador entrar a /flag por la URL
- En base a lo encontrado buscar al atleta referido.
- Descargar la imágen del jugador.
- Con un análisis de esteganografía encontrar la flag dentro de la imagen.

