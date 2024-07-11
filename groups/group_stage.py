import groups.group
import groups.groups_data

class GroupStage():
    """
    A class representing the group stage

    Attributes:
        group_a (group): group A
        group_b (group): group B
        group_c (group): group C
        group_d (group): group D
        group_e (group): group E
        group_f (group): group F
    """
    def __init__(self, group_a=groups.groups_data.group_a, group_b=groups.groups_data.group_b,
                  group_c=groups.groups_data.group_c, group_d=groups.groups_data.group_d,
                    group_e=groups.groups_data.group_e, group_f=groups.groups_data.group_f):

        """
        Initialize a new group stage instance.

        Args:
            group_a (group): group A
            group_b (group): group B
            group_c (group): group C
            group_d (group): group D
            group_e (group): group E
            group_f (group): group F
        """
        self._groupA = group_a
        self._groupB = group_b
        self._groupC = group_c
        self._groupD = group_d
        self._groupE = group_e
        self._groupF = group_f

    def assign_group_placement(self, row):
        return row['Group']+str(row['Placement'])
    
    # def simulate_group_stage():
    #     print("group stage")

    def simulate_group_stage(self):
        """
        Simulates entire group stage

        Returns:
            list of results for each group
        """
        # group_a = groups_data.group_a
        result_a = self._groupA.simulate_group()
        result_b = self._groupB.simulate_group()
        result_c = self._groupC.simulate_group()
        result_d = self._groupD.simulate_group()
        result_e = self._groupE.simulate_group()
        result_f = self._groupF.simulate_group()

        # group_c = groups.group_c()
        # result_c = group_c.simulate_group()
        # group_d = groups.group_d()
        # result_d = group_d.simulate_group()
        # group_e = groups.group_e()
        # result_e = group_e.simulate_group()
        # group_f = groups.group_f()
        # result_f = group_f.simulate_group()
        # result_a = groups.group.simulate_group(self.group_a)
        # result_b = groups.group.simulate_group(self.group_b)
        # result_c = groups.group.simulate_group(self.group_c)
        # result_d = groups.group.simulate_group(self.group_d)
        # result_e = groups.group.simulate_group(self.group_e)
        # result_f = groups.group.simulate_group(self.group_f)

        result_a["Group"]="A"
        result_b["Group"]="B"
        result_c["Group"]="C"
        result_d["Group"]="D"
        result_e["Group"]="E"
        result_f["Group"]="F"

        result_a['GroupPlacement'] =result_a.apply(lambda row: self.assign_group_placement(row), axis=1)
        result_b['GroupPlacement'] =result_b.apply(lambda row: self.assign_group_placement(row), axis=1)
        result_c['GroupPlacement'] =result_c.apply(lambda row: self.assign_group_placement(row), axis=1)
        result_d['GroupPlacement'] =result_d.apply(lambda row: self.assign_group_placement(row), axis=1)
        result_e['GroupPlacement'] =result_e.apply(lambda row: self.assign_group_placement(row), axis=1)
        result_f['GroupPlacement'] =result_f.apply(lambda row: self.assign_group_placement(row), axis=1)

        results = [result_a, result_b, result_c, result_d, result_e, result_f]
        return results
    
    def calculate_third_place_qualifiers(group_stage_tables):
        """
        Calculates the table that ranks all third placed teams

        Args:
            group_stage_tables (list): list of group tables

        Returns:
            third_place_table (DataFrame): Ranking of third place finishers
        """
        third_place_a=group_stage_tables[0][group_stage_tables[0]['Placement']==3]
        third_place_a['group']="A"
        third_place_b=group_stage_tables[1][group_stage_tables[1]['Placement']==3]
        third_place_b['group']="B"
        third_place_c=group_stage_tables[2][group_stage_tables[2]['Placement']==3]
        third_place_c['group']="C"
        third_place_d=group_stage_tables[3][group_stage_tables[3]['Placement']==3]
        third_place_d['group']="D"
        third_place_e=group_stage_tables[4][group_stage_tables[4]['Placement']==3]
        third_place_e['group']="E"
        third_place_f=group_stage_tables[5][group_stage_tables[5]['Placement']==3]
        third_place_f['group']="F"

        third_place_table=pd.concat([third_place_a, third_place_b, third_place_c, third_place_d, third_place_e, third_place_f])
        third_place_table['Goal Differential']=third_place_table['Goals Scored']-third_place_table['Goals Conceded']

        third_place_table.sort_values(by=['Points', 'Goal Differential', 'Goals Scored'], 
                           ascending=[False, False, False], inplace=True)
        return third_place_table
