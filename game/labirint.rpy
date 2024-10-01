#NPC
define bikov = Character('Бычек', color="#5b5e09")

define arkahaIsAlive = True
define nikitaIsAlive = True

init python:
    class Question:
        def __init__(self, text, correct, *variants):
            if len(variants) != 4:
                raise Exception("Должно быть 4 варианта ответа")
            self.text = text
            self.correct = correct - 1
            self.variants = variants

define questions = (
    Question(_('Какого цвета МОИ глаза?'), 3, _("Зеленые"), _('Карие'), _('Голубые'), _("Голубо зеленые")),
    Question(_('Куда бы Я хотел поехать в отпуск?'), 2, _('Горы'), _('На побережье океана'), _('Море'), _('Токио')),
    Question(_('Какой МОЙ любимый цвет?'), 3, _('Желтый'), _('Синий'), _('Белый'), _('Черный')),
    Question(_('Что Я обычно пью?'), 2, _('Вода'), _('Газированные напитки'), _('Чай'), _('Кофе')),
    Question(_('С кем Я люблю проводить время?'), 4, _('Один'), _('Семья'), _('Друзья'), _('Любовь'))
)

define countWins = 0

define variant_prefixes = (_('А'), _('Б'), _('В'), _('Г')) # Префиксы для вариантов ответа

screen question_screen:
    frame:
        padding (8, 8, 8, 8)
        xalign .5
        yalign .5
        xsize 800
        vbox:
            spacing 40
            text "%s. %s" % (question_index + 1, __(question.text))
            grid 2 2:
                xfill True
                # экран должен возращать индекс выбранного ответа
                for i, variant in enumerate(question.variants):
                    textbutton "%s. %s" % (__(variant_prefixes[i]), __(variant)) action Return(i)

label test_loop:

    # если вопросы закончились, то прыгаем в лейбл test_complete
    if question_index >= question_count:
        return

    $ question = questions[questions_order[question_index]] # получаем текущий вопрос по его индексу
    call screen question_screen # вызываем экран, в котором будет отображён текст вопроса и варианты ответа
    # экран возвращает индекс ответа(хранится в переменной _return), который выбрал игрок
    if _return == question.correct:
        "Верно!"
        $ countAnswer += 1
    else:
        "Неверно!"
    $ question_index += 1
    jump test_loop

