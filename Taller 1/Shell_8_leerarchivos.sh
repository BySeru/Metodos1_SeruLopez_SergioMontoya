cont=0

while IFS= read -r line; do
    rutas[$cont]=$line
    cont=$(($cont+1))
done < lista.dat

echo ${rutas[2]}