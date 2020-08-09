#path de la imagen
img_path=app/static/img/maradona.jpg


echo 'Ingrese la nueva flag: '
read new_flag
echo $new_flag > flag.txt

if [ -z $FLAG ]; then	
	#Añadir con steghide la flag de flag.txt a la imagen
	steghide embed -cf $img_path -ef flag.txt -p ''
else
	#Añadir la flag pasada como parametro a la imagen
	echo $FLAG > flag.txt
	steghide embed -cf $img_path -ef flag.txt -p ''
fi
