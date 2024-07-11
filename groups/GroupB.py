from teams.team import Team
from teams.quality_distribution import QualityDistribution

spainOffensiveQDist = QualityDistribution(2.5, 1.4)
spainDefensiveQDist = QualityDistribution(0.9, 1.2)

croatiaOffensiveQDist = QualityDistribution(2.2, 1.2)
croatiaDefensiveQDist = QualityDistribution(0.9, 1.5)

italyOffensiveQDist = QualityDistribution(1.9, 0.7)
italyDefensiveQDist = QualityDistribution(0.4, 1.1)

albaniaOffensiveQDist = QualityDistribution(0.8, 1.1)
albaniaDefensiveQDist = QualityDistribution(2.4, 1.4)

spain = Team("Spain", [], spainOffensiveQDist, spainDefensiveQDist)
croatia = Team("Croatia", [], croatiaOffensiveQDist, croatiaDefensiveQDist)
italy = Team("Italy", [], italyOffensiveQDist, italyDefensiveQDist)
albania = Team("Albania", [], albaniaOffensiveQDist, albaniaDefensiveQDist)

groupB = [spain, croatia, italy, albania]