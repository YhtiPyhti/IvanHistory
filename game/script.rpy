# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define ivan = Character('Ваня', color="#974141")
define divan = Character('Диван', color="#2d6fba")

define alina = Character('Тола', color="#008800")
define arina = Character('Кэрри', color="#f5b5db")
define arkaha = Character('Флирт', color="#e2e956fb")
define diana = Character('Ирида', color="#0c8438")
define katia = Character('Кити', color="#72ada9")
define nikita = Character('Слиппи', color="#0bd80b")
define roma = Character('Эриван', color="#b48e05")
define sergei = Character('Дьяволо', color="#b41405")

define historyman = Character('Рассказчик', color="#f3f8f3") # Sergei
define bomj = Character('Бомж-Серега', color="#145a0a") # Бомж

# Переменные выбора
default isByingBomj = False
default isSaveNikita = False

# Игра начинается здесь:
label start:

    scene bg avtf
    show ivan
    jump forest
    ivan "{b}Как же заебала эта ебатория{/b}"

    historyman "{i}Это наш главный герой Иван. И да, у этого бедняги сегодня было пять пар"

    ivan "Нужно быстрее в общагу, а то газета с новыми анекдотами сама себя не прочтёт"

    scene bg hostel with fade
    
    play music "trevoga.mp3"
    
    show ivan at left
    show fireman:
        xalign 1.2 
        yalign 2.0

    ivan "Да ёлки палки! Пожарки еще не хватало.{w} Ладно, пойду в магаз.{w} Надеюсь они скоро уедут"

    stop music

    scene bg magnit with fade
    show bomj at right
    show ivan at left

    historyman "{i}В магазине к нему обратился человек, при жизни ставший Легендой"

    bomj "Ххааук$йцууваап5y32ыыgыыук41?"

    ivan "Чё тебе надо, дед? Отвали от меня!"

    bomj "дфыра3э1ж24л546д7д6д5312дл2од4д21лр43жоп5д31ор3ж2лопр4ж1дро2р5оп"

    historyman "{i}Бездомный робко показывает на стеллаж с водкой..."

    menu:
        "{b}Купить Сереге покушать?"
        "Купить водки":
            ivan "Держи, только отстань от меня!"
            bomj "илчл3одео99гичждслмзывг9щяз28гсчлд"
            historyman "{i}Серега отдал странный предмет в качестве благодарности" # Флакончик со странной жидкостью
            $ isByingBomj = True
        "Купить хлеба и сосисок":
            ivan "Это тебе явно нужнее"
            bomj "ыародрвдыао123олд2лдр32"
            historyman "{i}Серега отдал Ивану странный предмет в качестве благодарности" # Флакончик со странной жидкостью
            $ isByingBomj = True
        "Ничего не покупать":
            ivan "Да иди ты нахуй!"
            bomj "АЫВалкцпощшам13УШУОАл550МЛВАЖЭййаф"

    scene bg street with fade

    show ivan at left

    historyman "{i}Выходя из магазина, Иван заметил своего старого товарища Никиту, который неспешно переходил дорогу"
    show nikita walk:
        xalign 0.3

    historyman "{i}Но также он заметил надвигающуюся угрозу"
    show car:
        yalign 0.25
        xalign 0.7
    
    historyman "{i}Грузовик несется на всей скорости к товарищу нашего героя"
    
    menu:
        "{b}Спасти ли мне своего товарища Никиту?"
        "Конечно! Он мне еще 5 рублей должен":
            ivan "СТООООООООЙ"
            historyman "{i}Иван оттолкнул Никиту, и встал на его место.{w} Грузовик-сан, не справившись с управлением, сбивает нашего героя, тем самым начиная нашу исторую" with hpunch
            jump fight
        "Да пошел он!":
            historyman "{i}На глазах у нашего героя сбивают Никиту, но Ивану нет никакого дела до этого.{w} Он слишком устал на парах" with hpunch

    if isByingBomj:
        ivan "Хммммм, что это дал мне Серега?"
        historyman "{i}Разглядывая странный предмет, Иван находит в нем что-то похожее на бутылек с деревяной пробкой, внутри которого находится странная переливающаяся жидкость"
        ivan "И что это за хрень?"
        ivan "Понюхаю её хоть что-ли"
        historyman "{i}Не долго думая, Иван открывает этот бутылек, и пытается принюхаться..."
        historyman "{i}{b}!!!РОКОВАЯ ОШИБКА!!!"
        historyman "{i}Герой начинает терять сознание и тут начинается наша история"
        jump fight
    else:
        historyman "{i}И все по новой"
        call start
    return
