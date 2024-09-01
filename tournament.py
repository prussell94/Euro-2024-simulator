from knockouts import knockout_match
from states import TournamentState, RoundOf16State, QuarterFinalsState, SemiFinalsState, FinalsState, GroupStageState
import states
import tournament
import knockouts
from teams.team_data import teams_dict

class Tournament():
    
    def __init__(self, group_stage, knockout_bracket):
        # Initialize with the starting state Group Stage
        self._group_stage = group_stage
        self._knockout_bracket = knockout_bracket
        self._teams = teams_dict
        self.state = GroupStageState()
    
        self.state.set_context(self)

    def set_state(self, state):
        """Set the current state of the tournament."""
        self.state = state
        self.state.set_context(self)

    def simulate_round(self):
        """Simulate the current round and transition to the next state."""
        if self.state:
            self.state.simulate_round(self)

    def transition_to(self, new_state):
        """Transition to a new state."""
        self.set_state(new_state)

    # def display_results(self):
    #     self.knockout_bracket.

    def get_group_stage(self):
        return self._group_stage
    def get_knockout_bracket(self):
        print("getting knockout bracket ----- ")
        return self._knockout_bracket
    
    def get_teams(self):
        return self._teams

    def set_group_stage(self, group_stage):
        self._group_stage = group_stage
    
    def set_knockout_bracket(self, knockout_bracket):
        self._knockout_bracket = knockout_bracket

    def set_teams(self, new_teams):
        self._teams = new_teams

    def next_state(self, tournament):
        pass

    def simulate_tournament(self):
        group_stage = states.GroupStageState()
        round_of_16 = states.RoundOf16State()
        quarter_finals = states.QuarterFinalsState()
        semi_finals = states.SemiFinalsState()
        finals = states.FinalsState()

        new_tournament = tournament.Tournament(group_stage, self._knockout_bracket)

        group_stage_results = group_stage.simulate_round(tournament=new_tournament)

    # knockouts.knockout_match_data.knockout_bracket
        round_of_16.simulate_round(tournament=new_tournament)
        quarter_finals.simulate_round(tournament=new_tournament)
        semi_finals.simulate_round(tournament=new_tournament)
        knockout_bracket_final = finals.simulate_round(tournament=new_tournament)

        return group_stage_results, knockout_bracket_final, self.get_teams()
