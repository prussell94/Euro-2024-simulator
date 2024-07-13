from teams.team_data import teams_dict
from groups.group import Group

group_a_teams = [teams_dict.get("Germany"), teams_dict.get("Switzerland"), teams_dict.get("Scotland"), teams_dict.get("Hungary")]
group_b_teams = [teams_dict.get("Spain"), teams_dict.get("Italy"), teams_dict.get("Croatia"), teams_dict.get("Albania")]
group_c_teams = [teams_dict.get("England"), teams_dict.get("Denmark"), teams_dict.get("Serbia"), teams_dict.get("Slovenia")]
group_d_teams = [teams_dict.get("France"), teams_dict.get("Netherlands"), teams_dict.get("Austria"), teams_dict.get("Poland")]
group_e_teams = [teams_dict.get("Belgium"), teams_dict.get("Romania"), teams_dict.get("Slovakia"), teams_dict.get("Ukraine")]
group_f_teams = [teams_dict.get("Portugal"), teams_dict.get("Turkey"), teams_dict.get("Czechia"), teams_dict.get("Georgia")]

group_a = Group(group_a_teams)
group_b = Group(group_b_teams)
group_c = Group(group_c_teams)
group_d = Group(group_d_teams)
group_e = Group(group_e_teams)
group_f = Group(group_f_teams)

groups = [group_a, group_b, group_c, group_d, group_e, group_f]
groups_dict = {"A": group_a_teams, "B": group_b_teams, "C": group_c_teams, "D": group_d_teams, "E": group_e_teams, "F": group_f_teams}