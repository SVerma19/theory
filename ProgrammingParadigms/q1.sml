fun sum 0 = 0 
    | sum n = n + sum (n - 1);

fun cumulative (n) = 
    if n = 0
        then 0 
    else
        n + sum(n - 1);

cumulative(5);
cuulative(7);



exception Empty
val rec lastelem =
  fn (h::nil) => h
    |(h::list) => lastelem (list)
    | (nil) => raise Empty;

lastelem([1, 2, 3, 4]);
lastelem([2, 3, 7, 8, 10, 12]);

