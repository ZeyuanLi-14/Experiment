from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'stage3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    A1Q2_reconcile = models.IntegerField(
        label="You now have a chance to change your previous answers. What would you like to do? ",
        choices=[[0, 'Change my selection of the rule'], [1, 'Change my previous lottery choice to the one prescribed by the rule'], [2, 'Do not change anything']],
        widget=widgets.RadioSelectHorizontal)
    A1Q3_reconcile = models.IntegerField(
        label="You now have a chance to change your previous answers. What would you like to do? ",
        choices=[[0, 'Change my selection of the rule'],
                 [1, 'Change my previous lottery choice to the one prescribed by the rule'],
                 [2, 'Do not change anything']],
        widget=widgets.RadioSelectHorizontal)
    A2Q2_reconcile = models.IntegerField(
        label="You now have a chance to change your previous answers. What would you like to do? ",
        choices=[[0, 'Change my selection of the rule'],
                 [1, 'Change my previous lottery choice to the one prescribed by the rule'],
                 [2, 'Do not change anything']],
        widget=widgets.RadioSelectHorizontal)
    A2Q3_reconcile = models.IntegerField(
        label="You now have a chance to change your previous answers. What would you like to do? ",
        choices=[[0, 'Change my selection of the rule'],
                 [1, 'Change my previous lottery choice to the one prescribed by the rule'],
                 [2, 'Do not change anything']],
        widget=widgets.RadioSelectHorizontal)
    A3Q2_reconcile = models.IntegerField(
        label="You now have a chance to change your previous answers. What would you like to do? ",
        choices=[[0, 'Change my selection of the rule'],
                 [1, 'Change my previous lottery choice to the one prescribed by the rule'],
                 [2, 'Do not change anything']],
        widget=widgets.RadioSelectHorizontal)
    A3Q3_reconcile = models.IntegerField(
        label="You now have a chance to change your previous answers. What would you like to do? ",
        choices=[[0, 'Change my selection of the rule'],
                 [1, 'Change my previous lottery choice to the one prescribed by the rule'],
                 [2, 'Do not change anything']],
        widget=widgets.RadioSelectHorizontal)



# PAGES
class Instructions(Page):
    pass


class A1Q2_reconcile(Page):
    form_model = 'player'
    form_fields = ["A1Q2_reconcile"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.A1Q2_inconsistent
    def vars_for_template(player: Player):
        rule = f"images/A1.png"
        question_a = player.participant.question_list['A1Q2a']
        question_b = player.participant.question_list['A1Q3b']
        answer_a = player.participant.all_answers['A1Q2a']
        answer_b = player.participant.all_answers['A1Q3b']
        return dict(rule = rule, question_a = question_a, question_b = question_b,
                    answer_a = answer_a, answer_b = answer_b)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.A1Q2_reconcile == 1:
            player.participant.all_answers['A1Q2b'] = player.participant.all_answers['A1Q2a'] # change to 'correct' answer


class A1Q3_reconcile(Page):
    form_model = 'player'
    form_fields = ["A1Q3_reconcile"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.A1Q3_inconsistent
    def vars_for_template(player: Player):
        rule = f"images/A1.png"
        question_a = player.participant.question_list['A1Q3a']
        question_b = player.participant.question_list['A1Q3b']
        answer_a = player.participant.all_answers['A1Q3a']
        answer_b = player.participant.all_answers['A1Q3b']
        return dict(rule = rule, question_a = question_a, question_b = question_b,
                    answer_a = answer_a, answer_b = answer_b)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.A1Q3_reconcile == 1:
            player.participant.all_answers['A1Q3b'] = player.participant.all_answers['A1Q3a'] # change to 'correct' answer

class A2Q2_reconcile(Page):
    form_model = 'player'
    form_fields = ["A2Q2_reconcile"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.A2Q2_inconsistent
    def vars_for_template(player: Player):
        rule = f"images/A2.png"
        question_a = player.participant.question_list['A2Q2a']
        question_b = player.participant.question_list['A2Q2b']
        answer_a = player.participant.all_answers['A2Q2a']
        answer_b = player.participant.all_answers['A2Q2b']
        return dict(rule = rule, question_a = question_a, question_b = question_b,
                    answer_a = answer_a, answer_b = answer_b)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.A2Q2_reconcile == 1:
            player.participant.all_answers['A2Q2b'] = player.participant.all_answers['A2Q2a'] # change to 'correct' answer


class A2Q3_reconcile(Page):
    form_model = 'player'
    form_fields = ["A2Q3_reconcile"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.A2Q3_inconsistent
    def vars_for_template(player: Player):
        rule = f"images/A2.png"
        question_a = player.participant.question_list['A2Q3a']
        question_b = player.participant.question_list['A2Q3b']
        answer_a = player.participant.all_answers['A2Q3a']
        answer_b = player.participant.all_answers['A2Q3b']
        return dict(rule = rule, question_a = question_a, question_b = question_b,
                    answer_a = answer_a, answer_b = answer_b)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.A2Q3_reconcile == 1:
            player.participant.all_answers['A2Q3b'] = player.participant.all_answers['A2Q3a'] # change to 'correct' answer


class A3Q2_reconcile(Page):
    form_model = 'player'
    form_fields = ["A3Q2_reconcile"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.A3Q2_inconsistent
    def vars_for_template(player: Player):
        rule = f"images/A3.png"
        question_a = player.participant.question_list['A3Q2a']
        question_b = player.participant.question_list['A3Q2b']
        question_c = player.participant.question_list['A3Q2c']
        answer_a = player.participant.all_answers['A3Q2a']
        answer_b = player.participant.all_answers['A3Q2b']
        answer_c = player.participant.all_answers['A3Q2c']
        return dict(rule = rule, question_a = question_a, question_b = question_b, question_c = question_c,
                    answer_a = answer_a, answer_b = answer_b, answer_c = answer_c)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.A3Q2_reconcile == 1:
            if player.participant.all_answers['A3Q2c'] == "A":
                player.participant.all_answers['A3Q2c'] = "C"
            else:
                player.participant.all_answers['A3Q2c'] = "A"  # change to 'correct' answer


class A3Q3_reconcile(Page):
    form_model = 'player'
    form_fields = ["A3Q3_reconcile"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.A3Q3_inconsistent
    def vars_for_template(player: Player):
        rule = f"images/A3.png"
        question_a = player.participant.question_list['A3Q3a']
        question_b = player.participant.question_list['A3Q3b']
        question_c = player.participant.question_list['A3Q3c']
        answer_a = player.participant.all_answers['A3Q3a']
        answer_b = player.participant.all_answers['A3Q3b']
        answer_c = player.participant.all_answers['A3Q3c']
        return dict(rule = rule, question_a = question_a, question_b = question_b, question_c = question_c,
                    answer_a = answer_a, answer_b = answer_b, answer_c = answer_c)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.A3Q3_reconcile == 1:
            if player.participant.all_answers['A3Q3c'] == "A":
                player.participant.all_answers['A3Q3c'] = "C"
            else:
                player.participant.all_answers['A3Q3c'] = "A"  # change to 'correct' answer


class Results(Page):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return "stage4"


page_sequence = [Instructions, A1Q2_reconcile, A1Q3_reconcile, A2Q2_reconcile, A2Q3_reconcile,A3Q2_reconcile, A3Q3_reconcile, Results]
