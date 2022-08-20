function help(){

	echo "(っ◔︣◡◔᷅)っ Debe incluir tres paramétros c(◕︣◡◕᷅c)"
}

if ! [ $# -eq 3 ]; then
	echo "son tres"
	help
	exit 1
fi