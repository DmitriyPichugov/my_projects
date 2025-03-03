import telebot
from telebot import types
import time


bot = telebot.TeleBot("7919514812:AAFTPOt2asL3YSzoOtR9N7QfPdNH9a-b_Zg")


# Стартовая команда и кнопка
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton("🇬🇧 English")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "🇷🇺 Русский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать 🔥")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Привет! Я твой бот-помошник! Если ты обучаешься в вышке на программе ПМИ в группе БПМИИ2411, то здесь ты можешь узнать важную информацию, расписание пар и получить все ссылки, которые могут тебе понадобиться!)", reply_markup=markup)
    elif message.text == "🇬🇧 English":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Start 🔥")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Hello! I am your assistant bot! If you are studying in HSE in the PMI program, you can find important information here, class schedules, and get all the links you might need!", reply_markup=markup)

    if message.text == 'Начать 🔥':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Создание новых кнопок
        btn1 = types.KeyboardButton('📆 Расписание')
        btn2 = types.KeyboardButton('🎥 Записи семинаров')
        btn3 = types.KeyboardButton('💻 Где решать задачи')
        btn4 = types.KeyboardButton('🌐 Студ. организации и другое')
        btn5 = types.KeyboardButton('💰 Ради чего мы сражаемся')
        btn6 = types.KeyboardButton('🧾 Wiki ФКН')
        btn7 = types.KeyboardButton('🧠 Smart LMS')
        btn8 = types.KeyboardButton('📎 Официальный сайт вышки')
        btn9 = types.KeyboardButton('💡 Курсы по машинному обучению и llm')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, '❓ Выбери интересующий тебя раздел информации', reply_markup=markup) # Ответ бота

    elif message.text == '📆 Расписание':
        bot.send_message(message.from_user.id, 'Отправляю вам exel таблицу с расписанием для 1-2 курсов направлений ПМИ/ЭАД 1 модуль 24-25. \
            ' + '[ссылка](https://docs.google.com/spreadsheets/d/1wm1Kv2lvdlU0MWsDm-DXOiBDOsuHWHtBc4x35TDttbQ/edit?gid=812790909#gid=812790909)', parse_mode='Markdown')

    elif message.text == '🎥 Записи семинаров':
        bot.send_message(message.from_user.id, 'Отправляю вам яндекс диск со всеми записями семинаров по дискретной математике \
            (Преподаватель: Валинкин), линейной алгебре и геометрии (Преподаватель: Игнатьев),\
                математическому анализу (Преподаватели: Ожегов, Мажуга). \n\
' + '[ссылка](https://disk.yandex.ru/d/GJF8OqXLMQWWaw)', parse_mode='Markdown')

    elif message.text == '💻 Где решать задачи':
        bot.send_message(message.from_user.id, 'Leetcode: ' +\
            '[ссылка](https://leetcode.com/problemset)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Codeforces: ' +\
            '[ссылка](https://codeforces.com/problemset)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'CodeRun: ' +\
            '[ссылка](https://coderun.yandex.ru/catalog)', parse_mode='Markdown')
    
    elif message.text == '🌐 Студ. организации и другое':
        bot.send_message(message.from_user.id, 'Волонтёры ФКН: ' +\
            '[ссылка](https://t.me/volunteer_fcs)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'EXTRA: ' +\
            '[ссылка](https://extra.hse.ru)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'CSTATI: ' +\
            '[ссылка](https://t.me/cstati_hse)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Движ: ' +\
            '[ссылка](https://t.me/ami_fun)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Movement: ' +\
            '[ссылка](https://m.vk.com/movement_hse)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Карьера: ' +\
            '[ссылка](https://t.me/hsemarathon)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Женщины в IT: ' +\
            '[ссылка](https://women-in-tech.ru)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Спорт в ВШЭ: ' +\
            '[ссылка](sport.hse.ru)', parse_mode='Markdown')
    
    elif message.text == '💰 Ради чего мы сражаемся':
        bot.send_message(message.from_user.id, 'Задачи за вознаграждение: ' +\
            '[ссылка](https://docs.google.com/spreadsheets/d/1WKHbT-7KOgjEawq5h5Ic1qUWzpfAzuD_J06N1JwOCGs/edit?gid=0#gid=0)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Критика резюме: ' +\
            '[ссылка](https://t.me/resume_review)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Канал с вакансиями: ' +\
            '[ссылка](https://t.me/not_boring_ds_jobs)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Задачи Яндекс собесов: ' +\
            '[ссылка](https://disk.yandex.ru/d/hoNm3hNSdUw4gA)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Я.Jobs: ' +\
            '[ссылка](https://yandex.ru/jobs)', parse_mode='Markdown')
    
    elif message.text == '🧾 Wiki ФКН':
        bot.send_message(message.from_user.id, 'Wiki ФКН: ' +\
            '[ссылка](http://wiki.cs.hse.ru/Wiki_%D0%A4%D0%9A%D0%9D)', parse_mode='Markdown')
        
    elif message.text == '🧠 Smart LMS':
        bot.send_message(message.from_user.id, 'Smart LMS: ' +\
            '[ссылка](https://edu.hse.ru/my/courses.php)', parse_mode='Markdown')
    
    elif message.text == '📎 Официальный сайт вышки':
        bot.send_message(message.from_user.id, 'Официальный сайт вышки: ' +\
            '[ссылка](https://www.hse.ru/)', parse_mode='Markdown')
    
    elif message.text == '💡 Курсы по машинному обучению и llm':
        bot.send_message(message.from_user.id, ' 1️⃣ Гайдбук по оценке больших языковых моделей от Hugging Face: \n\n\
В нем собраны различные способы оценки модели, руководства по разработке собственных оценок, а также советы и рекомендации из практического \
опыта🫥. В руководстве рассказывается о разных способах оценки: с помощью автоматических тестов, людей или других моделей. \n\n\
Особое внимание уделяется тому, как избежать проблем с инференсом модели🌟 и сделать результаты одинаковыми. В руководстве есть советы о том, \
как сделать данные чистыми, как использовать шаблоны для общения с LLM и как анализировать неожиданные плохие результаты.\n' +\
            '[ссылка](https://github.com/huggingface/evaluation-guidebook)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, ' 2️⃣ ML System Design: \n\
Один из лучших курсов по ML для тех, кто уже познал многие технологии, но при этом хочет структурировать свои знания и правильно их оформить, \
при этом попробовать это в бизнесе⚜️.\n' +\
            '[ссылка](https://ods.ai/tracks/ml-system-design-23)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, ' 3️⃣ Курс по генеративному ИИ от Microsoft: Довольно интересный курс для начинающих, \
в котором обсуждаются такие интересные темы, как векторные базы данных, rag, промптинг и агенты📊.\n' +\
            '[ссылка](https://github.com/microsoft/generative-ai-for-beginners?tab=readme-ov-file)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, ' 4️⃣ Курс по huggingface и его возможностях: Главы с 1 по 4 знакомят с основными концепциями \
библиотеки Transformers🫡, с 5 по 8 знакомят с основами Datasets и Tokenizers, прежде чем погрузиться в классические задачи NLP💪, а с 9 по 12 \
выходят за рамки NLP и изучают, как модели Transformer можно использовать для решения задач обработки речи и компьютерного зрения🤓.\n' +\
            '[ссылка](https://huggingface.co/learn/nlp-course/chapter1/1)', parse_mode='Markdown')
        
    if message.text == "Start 🔥":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #Создание новых кнопок
        btn1 = types.KeyboardButton('📆 Schedule')
        btn2 = types.KeyboardButton('🎥 Seminar Recordings')
        btn3 = types.KeyboardButton('💻 Where to Solve Problems')
        btn4 = types.KeyboardButton('🌐 Student Organizations and More')
        btn5 = types.KeyboardButton('💰 What We Fight For')
        btn6 = types.KeyboardButton('🧾 Wiki FCS')
        btn7 = types.KeyboardButton('🧠 Smart LMS ')
        btn8 = types.KeyboardButton('📎 Official HSE Website')
        btn9 = types.KeyboardButton('💡 ML and LLM Courses') # Ответ бота
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, '❓ Choose the section you are interested in', reply_markup=markup)

    elif message.text == '📆 Schedule':
        bot.send_message(message.from_user.id, 'I am sending you an exel table with a schedule for 1-2 courses in the PMI/EAD directions, \
1 module 24-25. \
            ' + '[link](https://docs.google.com/spreadsheets/d/1wm1Kv2lvdlU0MWsDm-DXOiBDOsuHWHtBc4x35TDttbQ/edit?gid=812790909#gid=812790909)', parse_mode='Markdown')

    elif message.text == '🎥 Seminar Recordings':
        bot.send_message(message.from_user.id, 'I am sending you a Yandex disk with all the recordings of seminars on discrete mathematics \
(Teacher: Valinkin), linear algebra and geometry (Teacher: Ignatiev), mathematical analysis (Teachers: Ozhegov, Mazhuga). \n\
' + '[link](https://disk.yandex.ru/d/GJF8OqXLMQWWaw)', parse_mode='Markdown')

    elif message.text == '💻 Where to Solve Problems':
        bot.send_message(message.from_user.id, 'Leetcode: ' +\
            '[link](https://leetcode.com/problemset)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Codeforces: ' +\
            '[link](https://codeforces.com/problemset)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'CodeRun: ' +\
            '[link](https://coderun.yandex.ru/catalog)', parse_mode='Markdown')
    
    elif message.text == '🌐 Student Organizations and More':
        bot.send_message(message.from_user.id, 'Volunteers FCS: ' +\
            '[link](https://t.me/volunteer_fcs)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'EXTRA: ' +\
            '[link](https://extra.hse.ru)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'CSTATI: ' +\
            '[link](https://t.me/cstati_hse)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Motion: ' +\
            '[link](https://t.me/ami_fun)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Movement: ' +\
            '[link](https://m.vk.com/movement_hse)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Career: ' +\
            '[link](https://t.me/hsemarathon)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Womens in IT: ' +\
            '[link](https://women-in-tech.ru)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Sport in HSE: ' +\
            '[link](sport.hse.ru)', parse_mode='Markdown')
    
    elif message.text == '💰 What We Fight For':
        bot.send_message(message.from_user.id, 'Reward tasks: ' +\
            '[link](https://docs.google.com/spreadsheets/d/1WKHbT-7KOgjEawq5h5Ic1qUWzpfAzuD_J06N1JwOCGs/edit?gid=0#gid=0)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Resume criticism: ' +\
            '[link](https://t.me/resume_review)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Jobs channel: ' +\
            '[link](https://t.me/not_boring_ds_jobs)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Tasks of Yandex interviews: ' +\
            '[link](https://disk.yandex.ru/d/hoNm3hNSdUw4gA)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Y.Jobs: ' +\
            '[link](https://yandex.ru/jobs)', parse_mode='Markdown')
    
    elif message.text == '🧾 Wiki FCS':
        bot.send_message(message.from_user.id, 'Wiki FCS: ' +\
            '[link](http://wiki.cs.hse.ru/Wiki_%D0%A4%D0%9A%D0%9D)', parse_mode='Markdown')
        
    elif message.text == '🧠 Smart LMS ':
        bot.send_message(message.from_user.id, 'Smart LMS: ' +\
            '[link](https://edu.hse.ru/my/courses.php)', parse_mode='Markdown')
    
    elif message.text == '📎 Official HSE Website':
        bot.send_message(message.from_user.id, 'Official HSE Website: ' +\
            '[link](https://www.hse.ru/)', parse_mode='Markdown')
    
    elif message.text == '💡 ML and LLM Courses':
        bot.send_message(message.from_user.id, ' 1️⃣ A guide to evaluating large language models from Hugging Face: \n\n\
It contains various ways to evaluate a model, guidelines for developing your own estimates, and tips and tricks from practical experience🫥. \
The guide explains different assessment methods: using automated tests, humans or other models. \n\n\
Particular attention is paid to how to avoid problems with model inference🌟 and make the results the same. The manual contains tips on how to, \
how to make data clean, how to use patterns to communicate with LLMs, and how to analyze unexpected bad results.\n' +\
            '[link](https://github.com/huggingface/evaluation-guidebook)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, ' 2️⃣ ML System Design: \n\
One of the best ML courses for those who have already learned many technologies, but at the same time want to structure their knowledge and \
format it correctly, try it in business⚜️.\n' +\
            '[link](https://ods.ai/tracks/ml-system-design-23)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, " 3️⃣ Microsoft's Generative AI Course: A Quite Interesting Course for Beginners, \
which discusses interesting topics such as vector databases, rags, prompting and agents📊.\n" +\
            '[link](https://github.com/microsoft/generative-ai-for-beginners?tab=readme-ov-file)', parse_mode='Markdown')
        time.sleep(1)
        bot.send_message(message.from_user.id, ' 4️⃣ A course on "huggingface" and its capabilities: Chapters 1 to 4 introduce the basic concepts \
of the "Transformers" library🫡, 5 to 8 introduce the basics of "Datasets" and "Tokenizers" before diving into classic NLP tasks💪, \
and from 9 to 12 go beyond NLP and explore how Transformer models can be used to solve speech processing and computer vision problems🤓.\n' +\
            '[link](https://huggingface.co/learn/nlp-course/chapter1/1)', parse_mode='Markdown')


# Строка для исправной, непрервыной работы бота
bot.polling(none_stop=True, interval=0)