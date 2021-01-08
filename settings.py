GROUP_ID = 124866462

TOKEN = '9536a9498f271692fd55be5d8c54111d314394b07b5b0854846eaf82073c5734d453c5729d15d955e5114'

INTENTS = [
    {
        'name': 'Дата проведение',
        'tokens': ('когда', 'сколько', 'дата', 'дату'),
        'scenario': None,
        'answer': 'Тур состоится 9-го октября, отправлнение в 10 утра'
    },
    {
        'name': 'Место проведения',
        'tokens': ('где', 'место', 'локация', 'адрес', 'метро'),
        'scenario': None,
        'answer': 'Концерт пройдет в Крокус-Экспо / Москва \n'
                  'Отправление автобуса с площади Минина / Нижний Новгород'
    },
    {
        'name': 'Регистрация',
        'tokens': ('регист', 'добав'),
        'scenario': 'registration',
        'answer': None
    }
]

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Чтобы зарегестрироваться введите ваше имя.',
                'failure_text': 'Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз.',
                'handler': 'handle_name',
                'next_step': 'step2'
            },
            'step2':{
                'text': 'Введите email. Мы отправим на него билет.',
                'failure_text': 'Во введенном адресе ошибка. Попробуйте еще раз.',
                'handler': 'handle_email',
                'next_step': 'step3'
            },
            'step3':{
                'text': 'Спасибо за регистрацию, {name}! Ваш билет ниже, распечатайте его. Копию мы отправили на {email}',
                'image': 'generate_ticket_handler',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю как на это ответить. ' \
    'Могу сказать когда и где пройдет конференция, а также зарегестрировать вас. Просто спросите.'


DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    host='localhost',
    database='vk_chat_bot'
    )