from matches import match
from teams import team
import states
import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock


class TestSimulateMatch(unittest.TestCase):

    # def setUp(self):
    #     self.state = states.GroupStageState()
    #     self.original_match = Mock(spec=match.Match)

    #     self.team_a = Mock(spec=team.Team)
    #     self.team_b = Mock(spec=team.Team)

    #     self.team_a.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2]
    #     self.team_a.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
        
    #     self.team_b.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
    #     self.team_b.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2]

    def setUp(self):
        # Create mock objects for Team
        self.team_a = MagicMock(spec=team.Team)
        self.team_b = MagicMock(spec=team.Team)

        # Set up mock return values for goal estimates
        self.team_a.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2]
        self.team_a.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
        self.team_b.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
        self.team_b.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2]

        # Mock methods to return specific values
        self.team_a.set_goalsScored = MagicMock()
        self.team_a.set_goalsConceded = MagicMock()
        self.team_a.set_pointsEarned = MagicMock()
        self.team_b.set_goalsScored = MagicMock()
        self.team_b.set_goalsConceded = MagicMock()
        self.team_b.set_pointsEarned = MagicMock()

        self.original_match = Mock(spec=match.Match)

        # Create an instance of the class that contains simulateMatch
        # self.simulator = states.GroupStageState()  # Replace with your class instance
        self.state = states.GroupStageState()


    # def setUp(self):
    #     # Initialize the state object
    #     self.state = states.GroupStageState()

    #     # Create mock teams
    #     self.team_a = Mock(spec=team.Team)
    #     self.team_b = Mock(spec=team.Team)

    #     # Mock the offensive and defensive quality distributions
    #     self.team_a.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2.5]
    #     self.team_a.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1.5]
        
    #     self.team_b.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1.8]
    #     self.team_b.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [2.2]

    #     # Mock methods for setting goals scored, conceded, and points earned
    #     self.team_a.set_goalsScored = 2
    #     self.team_a.set_goalsConceded = 1
    #     self.team_a.set_pointsEarned = 3

    #     self.team_b.set_goalsScored = 1
    #     self.team_b.set_goalsConceded = 2
    #     self.team_b.set_pointsEarned = 0

    #     self.team_a.get_goalsScored.return_value = 1
    #     self.team_a.get_goalsConceded.return_value = 2
    #     self.team_b.get_goalsScored.return_value = 2
    #     self.team_b.get_goalsConceded.return_value = 1

    #     # home_team_goals.return_value = 2
    #     # away_team_goals.return_value = 1

    #     # Mock match object
    #     self.original_match = Mock(spec=match.Match)
        
    def test_simulate_match(self):
        # Call the method under test
        match_result = self.state.simulate_match(self.team_a, self.team_b, self.original_match)

        # Assertions to check the correct behavior
        self.team_a.set_goalsScored.assert_called_once_with(1)
        self.team_a.set_goalsConceded.assert_called_once_with(2)
        self.team_b.set_goalsScored.assert_called_once_with(2)
        self.team_b.set_goalsConceded.assert_called_once_with(1)

        # Check the points awarded (adjust expected values based on logic)
        self.team_a.set_pointsEarned.assert_called_once_with(0)  # assuming loss for team_a
        self.team_b.set_pointsEarned.assert_called_once_with(3)  # assuming win for team_b

        # Verify the match result object
        self.assertIsInstance(match_result, Match)
        self.assertEqual(match_result.team_a, self.team_a)
        self.assertEqual(match_result.team_b, self.team_b)
        self.assertEqual(match_result.team_a_goals_scored, 1)
        self.assertEqual(match_result.team_b_goals_scored, 2)

    # def test_simulate_match(self):
    #     # Simulate the match
    #     match_result = self.state.simulate_match(self.team_a, self.team_b, self.original_match)

    #     # Verify that goals scored/conceded were set correctly
    #     self.team_a.set_goalsScored.assert_called_with(2)
    #     self.team_a.set_goalsConceded.assert_called_with(2)
    #     self.team_b.set_goalsScored.assert_called_with(2)
    #     self.team_b.set_goalsConceded.assert_called_with(2)

    #     # Verify that points were awarded based on the match result
    #     self.team_a.set_pointsEarned.assert_called()
    #     self.team_b.set_pointsEarned.assert_called()

    #     # Check that the match result has the expected winner
    #     self.assertEqual(match_result.winner, self.team_a.get_countryName() if 2 > 2 else self.team_b.get_countryName())

    # def test_simulate_match_impl(self):
    #     # Simulate the implementation details
    #     match_result = self.state.simulate_match_impl(self.team_a, self.team_b, self.original_match)

    #     # Verify that the match result was updated correctly
    #     self.assertEqual(match_result.team_a, self.team_a)
    #     self.assertEqual(match_result.team_b, self.team_b)
    #     self.assertEqual(match_result.team_a_goals_scored, 2)
    #     self.assertEqual(match_result.team_b_goals_scored, 2)
    #     self.assertEqual(match_result.winner, self.team_a.get_countryName() if 2 > 2 else self.team_b.get_countryName())

    # def test_simulate_match(self):
    #     match_result = self.match.simulateMatch(self.team_a, self.team_b)
        
    #     self.assertIsInstance(match_result, match.Match)
    #     self.assertEqual(match_result.team_a, self.team_a)
    #     self.assertEqual(match_result.team_b, self.team_b)
    #     self.assertEqual(match_result.team_a_goals, 2)
    #     self.assertEqual(match_result.team_b_goals, 1)

    #     self.team_a.set_goalsScored.assert_called_with(2)
    #     self.team_a.set_goalsConceded.assert_called_with(1)
    #     self.team_b.set_goalsScored.assert_called_with(1)
    #     self.team_b.set_goalsConceded.assert_called_with(2)

    #     self.team_a.set_pointsEarned.assert_called_with(3) 
    #     self.team_b.set_pointsEarned.assert_called_with(0) 

    # def test_simulate_draw(self):
    #     self.team_a.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
    #     self.team_a.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]

    #     self.team_b.get_offensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]
    #     self.team_b.get_defensiveQualityDistribution.return_value.get_goal_estimate.return_value = [1]

    #     match_result = self.match.simulateMatch(self.team_a, self.team_b)
        
    #     self.assertEqual(match_result.team_a_goals, 1)
    #     self.assertEqual(match_result.team_b_goals, 1)
        
    #     self.team_a.set_pointsEarned.assert_called_with(1)
    #     self.team_b.set_pointsEarned.assert_called_with(1)

if __name__ == '__main__':
    unittest.main()