from os import environ

SESSION_CONFIGS = [
    dict(
        name='experiment',
        app_sequence=['Consent', 'instructions', 'stage1', 'stage1_complex', 'stage2', 'stage2_complex', 'stage3', 'stage3_complex',
                      'stage4', 'stage4_complex', 'results'],
        num_demo_participants=30,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['treatment', 'question_list', 'axiom_choice','all_answers',
                      'A1Q2_inconsistent','A2Q2_inconsistent','A3Q2_inconsistent',
                      'A1Q3_inconsistent','A2Q3_inconsistent','A3Q3_inconsistent', 'luck']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8330512640948'

# Added Code
DEBUG = False
ROOMS = [
    dict(
        name='group_a',
        display_name='experiment',
    ),
]