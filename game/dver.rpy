define gm = Character('GameMaster', color="#ffffff")

define deadIsAll = False

label dver:
    scene bg coridor
    if arkahaIsAlive == False:
        "???" "{i}Ирида резко хватает за грудь Дивана"
        diana "Доволен собой!? {w}Решил все загадки, молодец!"
        divan "Отпусти."
        diana "Отпустить!?{w} Да ты смеешься что ли?{w} ТЫ СКАЗАЛ ЧТО ЗНАЕШЬ ЧТО ДЕЛАТЬ!!!"
        diana "Флирт был не просто дворфом над которым можно посмеяться, он был нашим другом. {w}ДРУГОМ понимаешь? А из-за те..."
        divan "Из-за меня вы остались в живых! Хватит винить МЕНЯ! Я делал что-то пытался спасти нас из этого ада!"
        diana "Да что ты..."
        if sergeiIsAlive:
            sergei "Он прав."
        elif alinaIsAlive:
            alina "Он прав."
        else:
            katia "Он прав."
        diana "И что?{w} ЧТО С ЭТОГО?{w} Мне может его еще и поблагодарить за это стоит, а?"
        if sergeiIsAlive:
            sergei "Отпусти его."
        elif alinaIsAlive:
            alina "Отпусти его."
        else:
            katia "Отпусти его."
        "???" "{i}Ирида кидает Дивана к стене напротив и идет вперед."
        katia "Ты прости ее за это, просто...{w}просто это место..."
        divan "Я понимаю."
        katia "Кстати, ты не хочешь нам что-то рассказать?"
    elif arkahaIsAlive and nikitaIsAlive == False:
        arkaha "Фух, наконец то выбрались!"
        katia "Дааа, это было {w}тяжко."
        if alinaIsAlive:
            alina "Под конец, я думала он нас всех убьет!"
        elif arinaIsAlive:
            arina "Под конец, я думала он нас всех убьет!"
        elif romaIsAlive:
            roma "Под конец, я думала он нас всех убьет!"
        elif nikitaIsAlive:
            nikita "Под конец, я думала он нас всех убьет!"
        else:
            diana "Под конец, я думала он нас всех убьет!"
        divan "Извините, что подвел вас..."
        katia "Слиппи жалко конечно, но мы выбрались, не стоит сильно винить себя!"
        diana "Да, ты молодец, ты вывел нас из этого лабиринта!"
        divan "Спасибо..."
        katia "Кстати об этом, ты не хочешь нам что-то рассказать?"
    else:
        diana "Фух, наконец то выбрались!"
        katia "Дааа, это было {w}тяжко."
        arkaha "Спасибо, Диван, ты наш спаситель, как ты отвечал на все эти вопросы!"
        diana "Кстати об этом, ты не хочешь нам что-то рассказать?"
    
    divan "Да, хочу, еще когда я очнулся в этом мире."
    if sergeiIsAlive:
        sergei "Этом мире?"
    elif arinaIsAlive:
        arina "Этом мире?"
    elif romaIsAlive:
        roma "Этом мире?"
    elif alinaIsAlive:
        alina "Этом мире?"
    else:
        katia "Этом мире?"
    divan "Да, в этом мире. Даже не знаю с чего начать..."
    divan "Видели те портреты ведь? Так вот, они это вы, но в дргуом мире, понимете?"
    if nikitaIsAlive:
        nikita "Ква-ква?"
    elif arkahaIsAlive:
        arkaha "Ты хочешь сказать нам, что ты не из этого мира?"
    elif arinaIsAlive:
        arina "Ты хочешь сказать нам, что ты не из этого мира?"
    elif romaIsAlive:
        roma "Ты хочешь сказать нам, что ты не из этого мира?"
    else:
        diana "Ты хочешь сказать нам, что ты не из этого мира?"
    
    divan "Да, не из этого, как все сложно."
    "???" "{i}Здесь наш Герой постепенно начинает рассказывать про свою жизнь в другом мире, ДнД и о СыSOS. Все остальные начали внимательно слушать его рассказ."
    katia"НИХУЯ СЕБЕ!!!"
    divan "Когда я осознал где я, у меня были такие же эмоции."
    diana "Тогда это многое объесняет...Твое странное поведение, страх, отстраненность, путанеца в именах..."
    divan "Представьте себя на моем месте. Вы очутились в незнакомом, жутком и жестоком мире, и не знаете как выбраться от сюда..."
    "???" "{i}Повисла тишина"
    divan "Ладно, пойдемте по этому туннелю, надеюсь мы хотя бы выберемся из этого леса."
    "???" "{i}Идя по длинному туннелю, они приходят к двери."
    katia "Открываю?"
    diana "Да."
    "???" "{i}Открывая дверь, их встречаю Я!"
    scene bg dangeonmaster:
        yzoom 0.5
    gm "Ну здраствуй{w}, Иван.{w}Ну как, понравилась моя история?"
    if romaIsAlive:
        roma "Ты еще кто такой?"
    elif arinaIsAlive:
        arina "Ты еще кто такой?"
    elif alinaIsAlive:
        alina "Ты еще кто такой?"
    elif nikitaIsAlive:
        nikita "Ква-ква?"
    else:
        diana "Ты еще кто такой?"
    divan "Гейм-мастер."
    gm "Оооо, а ты догадливый оказывается!"
    divan "Это ты меня сюда забросил!?"
    gm "Ой, ну не стоит кричать..."
    if arkahaIsAlive:
        arkaha "ЭТО ТЫ ВИНОВАТ В ЭТИХ ПИЗДЕЦАХ ЧТО ТВОРИЛИСЬ ТУТ!?!?"
    elif romaIsAlive:
        roma "ЭТО ТЫ ВИНОВАТ В ЭТИХ ПИЗДЕЦАХ ЧТО ТВОРИЛИСЬ ТУТ!?!?"
    else:
        katia "ЭТО ТЫ ВИНОВАТ В ЭТИХ ПИЗДЕЦАХ ЧТО ТВОРИЛИСЬ ТУТ!?!?"
    gm "Не мешайте нам."
    gm "Внезапно из стен появилсь руки, которые мертвой хваткой схватили героев."
    diana "Ты...ТЫЫЫЫ..Я ТЕБ..."
    gm "И закрыли им рты."
    divan "Да что тебе нужно?"
    gm "Мне?{w} Ничего. Ты думаешь я хочу вас проводить по опасным местам, описывать эти жуткие вещи и наблюдать за вашими страданиями."
    gm "Нет! Это все необходимо{w}, понимаешь необходимо!"
    divan "Что мне сделать чтобы я вернулся?"
    gm "Вооот этот вопрос куда уместнее, чем предыдущий."
    gm "Смотри, у тебя есть два выбора."
    divan "Да хватит твоих игр, я не буду играть по твоим правилам!"
    gm "Эх..."
    if alinaIsAlive:
        gm "Одна из рук ловким движением сворачивает шею Толе."
    elif arinaIsAlive:
        gm "Одна из рук ловким движением сворачивает шею Кэрри."
    elif sergeiIsAlive:
        gm "Одна из рук ловким движением сворачивает шею Дьяволо."
    elif romaIsAlive:
        gm "Одна из рук ловким движением сворачивает шею Эривану."
    elif nikitaIsAlive:
        gm "Одна из рук ловким движением сворачивает шею Слиппи."
    elif arkahaIsAlive:
        gm "Одна из рук ловким движением сворачивает шею Флирту."
    else:
        gm "Одна из рук ловким движением сворачивает шею Кити."

    divan "НЕЕЕЕЕЕЕТ! Остановись, не нужно этого делать!"
    gm "Ты уже играешь по моим правилам, просто еще не понял этого."
    gm "Теперь ты готов к диалогу."
    divan "Да"
    gm "Ну чтож, вернемся, у тебя есть выбор:{p}УБИТЬ ВСЕХ ВЫЖИВШИХ{p}ОСТАТЬСЯ ЗДЕСЬ НАВСЕГДА"
    gm "Что выберешь?"
    gm "Давай сдлеаем выбор еще сложнее"
    gm "По неизвестной причине, павшие герои переносятся к Дивану и начинают оживать один за одним. Ноне успев очнуться их хватают руки из стен."
    divan "Ублюдок!"
    gm "Сточту за комплимент."
    gm "Ну так что{w}, что выберешь."

    menu:
        "{b}Что сделать?"
        "УБИТЬ ВСЕХ":
            $deadIsAll = True
            gm "Вот оно как{w}, хм{w}, интересно."
            divan "Заткнись и просто сделай это!"
            gm "Ловким движением, руки поочередно сворачивают шеи всем авантюристам."
            gm "Не скажу конечно, что доволен твоим выбором, но он на то и твой, хех"
            divan "Забери меня от сюда!"
        "ОСТАТЬСЯ ЗДЕСЬ НАВСЕГДА":
            gm "Вот оно как{w}, хм{w}, интересно."
            divan "Я не променяю эти жизни на свою! Доволен!"
            gm "Ага."
            divan "Что!"
            gm "Тебе не послышелось, я доволен тобой"
            gm "Именно этого я и ожидал от тебя"
    $ renpy.notify("Судьба изменина")
    gm "Забирайся ко мне и попадешь домой..."
    jump hospital