class Rat(object):

    DEFAULT_HEALTH = 100
    DEFAULT_STARVE = 34
    rats = []

    @property
    def health(self):
        attr = '_health'
        if not hasattr(self, attr):
            setattr(self, attr, self.DEFAULT_HEALTH)
        return getattr(self, attr)

    @health.setter
    def health(self, value):
        self._health = value
        self.rats[self.rat_idx] = self._health

    def __init__(self, name=None, health=None):
        self.fed = False
        self.rat_idx = len(self.rats)
        if name is None:
            name = 'Rat{:<03}'.format(self.rat_idx)
        self.name = name
        if health is None:
            health = self.DEFAULT_HEALTH
        self.rats.append(health)
        self.health = health if health is not None else self.DEFAULT_HEALTH

    def was_fed(self):
        return self.fed == True

    def feed(self):
        self.fed = True

    def starve(self):
        self.fed = False
        self.health -= self.DEFAULT_STARVE
        self.rats[self.rat_idx] = self.health

    def reset_feed_state(self):
        self.fed = False

    def is_alive(self):
        return self.health > 0
