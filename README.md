# Grupo 07

## Integrantes                                                                                                                                                                                                 
Ballesteros Guillermo

Ramos Esteban


## Para el ctfd                                                                                                                                                                                               
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
Quizás podrías probar con un diccionario famoso

#### Hint 2:
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
### Cómo instalarlo                                                                                                                                                                                                
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

### Cómo lo acceden

- http://URL:1986

## Cómo resolverlo - Writeup

El método recomendado es:

- Romper el Loguin con Hydra usando rockyou.
- Dentro del buscador se puede usar ZAP (spider) para encontrar y entrar a /flag
- En base a lo encontrado buscar al atleta referido.
- Descargar la imágen del jugador.
- Con un análisis de esteganografía encontrar la flag dentro de la imagen.

