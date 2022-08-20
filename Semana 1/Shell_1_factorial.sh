echo -n "Ingrese el número del cual desea conocer el factorial: "
read n
function factorial(){
	local cont=1
	for i in $(seq 1 $n)
	do	
		cont=$(($cont*$i))
	done
	n_fact=$((cont))
}
factorial
echo "El factorial de $n es: $n_fact"