from scipy.stats import norm, truncnorm

class QualityDistribution():
    """
    A class representing a probability distribution which reflects the quality of a certain component of a team (offensive, defensive quality etc.)

    Attributes:
        mean (float): The mean of quality
        stdev (float): The standard deviation of quality.
    """
    def __init__(self, mean, stdev):
        self._mean = mean
        self._stdev = stdev
    def get_mean(self):
        return self._mean
    def get_stdev(self):
        return self._stdev
    
    @property
    def mean(self):
        return self._mean
    
    @property
    def stdev(self):
        return self._stdev

    @mean.setter
    def mean(self, m):
        self._mean = m

    @stdev.setter
    def stdev(self, std):
        self._stdev = std

    def get_goal_estimate(self):
        """
        Retrieves an estimate of number of goals scored/conceded

        Returns:
            number_of_goals (float): An estimate of number of goals scored/conceded. Currently upper bounded with 6 goals
        """
        lower_bound=0
        upper_bound=6
        a = (lower_bound - self.get_mean() / self.get_stdev())
        b = (upper_bound - self.get_mean()) / self.get_stdev()
        team_dist=truncnorm(a=a, b=b, loc=self.get_mean(), scale=self.get_stdev())
        number_of_goals = team_dist.rvs(size=1)
        return number_of_goals
    
    def accept(self, visitor):
        return visitor.visit_quality_distribution(self)