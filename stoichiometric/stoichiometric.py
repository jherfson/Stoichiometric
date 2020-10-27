import json
from pymatgen.analysis.reaction_calculator import Reaction
from pymatgen.core.composition import Composition


__autor__ = 'Jherfson Castro Gomes'
__email__ = 'jherfson.castro@gmail.com'
__version__ = '2020.3.8'
__date__ = 'apr 24, 2020'


class Stoichiometric():
    """[summary]
    """
    def __init__(self, equation, mass_production):
        """[summary]

        Args:
            equation ([type]): [description]
            mass_production ([type]): [description]
        """
        self.equation = equation
        self.mass_production = mass_production

        # fazendo a separação da reagente do produto
        self.separate_rp = self.equation.split('->')

        # separando os reagente para passar para Classe Composition
        self.reagent = self.separate_rp[0].split('+')

        # separando os produtos para passar para Classe Composition
        self.producer = self.separate_rp[1].split('+')

        reactants = [Composition(i) for i in self.reagent]
        producers = [Composition(i) for i in self.producer]


        self.reaction = Reaction(reactants, producers)

        self.mol_reactant = []
        self.mass_reactant = []

        for i in range(len(self.reagent)):
            mol = (self.reaction.coeffs[i]/self.reaction.coeffs[-2]) * \
                (mass_production/Composition(self.producer[-2]).weight)
            self.mol_reactant.append(mol)
            mass = mol * Composition(self.reagent[i]).weight
            self.mass_reactant.append(mass)


        self.mol_production1 = mass_production/Composition(self.producer[-2]).weight
        self.mol_production2 = (self.reaction.coeffs[-1]/self.reaction.coeffs[-2]) * \
            (mass_production/Composition(self.producer[-2]).weight)

        self.mass_production2 = self.mol_production2*Composition(self.producer[-1]).weight

        self.soma_production = mass_production + self.mass_production2


    def to_dict(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        # composto
        comp = self.reagent.copy()
        comp.extend(self.producer)

        # mol
        mol = self.mol_reactant.copy()
        mol.append(self.mol_production1)
        mol.append(self.mol_production2)

        # mass
        massa = self.mass_reactant.copy()
        massa.append(self.mass_production)
        massa.append(self.mass_production2)
        chemical_compounds = []
        for i in range(len(self.reaction.coeffs)):
            x = {comp[i]: {'coefciente': round(self.reaction.coeffs[i], 4), 'peso molecular': round(Composition(
                comp[i]).weight, 4), 'mol': round(mol[i], 4), 'mass': round(massa[i], 4)}}
            chemical_compounds.append(x)
        return chemical_compounds


    def to_json(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return json.dumps(self.to_dict(), indent=4, separators=(", ", " = "))

    def print_total_mass(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {
            f'massa do reagente: {round(sum(self.mass_reactant), 4)}',
            f'massa do produto: {round(self.soma_production, 4)}'
        }

    def individual_mass(self):
        pass


if __name__ == "__main__":
    eq = input("Digite a equação química: ")
    mass = float(input("Digite o valor da massa: "))
    st = Stoichiometric(eq, mass)
    print(st.to_json())
    print(st.print_total_mass())
    