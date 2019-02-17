"""
https://github.com/PJUllrich/Design-Patterns
"""


class Elf(object):
    name = 'Galadriel'

    def nall_nin(self):
        print("Elf says: Calling the Overload ...")


class Dwarf(object):
    def estver_narho(self):
        print("Dwarf says: Calling the Overload ...")


class Human(object):
    def ring_mig(self):
        print("Human says: Calling the Overload ...")


class MinionAdapter(object):
    _initialised = False

    def __init__(self, minion, **adapter_methods):
        self.minion = minion
        for k, v in adapter_methods.items():
            func = getattr(self.minion, v)
            self.__setattr__(k, func)
        self._initialised = True

    def __getattr__(self, attr):
        """ Attributes not in Adapter are delegated to the minion """
        return getattr(self.minion, attr)

    def __setattr__(self, k, v):
        """ Set attributes normally during initialisation"""
        if not self._initialised:
            super().__setattr__(k, v)
        else:
            """ Set attributes on minion after initialisation """
            setattr(self.minion, k, v)


if __name__ == "__main__":
    minion_adapters = [
        MinionAdapter(Elf(), call_me='nall_nin'),
        MinionAdapter(Dwarf(), call_me='estver_narho'),
        MinionAdapter(Human(), call_me='ring_mig')
    ]

    for adapter in minion_adapters:
        adapter.call_me()

    elf_adapter = minion_adapters[0]
    print()
    print("Name from Adapter: {0}".format(elf_adapter.name))
    print("Name from Minion: {0}".format(elf_adapter.minion.name))

    minion_adapters[0].name = "Elrond"
    print()
    print("Name from Adapter: {0}".format(elf_adapter.name))
    print("Name from Minion: {0}".format(elf_adapter.minion.name))
