from teams.team import Team
from teams.quality_distribution import QualityDistribution

belgiumOffensiveQDist = QualityDistribution(2.9, 1.6)
belgiumDefensiveQDist = QualityDistribution(1.4, 1.6)

slovakiaOffensiveQDist = QualityDistribution(1.1, 1.1)
slovakiaDefensiveQDist = QualityDistribution(1.6, 1.3)

romaniaOffensiveQDist = QualityDistribution(1.3, 1.4)
romaniaDefensiveQDist = QualityDistribution(1.5, 1.4)

ukraineOffensiveQDist = QualityDistribution(1.2, 1.1)
ukraineDefensiveQDist = QualityDistribution(1.6, 1.3)

belgium = Team("Belgium", [], belgiumOffensiveQDist, belgiumDefensiveQDist)
slovakia= Team("Slovakia", [], slovakiaOffensiveQDist, slovakiaDefensiveQDist)
romania = Team("Romania", [], romaniaOffensiveQDist, romaniaDefensiveQDist)
ukraine = Team("Ukraine", [], ukraineOffensiveQDist, ukraineDefensiveQDist)

groupE = [belgium, slovakia, romania, ukraine]