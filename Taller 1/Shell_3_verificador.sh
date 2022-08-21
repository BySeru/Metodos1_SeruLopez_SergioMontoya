pass=0

function checkvalue(){
    if [[ $1 = 0 || $1 = 1 ]]; then
        pass=1
    else
        echo "╔══════════════════════════════════════════════════════════════════════════╗"
        echo "  Supongamos que $value es un elemento del conjunto {0,1}."
        echo "  Luego $value=0 o $value=1, no obstante $value difiere de dichos valores."
        echo "  Dado que se llega a una contradicción, se ha de escoger otro número."
        echo "  Inténtelo de nuevo."
        echo "╚══════════════════════════════════════════════════════════════════════════╝"
    fi
}

while [ $pass -eq 0 ]; do
    read -p "Ingrese un número tq pertenezca al conjunto {0,1}: " value
    checkvalue $value
done
1