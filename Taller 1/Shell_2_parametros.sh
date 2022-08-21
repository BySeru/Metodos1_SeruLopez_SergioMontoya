function help(){

	echo "(っ◔︣◡◔᷅)っ Debe incluir tres paramétros:posición inicial, velocidad inicial y tiempo total. c(◕︣◡◕᷅c)"
}

if ! [ $# -eq 3 ]; then
	echo "son tres"
	help
	exit 1
else
	echo -ne 'corriendo programa                    (00%)\r'
	sleep 1
	echo -ne 'corriendo programa. .                 (20%)\r'
	sleep 1
	echo -ne 'corriendo programa. . . .             (40%)\r'
	sleep 1
	echo -ne 'corriendo programa. . . . . .         (60%)\r'
	sleep 1
	echo -ne 'corriendo programa. . . . . . . .     (80%)\r'
	sleep 1
	echo -ne 'corriendo programa. . . . . . . . . . (100%)\r'
	echo -ne '\n'
fi
1