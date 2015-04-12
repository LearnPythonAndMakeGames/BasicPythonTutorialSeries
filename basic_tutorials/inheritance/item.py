# D.R.Y.  Don't Repeat Yourself
# Item:
#     Weapon:
#          Sharp Edge:
#              Sword:
#                  Long Sword
#                      special hilt
#                      special engraving
#                      special jagged edge
#                  Broad Sword
#                 ...
#              Axe:
#                 ...
#              Dagger:
#                 ...
#          Blunt Edge:
#              Staff:
#                 ...
#     Ore:
#          Iron
#          Crystal
#          Gem
#     Element:
#          Carbon
#          Manganese
#          Chromium
#          Nickel
#          Tungsten


class Item(object):
    """Base Item class"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        class_name = self.__class__.__name__
        return "<{} {}:{}>".format(class_name, self.name, self.value)

    def __str__(self):
        return "  {}: {}".format(self.name, self.value)


class Mixin(object):
    """Base Mixin Class"""


class Equipable(Mixin):
    """Item is equipable"""
    equipable = False


class CombatUse(Mixin):
    """Item can be used in combat"""
    combat_ready = False

    def attack(self):
        """Calculates the value of attack during combat"""
        return 1


class Thrown(Mixin):
    """Item can be thrown"""
    throwable = False

    def throw(self):
        return None


class Craftable(Mixin):
    """Item can be used in crafting"""
    craftable = False

    def combine(self, other):
        """combines this item with another"""
        result = None
        return result


class Weapon(Equipable, CombatUse, Thrown, Item):
    """Base Weapon class"""

    def __init__(self, name, value):
        super(Weapon, self).__init__(name, value)
        self.equipable = True

    def __str__(self):
        star = " "
        if self.equipable:
            star = "*"
        return "{} {}: {}".format(star, self.name, self.value)

    def melt(self):
        """Melts the weapon into constituent parts"""
        parts = []
        return parts


class Ore(CombatUse, Thrown, Craftable, Item):
    """Base Ore class"""

    def __init__(self, name, value):
        super(Weapon, self).__init__(name, value)
        self.equipable = True

    def __str__(self):
        star = " "
        if self.equipable:
            star = "*"
        return "{} {}: {}".format(star, self.name, self.value)


if __name__ == "__main__":
    item = Item("item", 100)
    sword = Weapon("sword", 150)
    print item
    print sword
