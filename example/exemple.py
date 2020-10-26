from stoichiometric.stoichiometric.stoichiometric import Stoichiometric
##import stoichiometric 

eq = "Li2CO3 + Nb2O5 -> Li1Nb3O8 + CO2"
mass = 5.0

s = Stoichiometric(eq, mass)


print(s.to_json())