label labirint:
    scene bg biblioteka_1: 
        yalign 0.3
        zoom 1.3
    with fade

    "???" "{i}Величественная библиотека раскинулась на несколько этажей, и её стены покрыты стеллажами, заполненными книгами от пола до потолка. Каждая полка — это настоящий мир, наполненный знаниями и историями."
    "???" "{i}Книги разных размеров и цветов создают яркую мозаику, а запах бумаги и старинных переплетов наполняет воздух."

    "???" "{i}Так же здесь весят портреты и лишь Диван узнает, кто изображен на них...{b}лишь он{/b} сможет помочь своим товарищам пройти испытание."
    ivan "Тепрь я понял о чем говорил Медвед..."
    ivan "Вот почему он выбрал именно меня для своих загадок. Вот почему мне везде мерещаться преподователи"
    ivan "Два мира как будто бы объеденилсь и вышло нечто...Нечто испытывающее меня!"

    if arinaIsAlive:
        arina "Ебааааать"
    arkaha "А снаружи дом выглядил меньше"
    diana "Дурак что ли{w}, это же магия"
    katia "Даааа, ебаная магия"
    nikita "Ква-ква"
    "???" "{i}Слиппи заметил октырую книгу, которая источала из себя яркий свет"
    if alinaIsAlive:
        alina "О, чур я первая"
        nikita "Ква-ква!"
        alina "И так, что же тут у нас"
        diana "Читай вслух"
        arkaha "..."
        diana "Что...{w}мне тоже интересно..."
        alina "История НЭТИ и СыSOS"
    elif sergeiIsAlive:
        sergei "О, чур я первый"
        nikita "Ква-ква!"
        sergei "И так, что же тут у нас"
        katia "Читай вслух"
        diana "..."
        katia "Что...{w}мне тоже интересно..."
        sergei "История НЭТИ и СыSOS"
    else:
        katia "О, чур я первая"
        nikita "Ква-ква!"
        katia "И так, что же тут у нас"
        arkaha "Читай вслух"
        diana "..."
        arkaha "Что...{w}мне тоже интересно..."
        katia "История НЭТИ и СыSOS"

    show book:
        zoom 1.7
        yalign 0.2
        xalign 0.5

    show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}В безмолвном сердце древнего мира, {p}где свет солнца с трудом пробивался{p} сквозь густые кроны вековых деревьев,{p} раскинулся лес НЭТИ — место, окутанное {p}тайной и пропитанное магией.{p}Уводя вдаль от привычного мира. {p}Каждые несколько лет, когда ночное {p}небо озарялось таинственными звездами{p} и луны прятались за облаками, в НЭТИ {p}собиралась отважная группа {p}авантюристов. Этих бедолаг, лес {p}выбирал сам чтобы искусить и {p}испытать их. НЭТИ был известен{p}своей жестокостью и беспощадностью.{p}Всякий раз, когда лес{p}призывал гостей, {p}из стони выбирались лишь {p}{b}единицы.{/font}{/color}":
        yalign 0.3
        xalign 0.26
    show neti:
        yalign 0.4
        xalign 0.75
        xzoom 0.9

    nikita "Ква-ква-ква..."
    arkaha "Да, сам в шоке с этого..."
    diana "То есть мы здесь из-за этого ЕБАННОГО леса!"
    ivan "Ну конечно ведь это лес НЭТИ.{w} Пазл складывается!"
    hide text
    hide neti
    hide book
    "???" "{i}Дочитав книгу, она резко захлапывается и тут же издаеться страшный и пронзительный рев."
    bikov "РВААААААААА" with hpunch
    if romaIsAlive:
        roma "Что это было!?"
    elif alinaIsAlive:
        alina "Что это было!?"
    elif arinaIsAlive:
        arina "Что это было!?"
    else:
        katia "Что это было!?"
    
    "???" "{i}Из дальнего угла слышны шаги, трясущие всю библиотеку! И тут показывается он..."
    show bichok at center
    "???" "{i}Огромный по размеру быко-человек с огромными рогами ломает стенку стелажа."
    "???" "{i}Шаркая ногами и издавая страшный рык начинает сломя голову начинает нестись в сторону авантюристов."
    katia "Э-э-э-э, что это за {b}ПИЗДЕЦ{/b} такой!!!"
    diana "Нужно валить и по быстрее!"
    "???" "{i}Герои резко начинают бежать в один из коридоров огромной библиотеки. На угад сворачивая в любую из сторон."
    scene bg biblioteka_2: 
        yalign 0.3
        zoom 1.3
    with fade
    "???" "{i}Бегая наугад они наталкиваються на висящий портрет с надписью \"Роман\"."
    "???" "{i}Внезапно перед ними выскакивает стол с листком по середине."
    divan "Я этим займусь."
    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xalign 0.5
            xzoom 1.2
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}День первый{p}Я никогда не думал, что окажусь здесь, {p}в этом дремучем лесу под названием НЭТИ. {p}Когда тьма опускается, деревья становятся{p}настоящими монстрами: их искривленные {p}силуэты, словно скелеты древних гигантов, {p}вытягиваются в бесконечность, пронзая {p}мрак. Листва шепчет на ветру, и в {p}этом шепоте я слышу что-то{p} зловещее, словно сама природа приглашает{p} меня войти в свои объятия. Каждый {p}шаг отзывается эхом в моей голове,{p} и я ощущаю, как холод пробирается ко{p} мне под кожу.Все здесь пропитано {p}магией и страхом. Лес как будто {p}живёт своей жизнью, храня в себе{p} тайны, что не должны быть раскрыты.{p} Временами я вижу проблески света{p} — это, вероятно, феи или что-то {p}ещё, что манит меня своим мерцанием.{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        nikita "Ква!"#молодец
        divan "Я знаю"
        if sergeiIsAlive:
            sergei "Откуда ты вообще знаешь ответы на эти вопросы?"
        elif alinaIsAlive:
            alina "Откуда ты вообще знаешь ответы на эти вопросы?"
        elif arinaIsAlive:
            arina "Откуда ты вообще знаешь ответы на эти вопросы?"
        elif romaIsAlive:
            roma "Откуда ты вообще знаешь ответы на эти вопросы?"
        else:
            diana "Откуда ты вообще знаешь ответы на эти вопросы?"
        divan "Это сложно объяснить, давайте позже, как выберемся из этого ПИЗДЕЦА!"
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        show bichok at center
        arkaha "О черт! Бежим скорее"
    hide list
    hide text  
    scene bg biblioteka_3: 
        yalign 0.3
        zoom 1.3
    with fade
    "???" "Плутая по лабиринтам они наталкиваються на еще один портрет \"Диана\""
    katia "Твой выход, Диван!"
    
    $ questions = (
        Question(_('Как зовут МОЮ собаку?'), 3, _("Бубочка"), _('Дурочка'), _('Жалина'), _("Рошель")),
        Question(_('Куда бы Я хотел поехать в отпуск?'), 1, _('Умеет разговаривать как Стич'), _('Издавать смешной звук щекой'), _('Храпеть как старыйы дед'), _('Ржать как чайка')),
        Question(_('Кому Я швырнула в лоб льдинку?'), 1, _('Алина'), _('Катя'), _('Аркаша'), _('Сережа')),
        Question(_('Сколько Я работала экскурсоводом?'), 4, _('5 лет'), _('2 года'), _('7 лет'), _('4 года')),
        Question(_('Когда у МЕНЯ день рождения?'), 2, _('11 апреля 2003'), _('11 марта 2003'), _('11 февраля 2003'), _('11 января 2003'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xalign 0.5
            xzoom 1.2
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}День третий.{p}Мы нашли его. Особняк \"СыSOS Family\"{p} — зловещее строение, затерянное среди деревьев. {p}Он выглядит так, словно его построили{p} в кошмаре: щербатые стены, обвитые лианами{p}, окна, как пустые глазницы. Я чувствую,{p} как сердце замирает, когда мы переступаем{p}порог. Внутри темно и сыро, воздух {p}напоен запахом плесени и чего-то невыносимо{p} древнего. Каждый шаг вызывает треск старых {p}досок, словно сам особняк живёт и дышит{p}. Стены покрыты странными{p} символами. Я вижу тени, которые{p} движутся, когда я отвожу взгляд. Иногда{p} мне кажется, что кто-то или что-то {p}следит за нами, прячется в темных {p}уголках, готовое вырваться в любой момент.{p}Каждый уголок этого особняка дышит{p} опасностью. Я чувствую, как страх {p}обвивает меня, как плотная {p}паутина. Лишь бы нам удалось {p}выбраться отсюда живыми.{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        if alinaIsAlive:
            alina "Это звучит жутко..."
        elif arinaIsAlive:
            arina "Это звучит жутко..."
        elif romaIsAlive:
            roma "Это звучит жутко..."
        elif sergeiIsAlive:
            sergei "Это звучит жутко..."
        else:
            arkaha "Это звучит жутко..."
        ivan "Особняк СыSOS...{w}А что звучит в полне себе!"
        divan "Нужно бежать к следующему портету"
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        show bichok at center
        diana "БЕЖИМ!!!"
    
    hide list
    hide text

    scene bg biblioteka_3: 
        yalign 0.3
        zoom 1.3
    with fade
    "???" "Бегая туда-сюда они натыкаются на еще один портрет \"Екатерина\""

    $ questions = (
        Question(_('Сколько у МЕНЯ родных сестер?'), 2, _("0"), _('1'), _('2'), _("У меня брат")),
        Question(_('МОЕ хобби?'), 1, _('Фотографии'), _('Танцы'), _('Игра на гитаре'), _('Его нет')),
        Question(_('Кому Я швырнула в лоб льдинку?'), 1, _('Алина'), _('Катя'), _('Аркаша'), _('Сережа')),
        Question(_('Как зовут МОЮ кошку?'), 4, _('Люся'), _('Муся'), _('Ляля'), _('Мася')),
        Question(_('МОЕ любимое животное?'), 2, _('Собака'), _('Кошка'), _('Кролик'), _('Крыса'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xalign 0.5
            xzoom 1.2
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}День пятый.{p}Мои худшие опасения подтвердились.{p} Сегодня, блуждая по лесу, мы наткнулись{p} на существо, которое навсегда останется {p}в моем кошмаре. Она была женщиной,{p} но в ней не было ничего человеческого.{p} Её тело изогнулось, как щупальца осьминога,{p} и из неё исходила зловещая аура.{p} Чёрные глаза светились в темноте, как {p}угли, готовые поглотить нас. Её {p}приспешники, подобные тени, окружали её,{p} но их образы были размыты, словно {p}они были частью леса. Они двигались{p} быстро и бесшумно, сливаясь с окружающей{p} средой, и я почувствовал, как холодок{p} пробежал по спине.  Мы бежали,{p} не оглядываясь, как будто сами{p} деревья пытались нас остановить.{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        if romaIsAlive:
            roma "Это Архипелаг, они увидели ее...{w}А что особняк, они в нем не остались больше или как?"
        elif alinaIsAlive:
            alina "Это Архипелаг, они увидели ее...{w}А что особняк, они в нем не остались больше или как?"
        elif arinaIsAlive:
            arina "Это Архипелаг, они увидели ее...{w}А что особняк, они в нем не остались больше или как?"
        elif sergeiIsAlive:
            sergei "Это Архипелаг, они увидели ее...{w}А что особняк, они в нем не остались больше или как?"
        else:
            diana "Это Архипелаг, они увидели ее...{w}А что особняк, они в нем не остались больше или как?"
        ivan "Архипова та еще стерва, но щупальца..."
        divan "Узнаем позже"
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        show bichok at center
        katia "СЪЕБЫВАЕМ!"
    hide list
    hide text

    scene bg biblioteka_4: 
        yalign 0.3
        zoom 1.3
    with fade

    "???" "Следующим они нашли портрет \"Алина\""

    $ questions = (
        Question(_('На каком факультет Я изначально пошла?'), 1, _("ФПМИ"), _('ФБ'), _('ФЭН'), _("ФГО")),
        Question(_('Каким спортом Я занималась?'), 3, _('Волейбол'), _('Тенис'), _('Баскетбол'), _('Спортивное ориентирование')),
        Question(_('Замужем ли Я?'), 1, _('Наверное'), _('Да'), _('Нет'), _('Я жената')),
        Question(_('Каких насекомых Я боюсь?'), 4, _('Гусеницы'), _('Пауки'), _('Тараканы'), _('Всех')),
        Question(_('Что Я люблю делать больше всего?'), 2, _('Есть'), _('Спать'), _('Есть во сне'), _('Владислава'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xalign 0.5
            xzoom 1.2
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}День седьмой.{p}Особняк стал нашим временным прибежищем,{p} но это место тоже таит опасности.{p} Наша группа разделилась, и я остался{p} один, блуждая по его бездонным коридорам.{p} В одном из залов я встретил {p}его — Музыканта. Он сидел за старинным {p}пианино, его руки танцевали по {p}клавишам, создавая мелодию, которая {p}завораживала и пугала одновременно. {p}Его лицо было скрыто в тени, и, когда{p} он поднял голову, я увидел, что{p} его глаза были пустыми, как бездна. Он{p} предложил мне сделку: если я сыграю с ним, {p}он даст мне ключ к выходу из этого проклятого{p} места. Но внутри меня что-то кричало, что{p} это ловушка. Я не смог сопротивляться его {p}музыке, но в последний момент, когда {p}его мелодия затянула меня, я вырвался и{p} бежал, оставив его позади. Я не{p} знаю, что стало с остальными.{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        if arinaIsAlive:
            arina "Вот и узнали про особняк...{w}Да будь ты проклят НЭТИ"
        elif alinaIsAlive:
            alina "Вот и узнали про особняк...{w}Да будь ты проклят НЭТИ"
        elif romaIsAlive:
            roma "Вот и узнали про особняк...{w}Да будь ты проклят НЭТИ"
        elif sergeiIsAlive:
            sergei "Вот и узнали про особняк...{w}Да будь ты проклят НЭТИ"
        else:
            katia "Вот и узнали про особняк...{w}Да будь ты проклят НЭТИ"
        divan "..."
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        nikita "КВА-КВА!"
    
    hide list
    hide text
    
    if countWins < 3:
        $ nikitaIsAlive = False
        show bichok:
            xalign 0.5
            yalign 0.6
        show slippi:
            xalign 0.5
            yalign 0.8
            zoom 1.4
        "???" "{i}Зловещее существо резко появляется из-за угла и хватает лягушку."
        divan "Слиппи{w}, НЕТ"
        arkaha "Да не переживай, он ядовитый. Весь.{w} Щас отпустит и будет корячиться от бо..."
        show slippi:
            xalign 0.5
            yalign 0.3
            zoom 1.4
        with move
        "???" "{i}Герои наблюдают как быко-человек корячиться от боли и недолго думая разрывает Слиппи пополам."
        katia "БЛЯТЬ, БЕЖИМ СКОРЕЕ, ЧЕГО ЗАСТЫЛИ!!!"
        "???" "{i}В полном шоке аванюристы начинают убегать от нависшей над ними угрозы."
    $ renpy.notify("Судьба изменина")
    
    scene bg biblioteka_5: 
        yalign 0.3
        zoom 1.3
    with fade

    "???" "Еще один портрет - \"Аркадий\""

    $ questions = (
        Question(_('Любимые исполнители Аркадия Юрьевича?'), 4, _("КИШ"), _('Три дня дождя'), _('Шаман'), _("Тони Раут")),
        Question(_('Имя первого питомца Аркадия Юрьевича?'), 1, _('Джесика'), _('Максимильян'), _('Дина'), _('Дрима')),
        Question(_('Сколько пенсыл Аркадия Юрьевича?'), 1, _('100 000'), _('0'), _('1'), _('-7')),
        Question(_('Родной город Аркадия Юрьевича?'), 1, _('Новокузнецк'), _('Новосибирск'), _('Кемерово'), _('Томск')),
        Question(_('Любимый инструмент Аркадия Юрьевича?'), 4, _('Молоток'), _('Вилка'), _('Паяльник'), _('Гитара'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xzoom 1.2
            xalign 0.5
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}День девятый.{p}Сегодня я спустился в библиотеку особняка.{p} Это место было мрачным и запущенным, с пыльными {p}книгами, которые шептали свои истории. {p}Но среди них я почувствовал присутствие чего-то{p} ужасного. И вот, когда я открыл одну из книг, {p}она сама вырвалась из полки, и из тьмы возникло {p}чудовище. Оно было огромным, с лапами, которые{p} могли бы разорвать меня на куски, и множеством глаз, {p}сверкающих как звёзды в ночи. Я замер на {p}месте, когда оно приблизилось, и его шёпот {p}проникал в мою голову. Я видел в его глазах не только {p}ненависть, но и тоску. Оно искало что-то,{p} и я догадывался, что это — ответы на вопросы, {p}которые могут поглотить всё существо. Я не {p}мог оставаться там ни секунды дольше, и, {p}пока оно отвлеклось, я выбежал из библиотеки,{p} сердце стучало в груди, как барабан. Теперь {p}я понимаю: лес НЭТИ и особняк \"СыSOS Family\" — это{p} не просто испытания. Это игра, в которую играют{p} силы, о которых я даже не догадываюсь. И каждый {p}шаг может стать последним.{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        if sergeiIsAlive:
            sergei "Эта та штука, что за нами гониться, ей нужны ответы, может это они и есть, давай Диван поднажми"
        elif arinaIsAlive:
            arina "Эта та штука, что за нами гониться, ей нужны ответы, может это они и есть, давай Диван поднажми"
        elif alinaIsAlive:
            alina "Эта та штука, что за нами гониться, ей нужны ответы, может это они и есть, давай Диван поднажми"
        elif romaIsAlive:
            roma "Эта та штука, что за нами гониться, ей нужны ответы, может это они и есть, давай Диван поднажми"
        else:
            diana "Эта та штука, что за нами гониться, ей нужны ответы, может это они и есть, давай Диван поднажми"      
        divan "Я стараюсь"
        ivan "Хммм, Быков стал минотавром, {w}символично"
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        show bichok at center
        arkaha "ЕБАНЫЙ В РОТ!"
    hide list
    hide text

    scene bg biblioteka_6: 
        yalign 0.3
        zoom 1.3
    with fade

    "???" "Следующим они нашли портрет \"Аркадий\""

    $ questions = (
        Question(_('Кем Я хотела стать в детстве?'), 1, _("Врач"), _('Учитель'), _('Электрик'), _("Адвокат")),
        Question(_('Как зовут МОЮ кошку?'), 3, _('Мирка'), _('Муська'), _('Милка'), _('Симка')),
        Question(_('Что являеться одним из МОИХ самых больших страхов?'), 1, _('Высота'), _('Глубина'), _('Маленькое пространство'), _('Пауеи')),
        Question(_('Какой у МЕНЯ рост?'), 3, _('155'), _('167'), _('161'), _('165')),
        Question(_('Ломала ли Я кости?'), 2, _('Да'), _('Нет'), _('Руку'), _('Голеностоп'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xzoom 1.2
            xalign 0.5
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}День тренадцатый.{p}Мне кажется я начал сходить с ума. {p}Никто из моих товарещей не вернулся, не знаю,{p} может это существа снаружи или тот страннный{p} мужчина-музыкант, но их нет. Походив по {p}особняку еще, я нашел комнаты принадлежавшие,{p} видимо, СыSOSовцам. В каждой из них я все {p}больше узнавал о них и хочу вернуться в {p}библиотеку, вдруг именно там я смогу {p}найти выход. Мне страшно. Очень страшно. Зачем {p}я вообще веду эти записки.{p} Кому они уже нужны. {p}Думал вернусь из этого приключения героем...{p}Я не помню когда последний раз нормально ел{p} и вода уже тоже заканчиваеться, таким {p}темпом, если не от чудовищь, то {p}от голода или жажды точно пойду {p}в фундвмент этого здания{p}Почему я здесь?{p}Все, решил, завтра я спущусь к этому монстру{p} в библиотеку!{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        if romaIsAlive:
            roma "Бедняга, сколько же он пережил..."
        elif arinaIsAlive:
            arina "Бедняга, сколько же он пережил..."
        elif sergeiIsAlive:
            sergei "Бедняга, сколько же он пережил..."
        elif alinaIsAlive:
            alina "Бедняга, сколько же он пережил..."
        else:
            arkaha "Бедняга, сколько же он пережил..."  
        divan "Не время для жалости, пора к следующему"
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        show bichok at center
        nikita "КВА-КВА!"
    hide list
    hide text

    scene bg biblioteka_7: 
        yalign 0.3
        zoom 1.3
    with fade
    "???" "Пробежав по коридором еще немного, герои находят портрет с подписью \"Никита\""

    $ questions = (
        Question(_('Кем Я хотела стать в детстве?'), 1, _("Врач"), _('Учитель'), _('Электрик'), _("Адвокат")),
        Question(_('Как зовут МОЮ кошку?'), 3, _('Мирка'), _('Муська'), _('Милка'), _('Симка')),
        Question(_('Что являеться одним из МОИХ самых больших страхов?'), 1, _('Высота'), _('Глубина'), _('Маленькое пространство'), _('Пауеи')),
        Question(_('Какой у МЕНЯ рост?'), 3, _('155'), _('167'), _('161'), _('165')),
        Question(_('Ломала ли Я кости?'), 2, _('Да'), _('Нет'), _('Руку'), _('Голеностоп'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        show list:
            yalign 0.3
            zoom 2
            xzoom 1.2
            xalign 0.5
        "???" "{i}На листке начинают появляться буквы, заменюящие содержиое листка."
        show text "{color=#000000}{font=ofont.ru_PF Libera Pro Liberissima.ttf}Я ПОНЯЛ! {p}Я НАКОНЕЦ ТО ПОНЯЛ КАК ВЫБРАТЬСЯ ОТСЮДА!!!{p}Разгадывая загадки у портретов, чудовище {p}становиться слабее и уже не так страшно! {p}Хорошо, что я осмотрел особняк, я выберусь, {p}я точно выберусь от сюда, из этого {p}ада! Если кто-то читает мои записи, то {p}вот где расположен выход из этого места. {p}{p}НАЛЕВО-НАЛЕВО-ПРЯМО-ПРЯМО-НАЛЕВО{p}-НАПРАВО-НАЗАД-ПРЯМО-НАПРАВО{p}{p} Я стою прямо у двери, но тут какой то {p}сложный меха...{p}О НЕТ!!!! ТОЛЬКО НЕ ТЫ! ОН ВОСКРЕС!!!!{p}ВРЕМЕНИ МАЛО! Надеюсь мои записи{p} помогут вам, как помогли бы мне!{/font}{/color}":
            yalign 0.3
            xalign 0.5
        $ countWins += 1
        katia "ВОТ ОНО!!! НУЖНО БЛЯТЬ СКОРЕЕ БЕЖАТЬ ПО ЭТИМ ПОДСКАЗКАМ!"
        divan "Покойся с миром, бедная душа..."
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        nikita "КВА-КВА!"
        show bichok at center
    hide list
    hide text

    scene bg biblioteka_8: 
        yalign 0.3
        zoom 1.3
    with fade

    "???" "Последний портрет был над странной, механической дверью \"Сергей\""

    $ questions = (
        Question(_('МОЯ самая знаменитая фраза'), 2, _("Елки"), _('Ебаный Бобаный'), _('КАЗАНТИП'), _("Еще по одной")),
        Question(_('Курил ли Я до Новосибирска?'), 2, _('Да'), _('Нет'), _('Немножко'), _('Только по праздникам')),
        Question(_('В какой комнате Я жил?'), 3, _('909'), _('915'), _('910'), _('910а')),
        Question(_('Сколько раз МНЕ везло на сдачах лабораторных?'), 1, _('Всегда'), _('8 раз'), _('Ни разу'), _('13 раз')),
        Question(_('Основателем какой компании Я стал поневоле?'), 4, _('АКОГДАНЕДЕЛАЛИТО'), _('СыSOS'), _('НИКАПЛИВРОТ'), _('СысГИС'))
    )

    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0
    $ countAnswer = 0

    call test_loop

    if countAnswer >= 2:
        diana "Открывается,{w} она открываеться, {w}быстрее, все внутрь!"
        $ countWins += 1
    else:
        "???" "{i}Портрет преображается на глазах, и вдруг на его поверхности заиграла зловещая улыбка, словно из теней. Краска начинает медленно течь, оставляя за собой таинственные следы."
        "Портрет" "Не прошел!"
        "Портрет" "ААААААААААААААААААААААААААА"
        arkaha "Отойди, Диван, тут и я справлюсь"
        "???" "{i} Размохнувшись своим топором, Флирт бьет со всей силы в середину двери, из-за чего появляется неглубокая трешина" with hpunch
        diana "Я помогу"
        "???" "{i}Герои начали поочередно ломать дверь. После нескольких ударов она наконец начала ломаться."
        divan "Еще немного!"
        "???" "{i}Продолбив щель в двери, авантюристы поочередно начали заходить внутрь."
    if countWins <= 6:
        $ arkahaIsAlive = False
        show bichok at center
        show flirt:
            xalign 0.4
            yalign 0.6
            zoom 1.7
        "???" "{i}Последним проходил Флирт, и, внезапно, у него в груди появляется рог чудовища."
        arkaha "Вот черт..."
        "???" "{i}Дварфа начинают агрессивно тянуть назад."
        arkaha "Я задержу его и постараюсь закрыть щель, бегите!"
        katia "НЕЕЕТ,{w} ФЛИРТ"
        diana "Бежим скорее, его смерть не должа стать напрасной! Бежим!"
        "???" "{i}Со слезами на глаза, герои прощаються с их верным другом и начинаю бежать по темному коридору"
        arkaha "Я НЕ УМРУ БЕЗ БОЯ!!! НАПАДАЙ ЧУДОВИЩЕ!"
    jump dver