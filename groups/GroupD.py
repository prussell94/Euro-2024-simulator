from teams.team import Team
from teams.quality_distribution import QualityDistribution

polandOffensiveQDist = QualityDistribution(1.3, 1.4)
polandDefensiveQDist = QualityDistribution(1.4, 1.2)

netherlandsOffensiveQDist = QualityDistribution(1.9, 1.1)
netherlandsDefensiveQDist = QualityDistribution(1.3, 1.3)

austriaOffensiveQDist = QualityDistribution(1.5, 1.4)
austriaDefensiveQDist = QualityDistribution(1.4, 1.4)

franceOffensiveQDist = QualityDistribution(3.1, 1.1)
franceDefensiveQDist = QualityDistribution(0.8, 1.3)

poland = Team("Poland", [], polandOffensiveQDist, polandDefensiveQDist)
netherlands= Team("Netherlands", [], netherlandsOffensiveQDist, netherlandsDefensiveQDist)
austria = Team("Austria", [], austriaOffensiveQDist, austriaDefensiveQDist)
france = Team("France", [], franceOffensiveQDist, franceDefensiveQDist)

groupD = [poland, netherlands, austria, france]
