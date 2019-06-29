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


class ElfAdapter(object):
    def __init__(self, elf):
        self.elf = elf

    def call_me(self):
        self.elf.nall_nin()


class DwarfAdapter(object):
    def __init__(self, dwarf):
        self.dwarf = dwarf

    def call_me(self):
        self.dwarf.estver_narho()


class HumanAdapter(object):
    def __init__(self, human):
        self.human = human

    def call_me(self):
        self.human.ring_mig()


if __name__ == "__main__":
    minions = [ElfAdapter(Elf()), DwarfAdapter(
        Dwarf()), HumanAdapter(Human())]

    for minion in minions:
        minion.call_me()
