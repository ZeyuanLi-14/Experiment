from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'stage1_complex'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    axiom1 = models.IntegerField(
        label="Would you like to use this rule to make decisions on your behalf in subsequent questions?",
        choices=[[1, "Yes"], [0, "No"]],
        widget=widgets.RadioSelectHorizontal)
    axiom2 = models.IntegerField(
        label="Would you like to use this rule to make decisions on your behalf in subsequent questions?",
        choices=[[1, "Yes"], [0, "No"]],
        widget=widgets.RadioSelectHorizontal)
    axiom3 = models.IntegerField(
        label="Would you like to use this rule to make decisions on your behalf in subsequent questions?",
        choices=[[1, "Yes"], [0, "No"]],
        widget=widgets.RadioSelectHorizontal)
    A1Q1a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B", "C"],
        widget=widgets.RadioSelectHorizontal)
    A1Q1b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q1a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q1b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q1a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q1b = models.StringField(
        label="Which option would you prefer?",
        choices=[["B", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A3Q1c = models.StringField(
        label="Which option would you prefer?",
        choices=[["A", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)


# PAGES
class Axiom1(Page):
    form_model = 'player'
    form_fields = ["axiom1"]


class Axiom2(Page):
    form_model = 'player'
    form_fields = ["axiom2"]


class Axiom3(Page):
    form_model = 'player'
    form_fields = ["axiom3"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.axiom_choice = [player.axiom1, player.axiom2, player.axiom3]

class Instructions1(Page):
    pass


class Instructions2(Page):
    pass


class A1Q1a(Page):
    form_model = 'player'
    form_fields = ["A1Q1a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q1a']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers = {'A1Q1a': player.A1Q1a}
        if player.axiom1 == 1:
            player.A1Q1b = player.A1Q1a  # whatever the axiom chooses for the player
            player.participant.all_answers['A1Q1b'] = player.A1Q1b


class A1Q1b(Page):
    form_model = 'player'
    form_fields = ["A1Q1b"]

    # only appears if the player does not select the axiom
    @staticmethod
    def is_displayed(player: Player):
        return player.axiom1 == 0
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q1b']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers['A1Q1b'] = player.A1Q1b


class A2Q1a(Page):
    form_model = 'player'
    form_fields = ["A2Q1a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q1a']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers['A2Q1a'] = player.A2Q1a
        if player.axiom2 == 1:
            player.A2Q1b = player.A2Q1a  # whatever the axiom chooses for the player
            player.participant.all_answers['A2Q1b'] = player.A2Q1b


class A2Q1b(Page):
    form_model = 'player'
    form_fields = ["A2Q1b"]

    # only appears if the player does not select the axiom
    @staticmethod
    def is_displayed(player: Player):
        return player.axiom2 == 0
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q1b']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers['A2Q1b'] = player.A2Q1b


class A3Q1a(Page):
    form_model = 'player'
    form_fields = ["A3Q1a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q1a']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers['A3Q1a'] = player.A3Q1a
        # if player.axiom2 == 1:
        #     player.A2Q1b = player.A2Q1a  # whatever the axiom chooses for the player
        #     player.participant.all_answers['A2Q1b'] = player.A2Q1b

class A3Q1b(Page):
    form_model = 'player'
    form_fields = ["A3Q1b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q1b']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers['A3Q1b'] = player.A3Q1b
        if player.axiom3 == 1:
            if player.A3Q1a == "A" and player.A3Q1b == "B":
                player.A3Q1c = "C"
                player.participant.all_answers['A3Q1c'] = player.A3Q1c
            elif (player.A3Q1a == player.A3Q1b == "B") or (player.A3Q1a == "A" and player.A3Q1b == "C"):
                import random
                player.A3Q1c = random.choice(["A","C"])
                player.participant.all_answers['A3Q1c'] = player.A3Q1c
            else:
                player.A3Q1c = "A"
                player.participant.all_answers['A3Q1c'] = player.A3Q1c


class A3Q1c(Page):
    form_model = 'player'
    form_fields = ["A3Q1c"]

    # only appears if the player does not select the axiom
    @staticmethod
    def is_displayed(player: Player):
        return player.axiom3 == 0
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q1c']
        return dict(question = question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.all_answers['A3Q1c'] = player.A3Q1c


class Results(Page):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return "stage2_complex"


page_sequence = [Axiom1, Axiom2, Axiom3, Instructions1, Instructions2, A1Q1a, A1Q1b, A2Q1a, A2Q1b, A3Q1a, A3Q1b, A3Q1c, Results]
