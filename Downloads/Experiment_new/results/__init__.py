from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="What is your age?", min=18, max=125)
    gender = models.StringField(label="What is your gender? ", choices=["Male", 'Female', 'Other'],
                                widget=widgets.RadioSelectHorizontal)
    income = models.StringField(label="What is your total annual income? ",
                                choices=["Under $10,000", '$10,000 ~ $29,999', '$30,000 ~ $49,999', '$50,000 ~ $79,999',
                                         "$80,000 or above"], widget=widgets.RadioSelectHorizontal)
    race = models.StringField(label="Please choose your race. ",
                              choices=["White", 'Black or African American', 'Asian', 'Hispanic or Latino', 'Other'],
                              widget=widgets.RadioSelectHorizontal)
    education = models.StringField(label="What is your highest level of education? ",
                                   choices=['No formal education', 'Primary School', 'High School', 'Bachelors Degree',
                                            'Masters Degree', 'PhD'], widget=widgets.RadioSelectHorizontal)
    # employment = models.StringField(label="What is your current employment status? ",
    #                                 choices=["?"])
    earned = models.IntegerField(label = "Final Payoff for each player")
    luck = models.IntegerField(label = "Whether the player got the extra bonus")


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


# class Results(Page):
#     @staticmethod
#     def vars_for_template(player: Player):
#         payoff = player.participant.payoff + 3
#         return dict(payoff=payoff)

class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'race', 'income', 'education']
    def before_next_page(player: Player, timeout_happened):
        player.participant.payoff += 3
        player.earned = int(player.participant.payoff)
        player.luck = player.participant.luck

class Finished(Page):
    pass


page_sequence = [Survey, Finished]
