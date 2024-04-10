from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'stage4'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    A1Q4a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B", "C"],
        widget=widgets.RadioSelectHorizontal)
    # no A1Q2b
    A2Q4a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q4b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q4a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q4b = models.StringField(
        label="Which option would you prefer?",
        choices=[["B", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A3Q4c = models.StringField(
        label="Which option would you prefer?",
        choices=[["A", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A1Q5a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B", "C"],
        widget=widgets.RadioSelectHorizontal)
    A1Q5b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q5a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A2Q5b = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q5a = models.StringField(
        label="Which option would you prefer?",
        choices=["A", "B"],
        widget=widgets.RadioSelectHorizontal)
    A3Q5b = models.StringField(
        label="Which option would you prefer?",
        choices=[["B", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)
    A3Q5c = models.StringField(
        label="Which option would you prefer?",
        choices=[["A", "A"], ["C", "B"]],
        widget=widgets.RadioSelectHorizontal)




# PAGES
class Instructions(Page):
    pass

class A1Q4a(Page):
    form_model = 'player'
    form_fields = ["A1Q4a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q4a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A1Q4a']=player.A1Q4a


class A2Q4a(Page):
    form_model = 'player'
    form_fields = ["A2Q4a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q4a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q4a']=player.A2Q4a


class A2Q4b(Page):
    form_model = 'player'
    form_fields = ["A2Q4b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q4b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q4b']=player.A2Q4b



class A3Q4a(Page):
    form_model = 'player'
    form_fields = ["A3Q4a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q4a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q4a']=player.A3Q4a


class A3Q4b(Page):
    form_model = 'player'
    form_fields = ["A3Q4b"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q4b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q4b']=player.A3Q4b


class A3Q4c(Page):
    form_model = 'player'
    form_fields = ["A3Q4c"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q4c']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q4c']=player.A3Q4c



class A1Q5a(Page):
    form_model = 'player'
    form_fields = ["A1Q5a"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q5a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A1Q5a']=player.A1Q5a


class A1Q5b(Page):
    form_model = 'player'
    form_fields = ["A1Q5b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A1Q5b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A1Q5b']=player.A1Q5b



class A2Q5a(Page):
    form_model = 'player'
    form_fields = ["A2Q5a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q5a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q5a']=player.A2Q5a


class A2Q5b(Page):
    form_model = 'player'
    form_fields = ["A2Q5b"]

    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A2Q5b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A2Q5b']=player.A2Q5b



class A3Q5a(Page):
    form_model = 'player'
    form_fields = ["A3Q5a"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q5a']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q5a']=player.A3Q5a


class A3Q5b(Page):
    form_model = 'player'
    form_fields = ["A3Q5b"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q5b']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q5b']=player.A3Q5b


class A3Q5c(Page):
    form_model = 'player'
    form_fields = ["A3Q5c"]
    @staticmethod
    def vars_for_template(player: Player):
        question = player.participant.question_list['A3Q5c']
        return dict(question=question)
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['all_answers']['A3Q5c']=player.A3Q5c


class Results(Page):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return upcoming_apps[-1]
    def before_next_page(player: Player, timeout_happened):
        import random
        # randomly select the question to be payed
        num = random.randint(0,len(player.participant.all_answers)-1)
        question_index_list = list(player.participant.question_list.keys())
        question_to_be_payed = question_index_list[num]
        # player.participant.test = [question_to_be_payed, player.participant.question_list[question_to_be_payed]]
        answer_to_be_payed = player.participant.all_answers[question_to_be_payed]
        transitivity_blist = ['A3Q1b', 'A3Q2b', 'A3Q3b', 'A3Q4b', 'A3Q5b']
        transitivity_clist = ['A3Q1c', 'A3Q2c', 'A3Q3c', 'A3Q4c', 'A3Q5c']


        # realization of lottery
        # if question_to_be_payed != A2Q3a or A2Q3a:
        # if question_to_be_payed != transitivity question
        draw = random.randint(1,100)

        if question_to_be_payed in ['A2Q3a', 'A2Q4a']:  # special case without stage 2
            if answer_to_be_payed == "A":
                if draw <= player.participant.question_list[question_to_be_payed][0][0][0]:
                    player.participant.payoff += player.participant.question_list[question_to_be_payed][0][0][1]
            else:
                if draw <= player.participant.question_list[question_to_be_payed][1][0][0]:
                    player.participant.payoff += player.participant.question_list[question_to_be_payed][1][0][1]
                else:
                    draw2 = random.randint(1, 100)
                    if draw2 <= player.participant.question_list[question_to_be_payed][3][0][0]:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][3][0][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][3][1][1]


        else:
            if (answer_to_be_payed == "A") or (
                    question_to_be_payed in transitivity_blist and answer_to_be_payed == "B"):  # adjusting for transitivity b questions
                if draw <= player.participant.question_list[question_to_be_payed][0][0][0]:
                    player.participant.payoff += player.participant.question_list[question_to_be_payed][0][0][1]
                elif draw <= player.participant.question_list[question_to_be_payed][0][0][0] + \
                        player.participant.question_list[question_to_be_payed][0][1][0]:
                    if player.participant.question_list[question_to_be_payed][0][1][1] == "Stage 2":
                        draw2 = random.randint(1, 100)
                        if draw2 <= player.participant.question_list[question_to_be_payed][3][0][0]:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][3][0][1]
                        else:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][3][1][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][0][1][1]
                else:
                    if player.participant.question_list[question_to_be_payed][0][2][1] == "Stage 2":
                        draw2 = random.randint(1, 100)
                        if draw2 <= player.participant.question_list[question_to_be_payed][3][0][0]:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][3][0][1]
                        else:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][3][1][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][0][2][1]
            elif (answer_to_be_payed == "B" and question_to_be_payed not in transitivity_blist) or (
                    answer_to_be_payed == "C" and question_to_be_payed in transitivity_blist) or (
                    answer_to_be_payed == "C" and question_to_be_payed in transitivity_clist):
                if draw <= player.participant.question_list[question_to_be_payed][1][0][0]:
                    player.participant.payoff += player.participant.question_list[question_to_be_payed][1][0][1]
                elif draw <= player.participant.question_list[question_to_be_payed][1][0][0] + \
                        player.participant.question_list[question_to_be_payed][1][1][0]:
                    if player.participant.question_list[question_to_be_payed][1][1][1] == "Stage 2":
                        draw2 = random.randint(1, 100)
                        if draw2 <= player.participant.question_list[question_to_be_payed][4][0][0]:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][4][0][1]
                        else:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][4][1][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][1][1][1]
                else:
                    if player.participant.question_list[question_to_be_payed][1][2][1] == "Stage 2":
                        draw2 = random.randint(1, 100)
                        if draw2 <= player.participant.question_list[question_to_be_payed][4][0][0]:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][4][0][1]
                        else:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][4][1][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][1][2][1]
            else:
                if draw <= player.participant.question_list[question_to_be_payed][2][0][0]:
                    player.participant.payoff += player.participant.question_list[question_to_be_payed][2][0][1]
                elif draw <= player.participant.question_list[question_to_be_payed][2][0][0] + \
                        player.participant.question_list[question_to_be_payed][2][1][0]:
                    if player.participant.question_list[question_to_be_payed][2][1][1] == "Stage 2":
                        draw2 = random.randint(1, 100)
                        if draw2 <= player.participant.question_list[question_to_be_payed][5][0][0]:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][5][0][1]
                        else:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][5][1][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][2][1][1]
                else:
                    if player.participant.question_list[question_to_be_payed][2][2][1] == "Stage 2":
                        draw2 = random.randint(1, 100)
                        if draw2 <= player.participant.question_list[question_to_be_payed][5][0][0]:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][5][0][1]
                        else:
                            player.participant.payoff += player.participant.question_list[question_to_be_payed][5][1][1]
                    else:
                        player.participant.payoff += player.participant.question_list[question_to_be_payed][2][2][1]

        luck = random.choices([1,0], weights=[1, 4])
        player.participant.luck = luck[0]
        player.participant.payoff = player.participant.payoff * luck[0]








page_sequence = [Instructions, A1Q4a, A2Q4a, A2Q4b, A3Q4a, A3Q4b, A3Q4c, A1Q5a, A1Q5b, A2Q5a, A2Q5b, A3Q5a, A3Q5b, A3Q5c, Results]
