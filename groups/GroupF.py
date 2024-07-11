from teams.team import Team
from teams.quality_distribution import QualityDistribution

turkeyOffensiveQDist = QualityDistribution(1.3, 1.2)
turkeyDefensiveQDist = QualityDistribution(1.5, 1.7)

georgiaOffensiveQDist = QualityDistribution(0.4, 1.1)
georgiaDefensiveQDist = QualityDistribution(2.9, 1.3)

portugalOffensiveQDist = QualityDistribution(2.9, 1.2)
portugalDefensiveQDist = QualityDistribution(0.5, 1.4)

czechiaOffensiveQDist = QualityDistribution(1.6, 1.2)
czechiaDefensiveQDist = QualityDistribution(1.5, 1.4)

turkey = Team("Turkey", [], turkeyOffensiveQDist, turkeyDefensiveQDist)
georgia= Team("Georgia", [], georgiaOffensiveQDist, georgiaDefensiveQDist)
portugal = Team("Portugal", [], portugalOffensiveQDist, portugalDefensiveQDist)
czechia = Team("Czechia", [], czechiaOffensiveQDist, czechiaDefensiveQDist)

groupF = [turkey, georgia, portugal, czechia]