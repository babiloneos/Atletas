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
~                                                                                                                                                                                                                  
## Dificultad                                                                                                                                                                                                      
~                                                                                                                                                                                                                  
Medio                                                                                                                                                                                                            
~                                                                                                                                                                                                                  
## Cómo deployarlo                                                                                                                                                               

Basta con ejecutar el container de docker despues de buildear la imagen con Dockerfile.                                   
~                                                                                                                                                                                                                  
### Cómo instalarlo                                                                                                                                                                                                
~                                                                                                                                                                                                                  
#### Build                                                                                                                                                                                                         

### Cómo cambiar la flag

- Ejecutar el script set_flag.sh mientras el container esté corriendo
ó
- Ejecutar el container con el parametro -e FLAG=flag_a_setear

### Cómo lo acceden

- http://URL/

## Cómo resolverlo - Writeup

El método recomendado es:

- Romper el Loguin con Hydra usando rockyou.
- Dentro del buscador se puede usar ZAP (spider) para encontrar y entrar a /flag
- En base a lo encontrado buscar al atleta referido.
- Descargar la imágen del jugador.
- Con un análisis de esteganografía encontrar la flag dentro de la imagen.

