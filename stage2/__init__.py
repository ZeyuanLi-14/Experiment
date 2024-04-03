from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'stage2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    A1Q2a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B", "C"],
        widget=widgets.RadioSelectHorizontal)
    # no A1Q2b
    A2Q2a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q2b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q2a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q2b = models.StringField(
        label="Which option would you prefer?",
        choices=[["B", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A3Q2c = models.StringField(
        label="Which option would you prefer?",
        choices=[["A", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A1Q3a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B", "C"],
        widget=widgets.RadioSelectHorizontal)
    A1Q3b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q3a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q3b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q3a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q3b = models.StringField(
        label="Which option would you prefer?",
        choices=[["B", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A3Q3c = models.StringField(
        label="Which option would you prefer?",
        choices=[["A", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)




# PAGES
class Instructions(Page):
    pass

class A1Q2a(Page):
    form_model = 'player'
    form_fields = ["A1Q2a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q2a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A1Q2a']=player.A1Q2a


class A2Q2a(Page):
    form_model = 'player'
    form_fields = ["A2Q2a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q2a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q2a']=player.A2Q2a


class A2Q2b(Page):
    form_model = 'player'
    form_fields = ["A2Q2b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q2b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q2b']=player.A2Q2b
        if player.A2Q2a != player.A2Q2b and player.participant.axiom_choice[1] == 1:  # whatever the axiom considers to be the correct answer, and if the player selected the axiom
            player.participant.A2Q2_inconsistent = True
        else:
            player.participant.A2Q2_inconsistent = False


class A3Q2a(Page):
    form_model = 'player'
    form_fields = ["A3Q2a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q2a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q2a']=player.A3Q2a


class A3Q2b(Page):
    form_model = 'player'
    form_fields = ["A3Q2b"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q2b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q2b']=player.A3Q2b


class A3Q2c(Page):
    form_model = 'player'
    form_fields = ["A3Q2c"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q2c']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q2c']=player.A3Q2c
        if player.A3Q2c != player.A3Q2a and player.A3Q2c != player.A3Q2b and player.A3Q2a != player.A3Q2b and player.participant.axiom_choice[2] == 1:  # whatever the axiom considers to be the correct answer, and if the player selected the axiom
            player.participant.A3Q2_inconsistent = True
        else:
            player.participant.A3Q2_inconsistent = False


class A1Q3a(Page):
    form_model = 'player'
    form_fields = ["A1Q3a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q3a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A1Q3a']=player.A1Q3a


class A1Q3b(Page):
    form_model = 'player'
    form_fields = ["A1Q3b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q3b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A1Q2b'] = player.A1Q3b
        player.participant.vars['all_answers']['A1Q3b'] = player.A1Q3b
        if player.A1Q2a != "C" and player.A1Q3b != player.A1Q2a and player.participant.axiom_choice[0] == 1:  # whatever the axiom considers to be the correct answer, and if the player selected the axiom
            player.participant.A1Q2_inconsistent = True
        else:
            player.participant.A1Q2_inconsistent = False
        if player.A1Q3a != "C" and player.A1Q3b != player.A1Q3a and player.participant.axiom_choice[0] == 1:  # whatever the axiom considers to be the correct answer, and if the player selected the axiom
            player.participant.A1Q3_inconsistent = True
        else:
            player.participant.A1Q3_inconsistent = False


class A2Q3a(Page):
    form_model = 'player'
    form_fields = ["A2Q3a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q3a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q3a']=player.A2Q3a


class A2Q3b(Page):
    form_model = 'player'
    form_fields = ["A2Q3b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q3b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q3b']=player.A2Q3b
        if player.A2Q3a != player.A2Q3b and player.participant.axiom_choice[1] == 1:  # whatever the axiom considers to be the correct answer, and if the player selected the axiom
            player.participant.A2Q3_inconsistent = True
        else:
            player.participant.A2Q3_inconsistent = False


class A3Q3a(Page):
    form_model = 'player'
    form_fields = ["A3Q3a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q3a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q3a']=player.A3Q3a


class A3Q3b(Page):
    form_model = 'player'
    form_fields = ["A3Q3b"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q3b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q3b']=player.A3Q3b


class A3Q3c(Page):
    form_model = 'player'
    form_fields = ["A3Q3c"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q3c']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q3c']=player.A3Q3c
        if player.A3Q3c != player.A3Q3a and player.A3Q3c != player.A3Q3b and player.A3Q3a != player.A3Q3b and player.participant.axiom_choice[2] == 1:  # whatever the axiom considers to be the correct answer, and if the player selected the axiom
            player.participant.A3Q3_inconsistent = True
        else:
            player.participant.A3Q3_inconsistent = False


class Results(Page):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if player.participant.A1Q2_inconsistent == player.participant.A1Q3_inconsistent == player.participant.A2Q2_inconsistent == player.participant.A2Q3_inconsistent == player.participant.A3Q2_inconsistent == player.participant.A3Q3_inconsistent == False:
            return "stage4"
        else:
            return 'stage3'


page_sequence = [Instructions, A1Q2a, A2Q2a, A2Q2b, A3Q2a, A3Q2b, A3Q2c, A1Q3a, A1Q3b, A2Q3a, A2Q3b, A3Q3a, A3Q3b, A3Q3c, Results]
