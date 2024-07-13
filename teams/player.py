class Player():
    """
    A class representing a soccer player

    Attributes:
        name (str): The name of player.
        country (str): The name of country.
        position (str): The position of player.
        quality (int): Ability of player.
        club (str): Name of club.
    """
    def __init__(self, name, country, position, quality, club):
        """
        Initialize a new player instance.

        Args:
            name (str): The name of player.
            country (str): The name of country.
            position (str): The position of player.
            quality (int): Ability of player.
            club (str): Name of club.
        """
        self._name = name
        self._country = country
        self._position = position
        self._quality = quality 
        self._club = club

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def position(self):
        return self._position

    @property
    def quality(self):
        return self._quality
    
    @property
    def club(self):
        return self._club

    @name.setter
    def name(self, name):
        self._name = name

    @country.setter
    def teamB(self, country):
        self._country = country

    @position.setter
    def position(self, position):
        self._position = position
    
    @quality.setter
    def quality(self, quality):
        self._quality = quality

    @club.setter
    def quality(self, club):
        self._club = club

    def teamB(self, teamBGoalsScored):
        self._teamBGoalsScored = teamBGoalsScored
    def name(self):
        return self._name
    def country(self):
        return self._country
    def position(self):
        return self._position
    def quality(self):
        return self._quality
    def club(self):
        return self._club