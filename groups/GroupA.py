from teams.team import Team
from teams.quality_distribution import QualityDistribution

germanyOffensiveQDist = QualityDistribution(2.9, 1.1)
germanyDefensiveQDist = QualityDistribution(0.8, 1.4)

scotlandOffensiveQDist = QualityDistribution(0.8, 1.7)
scotlandDefensiveQDist = QualityDistribution(1.2, 1.5)

switzerlandOffensiveQDist = QualityDistribution(1.4, 1.6)
switzerlandDefensiveQDist = QualityDistribution(0.7, 1.4)

hungaryOffensiveQDist = QualityDistribution(1.2, 1.6)
hungaryDefensiveQDist = QualityDistribution(1.2, 1.4)

germany = Team("Germany", [], germanyOffensiveQDist, germanyDefensiveQDist)
scotland = Team("Scotland", [], scotlandOffensiveQDist, scotlandDefensiveQDist)
switzerland = Team("Switzerland", [], switzerlandOffensiveQDist, switzerlandDefensiveQDist)
hungary = Team("Hungary", [], hungaryOffensiveQDist, hungaryDefensiveQDist)

groupA = [germany, scotland, switzerland, hungary]