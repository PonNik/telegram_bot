import random

msg_list = [{'message': """Ассалам Алейкум, меня зовут Гульнара, я рада приветствовать тебя на своём канале. Здесь мы халяльно зарабатываем с моими братьями👳🏻‍♂️ и сёстрами🧕🏼. Жми на кнопку снизу👇🏽 и скорее пиши мне, чтобы я рассказала тебе условия.
✨✨""", 
"btn_text": "❓Подробные условия❓", 
"url": "https://t.me/halal_adilya"}, 
            {"message": """🌙🌙🌙
🫵🏽Ты уже посмотрел мой канал❓с отзывами! Каждый день я помогаю своим братьям👳🏻‍♂️и сестрам 🧕🏼заработать вместе со мной. И каждый день они оставляют свои отзывы, которые я обязательно публикую на канале. Жми скорее на кнопку внизу👇🏽, смотри мой канал, читай отзывы и пиши мне скорее, чтобы узнать все об условиях работы со мной. Я даю каждому возможность изменить свою жизнь к лучшему по воле Всевышнего🤲🏼
🌙🌙🌙""", 
"btn_text": "✅ Перейти на канал ✅", 
"url": "https://github.com"}, 
            {"message": """🧕🏼БУДУ РАДА ТЕБЯ ПРИВЕТСТВОВАТЬ У СЕБЯ В СООБЩЕНИЯХ✨
🔽Нажми на кнопку внизу🔽""", 
"btn_text": "❓Подробные условия❓", 
"url": "https://t.me/halal_adilya"}, 
            {"message": """Здравствуйте!👋🏼
Сегодняшний день у меня начался с великолепной работы😊, я её оставила на канале. Вы просмотрели её? Получился отличный результат, а это значит, что сегодня будет прибыльный день у каждого, кто решится начать инвестировать📈💰
Жду сейчас только вас🫵🏼, чтобы начать вам зарабатывать огромные суммы!😇
Нажимайте скорее на кнопку ниже, буду ждать вас‼️👇🏼""", 
"btn_text": "❓Подробные условия❓", 
"url": "https://t.me/halal_adilya"}]


def get_rnd_message():
    return random.choice(msg_list)