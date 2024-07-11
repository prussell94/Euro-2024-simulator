from teams.team import Team
from teams.quality_distribution import QualityDistribution

sloveniaOffensiveQDist = QualityDistribution(0.8, 1.4)
sloveniaDefensiveQDist = QualityDistribution(1.5, 1.2)

denmarkOffensiveQDist = QualityDistribution(1.7, 1.1)
denmarkDefensiveQDist = QualityDistribution(1.2, 1.3)

serbiaOffensiveQDist = QualityDistribution(1.0, 1.4)
serbiaDefensiveQDist = QualityDistribution(1.9, 1.4)

englandOffensiveQDist = QualityDistribution(2.7, 1.1)
englandDefensiveQDist = QualityDistribution(0.8, 1.3)

slovenia = Team("Slovenia", [], sloveniaOffensiveQDist, sloveniaDefensiveQDist)
denmark= Team("Denmark", [], denmarkOffensiveQDist, denmarkDefensiveQDist)
serbia = Team("Serbia", [], serbiaOffensiveQDist, serbiaDefensiveQDist)
england = Team("England", [], englandOffensiveQDist, englandDefensiveQDist)

groupC = [slovenia, denmark, serbia, england]