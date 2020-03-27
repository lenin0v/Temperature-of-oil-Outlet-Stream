# Temperature-of-oil-Outlet-Stream
Intro to Thermal Sciences Schmidt Problem 7-8

#problem 7-8

A = 2200
m = 4.4
Cp = 0.2415

U = 6

Cmin = Cp*m*3600

Thi = 400 
Tci = 20

NTU = (U*A)/(Cmin)

print (f"NTU = {NTU}")

E = 0.71

Q = E*Cmin*(Thi-Tci)

print (f"Q = {Q} Btu/hr")

Thd = (Q/(-Cmin)) + Thi

print (f"Thd = {Thd}˚F")

Tcd = (Q/(Cmin)) + Tci

print (f"Tcd = {Tcd}˚F")
