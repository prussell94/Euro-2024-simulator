import unittest
from unittest.mock import MagicMock
import matches.match
import teams.team
import states

class TestSimulateMatch(unittest.TestCase):

    def setUp(self):
        # Create mock objects for Team
        self.team_a = MagicMock(spec=teams.team.Team)
        self.team_b = MagicMock(spec=teams.team.Team)

        # Set up mock return values for goal estimates
        self.team_a.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2]
        self.team_a.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
        self.team_b.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
        self.team_b.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2]

        # Create an instance of the class that contains simulateMatch
        # self.simulator = YourClassWithSimulateMatch()  # Replace with your class name
        states.GroupStageState = states.GroupStageState()

    def test_simulate_match(self):
        # Call the method under test
        match_result = self.simulator.simulateMatch(self.team_a, self.team_b)

        # Assertions to check the correct behavior
        self.team_a.set_goalsScored.assert_called_once_with(1)
        self.team_a.set_goalsConceded.assert_called_once_with(2)
        self.team_b.set_goalsScored.assert_called_once_with(2)
        self.team_b.set_goalsConceded.assert_called_once_with(1)

        # Check the points awarded (you'll need to adjust these expected values based on your logic)
        self.team_a.set_pointsEarned.assert_called_once_with(0)  # assuming loss for team_a
        self.team_b.set_pointsEarned.assert_called_once_with(3)  # assuming win for team_b

        # Verify the match result object
        self.assertIsInstance(match_result, Match)
        self.assertEqual(match_result.team_a, self.team_a)
        self.assertEqual(match_result.team_b, self.team_b)
        self.assertEqual(match_result.team_a_goals_scored, 1)
        self.assertEqual(match_result.team_b_goals_scored, 2)

if __name__ == '__main__':
    unittest.main()
