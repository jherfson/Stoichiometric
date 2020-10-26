import json
from pymatgen.analysis.reaction_calculator import Reaction
from pymatgen.core.composition import Composition


__autor__ = 'Jherfson Castro Gomes'
__email__ = 'jherfson.castro@gmail.com'
__version__ = '2020.7.30'
__date__ = 'apr 24, 2020'


eq = input("Digite a equação: ")

mass_production = float(input("Digite o valor da massa: "))


# Tirando os espaços que tiver antes e depois da equação de síntese
# eq = eq.strip()


# fazendo a separação da reagente do produto
sep = eq.split('->')

# separando os reagente para passar para Classe Composition
reac = sep[0].split('+')

# separando os produtos para passar para Classe Composition
prod = sep[1].split('+')

reactants = [Composition(i) for i in reac]
production = [Composition(i) for i in prod]


reaction = Reaction(reactants, production)

mol_reactant = []
mass_reactant = []

for i in range(len(reac)):
    mol = (reaction.coeffs[i]/reaction.coeffs[-2]) * \
        (mass_production/Composition(prod[-2]).weight)
    mol_reactant.append(mol)
    mass = mol * Composition(reac[i]).weight
    mass_reactant.append(mass)


mol_production1 = mass_production/Composition(prod[-2]).weight
mol_production2 = (reaction.coeffs[-1]/reaction.coeffs[-2]) * \
    (mass_production/Composition(prod[-2]).weight)

mass_production2 = mol_production2*Composition(prod[-1]).weight

soma_production = mass_production + mass_production2



def to_dict():
    # composto
    comp = reac.copy()
    comp.extend(prod)
    
    # mol
    mol = mol_reactant.copy()
    mol.append(mol_production1)
    mol.append(mol_production2)
    
    # mass
    massa = mass_reactant.copy()
    massa.append(mass_production)
    massa.append(mass_production2)
    chemical_compounds = []
    for i in range(len(reaction.coeffs)):
        x = {comp[i]: {'coefciente': reaction.coeffs[i], 'peso molecular': Composition(
            comp[i]).weight, 'mol': mol[i], 'mass': massa[i]}}
        chemical_compounds.append(x)
    return chemical_compounds


def to_json():
    return json.dumps(to_dict(), indent=4, separators=(", ", " = "))

def print_total_mass():
    return {
        f'massa do reagente: {sum(mass_reactant)}',
        f'massa do produto: {soma_production}'
    }

print(print_total_mass())