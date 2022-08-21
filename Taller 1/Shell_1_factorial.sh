if [ $# -eq 1 ]; then
	cont=1
	for i in $(seq 1 $1); do	
		cont=$(($cont*$i))
	done
	n_fact=$((cont))
	echo $n_fact
	else
    	echo -n "debe ingresar solo un parametro: "
		read n
		(./Shell_1_factorial.sh $n)
fi