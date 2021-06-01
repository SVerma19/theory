suspect(john).
suspect(julia).
suspect(kane).

victim(gordon).

loves(julia, gordon).
loves(julia, kane).

knows(john, julia).
knows(john, gordon).
knows(john, kane).
knows(X, Y) :- loves(X, Y).
    
kitchen(julia).
kitchen(kane).
balcony(john).

?- killer(X) :- kitchen(Y), knows(Z, Gordon).