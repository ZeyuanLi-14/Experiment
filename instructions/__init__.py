from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        # save the players in a local list, so the function get_players() is only executed once
        import random
        all_players = subsession.get_players()
        for player in all_players:
            participant = player.participant
            participant.treatment = random.choice([True, False])
            if participant.treatment:
                player.participant.question_list = {
                    'A1Q1a': [[(70, 0), (30, "Stage 2")], [(80, 0), (20, "Stage 2")], [(80, 0), (20, "Stage 2")],
                              [(20, 0), (80, 10)], [(80, 12), (20, 7)], [(30, 0), (70, 10)]],
                    'A1Q1b': [[(70, 0), (30, "Stage 2")], [(80, 0), (20, "Stage 2")], 'no third option',
                              [(20, 10), (80, 10)],
                              [(80, 12), (20, 7)]],
                    'A1Q2a': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], [(85, 0), (15, "Stage 2")],
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)], [(80, 12), (20, 2)]],
                    'A1Q2b': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], 'no third option',
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)]],
                    'A1Q3a': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], [(85, 0), (15, "Stage 2")],
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)], [(30, 0), (70, 10)]],
                    'A1Q3b': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], 'no third option',
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)]],
                    'A1Q4a': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], [(70, 0), (30, "Stage 2")],
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)], [(80, 10), (20, 0)]],
                    'A1Q5a': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], [(85, 0), (15, "Stage 2")],
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)], [(80, 10), (20, 0)]],
                    'A1Q5b': [[(60, 0), (40, "Stage 2")], [(80, 0), (20, "Stage 2")], 'no third option',
                              [(20, 10), (80, 5)], [(80, 12), (20, 2)]],
                    'A2Q1a': [[(80, 0), (10, 2), (10, "Stage 2")], [(80, 0), (10, 6), (10, "Stage 2")],
                              'no third option',
                              [(80, 12), (20, 2)], [(70, 10), (30, 0)]],
                    'A2Q1b': [[(80, 12), (10, 2), (10, "Stage 2")], [(80, 12), (10, 6), (10, "Stage 2")],
                              'no third option',
                              [(80, 12), (20, 2)], [(70, 10), (30, 0)]],
                    'A2Q2a': [[(80, 0), (10, 6), (10, "Stage 2")], [(80, 0), (10, 8), (10, "Stage 2")],
                              'no third option',
                              [(80, 12), (20, 7)], [(80, 10), (20, 5)]],
                    'A2Q2b': [[(40, 0), (30, 6), (30, "Stage 2")], [(40, 0), (30, 8), (30, "Stage 2")],
                              'no third option',
                              [(80, 12), (20, 7)], [(80, 10), (20, 5)]],
                    'A2Q3a': [[(100, 8)], [(20, 0), (80, "Stage 2")], 'no third option',
                              [(80, 12), (20, 4.5)]],
                    'A2Q3b': [[(75, 0), (25, "Stage 2")], [(80, 0), (20, "Stage 2")], 'no third option',
                              [(80, 10), (20, 0)], [(80, 12), (20, 4.5)]],
                    'A2Q4a': [[(100, 7)], [(20, 0), (80, "Stage 2")], 'no third option',
                              [(80, 10), (20, 7.5)]],
                    'A2Q4b': [[(40, 0), (60, "Stage 2")], [(52, 0), (48, "Stage 2")], 'no third option',
                              [(70, 10), (30, 0)], [(80, 10), (20, 7.5)]],
                    'A2Q5a': [[(70, 0), (15, 7), (15, "Stage 2")], [(70, 0), (15, 6), (15, "Stage 2")],
                              'no third option',
                              [(80, 12), (20, 2)], [(80, 10), (20, 0)]],
                    'A2Q5b': [[(50, 0), (25, 7), (25, "Stage 2")], [(50, 0), (25, 6), (25, "Stage 2")],
                              'no third option',
                              [(80, 12), (20, 2)], [(80, 10), (20, 0)]],
                    'A3Q1a': [[(5, 2), (5, 3), (90, "Stage 2")], [(10, 2), (90, "Stage 2")],
                              'no third option',
                              [(50, 8), (50, 9)], [(50, 8), (50, 9)]],
                    'A3Q1b': [[(10, 2), (10, 7), (80, "Stage 2")], [(10, 2), (90, "Stage 2")],
                              'no third option',
                              [(50, 8), (50, 9)], [(50, 8), (50, 9)]],
                    'A3Q1c': [[(10, 2), (10, 7), (80, "Stage 2")], [(5, 2), (5, 3), (10, "Stage 2")],
                              'no third option',
                              [(50, 8), (50, 9)], [(50, 8), (50, 9)]],
                    'A3Q2a': [[(6, 3), (9, 2), (85, "Stage 2")], [(7, 3), (8, 2), (85, "Stage 2")],
                              'no third option',
                              [(50, 8), (50, 7)], [(50, 8), (50, 7)]],
                    'A3Q2b': [[(6, 3), (9, 2), (85, "Stage 2")], [(2, 12), (18, 1), (80, "Stage 2")],
                              'no third option',
                              [(50, 8), (50, 7)], [(50, 8), (50, 7)]],
                    'A3Q2c': [[(7, 3), (8, 2), (85, "Stage 2")], [(2, 12), (18, 1), (80, "Stage 2")],
                              'no third option',
                              [(50, 8), (50, 7)], [(50, 8), (50, 7)]],
                    'A3Q3a': [[(10, 1), (0, 12), (90, "Stage 2")], [(7, 5), (8, 6), (85, "Stage 2")],
                              'no third option',
                              [(50, 6), (50, 7)], [(50, 6), (50, 7)]],
                    'A3Q3b': [[(12, 1), (3, 10), (85, "Stage 2")], [(0, 12), (10, 1), (90, "Stage 2")],
                              'no third option',
                              [(50, 6), (50, 7)], [(50, 6), (50, 7)]],
                    'A3Q3c': [[(12, 1), (3, 10), (85, "Stage 2")], [(7, 5), (8, 6), (85, "Stage 2")],
                              'no third option',
                              [(50, 6), (50, 7)], [(50, 6), (50, 7)]],
                    'A3Q4a': [[(5, 12), (5, 0), (90, "Stage 2")], [(6, 2), (4, 4), (90, "Stage 2")],
                              'no third option',
                              [(50, 7), (50, 8)], [(50, 7), (50, 8)]],
                    'A3Q4b': [[(14, 0), (1, 12), (85, "Stage 2")], [(6, 2), (4, 4), (90, "Stage 2")],
                              'no third option',
                              [(50, 7), (50, 8)], [(50, 7), (50, 8)]],
                    'A3Q4c': [[(5, 12), (5, 0), (90, "Stage 2")], [(14, 0), (1, 12), (85, "Stage 2")],
                              'no third option',
                              [(50, 7), (50, 8)], [(50, 7), (50, 8)]],
                    'A3Q5a': [[(5, 3), (0, 3), (95, "Stage 2")], [(8, 4), (12, 4), (80, "Stage 2")],
                              'no third option',
                              [(50, 9), (50, 8)], [(50, 9), (50, 8)]],
                    'A3Q5b': [[(8, 2), (12, 3), (80, "Stage 2")], [(8, 4), (12, 4), (80, "Stage 2")],
                              'no third option',
                              [(50, 9), (50, 8)], [(50, 9), (50, 8)]],
                    'A3Q5c': [[(5, 3), (0, 3), (95, "Stage 2")], [(8, 2), (12, 3), (80, "Stage 2")],
                              'no third option',
                              [(50, 9), (50, 8)], [(50, 9), (50, 8)]],
                }
            else:
                player.participant.question_list = {
                    'A1Q1a': [[(70, 0), (30, 8)], [(80, 0), (20, 11)], [(80, 0), (20, 7)]],
                    'A1Q1b': [[(70, 0), (30, 8)], [(80, 0), (20, 11)], 'no third option'],
                    'A1Q2a': [[(60, 0), (40, 6)], [(80, 0), (20, 10)], [(85, 0), (15, 10)]],
                    'A1Q3a': [[(60, 0), (40, 6)], [(80, 0), (20, 10)], [(85, 0), (15, 7)]],
                    'A1Q3b': [[(60, 0), (40, 6)], [(80, 0), (20, 10)], 'no third option'],
                    'A1Q4a': [[(60, 0), (40, 6)], [(80, 0), (20, 10)], [(80, 0), (20, 7)]],
                    'A1Q5a': [[(60, 0), (40, 6)], [(80, 0), (20, 10)], [(85, 0), (15, 8)]],
                    'A1Q5b': [[(60, 0), (40, 6)], [(80, 0), (20, 10)], 'no third option'],
                    'A2Q1a': [[(80, 0), (10, 2), (10, 10)], [(80, 0), (10, 6), (10, 7)], 'no third option'],
                    'A2Q1b': [[(80, 12), (10, 2), (10, 10)], [(80, 12), (10, 6), (10, 7)], 'no third option'],
                    'A2Q2a': [[(80, 0), (10, 6), (10, 11)], [(80, 0), (10, 8), (10, 9)], 'no third option'],
                    'A2Q2b': [[(40, 0), (30, 6), (30, 11)], [(40, 0), (30, 8), (30, 9)], 'no third option'],
                    'A2Q3a': [[(100, 8)], [(80, 10.5), (20, 0)], 'no third option'],
                    'A2Q3b': [[(75, 0), (25, 8)], [(80, 0), (20, 10.5)], 'no third option'],
                    'A2Q4a': [[(20, 0), (80, 9.5)], [(100, 7)], 'no third option'],
                    'A2Q4b': [[(52, 0), (48, 9.5)], [(40, 0), (60, 7)], 'no third option'],
                    'A2Q5a': [[(70, 0), (15, 7), (15, 10)], [(70, 0), (15, 6), (15, 8)], 'no third option'],
                    'A2Q5b': [[(50, 0), (25, 7), (25, 10)], [(50, 0), (25, 6), (25, 8)], 'no third option'],
                    'A3Q1a': [[(90, 7.5), (5, 2), (5, 3)], [(90, 7.5), (10, 2)], 'no third option'],
                    'A3Q1b': [[(80, 7.5), (10, 7), (10, 2)], [(90, 7.5), (10, 2)], 'no third option'],
                    'A3Q1c': [[(80, 7.5), (10, 7), (10, 2)], [(90, 7.5), (5, 2), (5, 3)], 'no third option'],
                    'A3Q2a': [[(85, 7.5), (6, 3), (9, 2)], [(85, 7.5), (7, 3), (8, 2)], 'no third option'],
                    'A3Q2b': [[(85, 7.5), (2, 12), (18, 1)], [(85, 7.5), (6, 3), (9, 2)], 'no third option'],
                    'A3Q2c': [[(85, 7.5), (7, 3), (8, 2)], [(80, 7.5), (2, 12), (18, 1)], 'no third option'],
                    'A3Q3a': [[(90, 6.5), (0, 12), (10, 1)], [(85, 6.5), (7, 5), (8, 6)], 'no third option'],
                    'A3Q3b': [[(85, 6.5), (12, 1), (3, 10)], [(90, 6.5), (0, 12), (10, 1)], 'no third option'],
                    'A3Q3c': [[(85, 6.5), (12, 1), (3, 10)], [(85, 6.5), (7, 5), (8, 6)], 'no third option'],
                    'A3Q4a': [[(90, 7.5), (5, 12), (5, 0)], [(90, 7.5), (6, 2), (4, 4)], 'no third option'],
                    'A3Q4b': [[(85, 7.5), (14, 0), (1, 12)], [(90, 7.5), (6, 2), (4, 4)], 'no third option'],
                    'A3Q4c': [[(90, 7.5), (5, 12), (5, 0)], [(85, 7.5), (14, 0), (1, 12)], 'no third option'],
                    'A3Q5a': [[(90, 8.5), (3, 9), (7, 5)], [(90, 0), (0, 12), (10, 4)], 'no third option'],
                    'A3Q5b': [[(90, 8.5), (0, 12), (10, 4)], [(90, 8.5), (9, 0), (1, 3)], 'no third option'],
                    'A3Q5c': [[(90, 8.5), (9, 0), (1, 3)], [(90, 8.5), (3, 9), (7, 5)], 'no third option'],

                }

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Instructions1(Page):
    pass


class Instructions2(Page):
    pass


class Types_of_Questions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q1a']
        return dict(question=question)

class Instructions3(Page):
    pass

class Instructions4(Page):  # last page
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q1a']
        return dict(question=question)

    def app_after_this_page(player, upcoming_apps):
        if player.participant.treatment:
            return "stage1_complex"
        else:
            return "stage1"

# class Instructions5(Page):
#     pass
#
# class Test(Page):
#     form_model = 'player'
#     form_fields = ["Test"]
#
#     @staticmethod
#     def vars_for_template(player: Player):
#         question = player.participant.question_list['A1Q1a']
#         return dict(question=question)
#     def app_after_this_page(player, upcoming_apps):
#         if player.participant.treatment:
#             return "stage1_complex"
#         else:
#             return "stage1"
# #
# class Results(Page):
#     @staticmethod
#     def app_after_this_page(player, upcoming_apps):
#         if player.participant.treatment:
#             return "stage1_complex"
#         else:
#             return "stage1"




page_sequence = [Instructions1, Instructions2,Types_of_Questions,Instructions3,Instructions4]
