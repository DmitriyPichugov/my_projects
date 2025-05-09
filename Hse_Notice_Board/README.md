Название проекта: Hse_Notice_Board (студенческий проект)

Описание: Проект представляет собой Telegram-бота, написанного на Python с использованием библиотеки pyTelegramBotAPI (telebot).
Бот создан для того, чтобы предоставлять студентам важную информацию, расписание, ссылки на ресурсы, записи семинаров и другие
полезные материалы. Особенностью проекта является поддержка двух языков — русского и английского, что позволяет охватить как
русскоязычных, так и иностранных студентов.


Ключевые компоненты и функциональность:

Выбор языка: При старте бот предлагает пользователю выбрать язык (русский или английский).

Главное меню: После выбора языка отображается главное меню с кнопками, через которые пользователь может перейти к интересующим
разделам: расписание, записи семинаров, ресурсы для решения задач, ссылки на студенческие организации, информация о вакансиях,
ссылки на официальные сайты и обучающие курсы.

Обработка запросов: В зависимости от выбора пользователя бот отправляет сообщения с информацией и ссылками. Для отправки сообщений
используются функции с указанием параметра parse_mode='Markdown', что позволяет красиво форматировать текст и вставлять кликабельные ссылки.

Пошаговая отправка сообщений: В некоторых разделах (например, ссылки на студенческие организации или обучающие курсы) бот отправляет
несколько сообщений с небольшими задержками (time.sleep()), чтобы обеспечить удобное восприятие информации.

Целевая аудитория: Студенты ВШЭ (высшей школы экономики), обучающиеся на программах, для которых данная информация актуальна. Бот может
быть адаптирован и для других вузов или образовательных учреждений, где требуется оперативная рассылка информации и ссылки на важные ресурсы.


Преимущества проекта:

Многоязычный интерфейс: Поддержка русского и английского языков позволяет охватить широкую аудиторию.

Удобство использования: Интерактивное меню с кнопками делает навигацию по информации простой и интуитивной.

Актуальность: Бот предоставляет актуальные ссылки на расписание, записи семинаров, ресурсы для решения задач и прочую важную информацию для
студентов.

Легкость масштабирования: Добавление новых разделов или обновление информации производится легко, благодаря модульной структуре кода.

Таким образом, данный проект представляет собой функциональный Telegram-бот, ориентированный на поддержку студентов через предоставление
актуальной информации в удобном формате.
