"""
https://github.com/PJUllrich/Design-Patterns
"""


class Elf(object):
    def nall_nin(self):
        print("Elf says: Calling the Overload ...")


class Dwarf(object):
    def estver_narho(self):
        print("Dwarf says: Calling the Overload ...")


class Human(object):
    def ring_mig(self):
        print("Human says: Calling the Overload ...")


if __name__ == "__main__":
    minions = [Elf(), Dwarf(), Human()]

    for minion in minions:
        if isinstance(minion, Elf):
            minion.nall_nin()
        elif isinstance(minion, Dwarf):
            minion.estver_narho()
        else:
            minion.ring_mig()
