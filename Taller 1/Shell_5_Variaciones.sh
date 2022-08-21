n=20
r=3
rest=$(($n-$r))

n_fact=$(./Shell_1_factorial.sh $n)
rest_fact=$(./Shell_1_factorial.sh $rest)

var=$(($n_fact / $rest_fact))

echo $var
