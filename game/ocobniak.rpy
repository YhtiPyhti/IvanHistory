#NPC
define medved = Character('Медвед', color="#5b5e09")

label ocobniak:
    scene bg lec doroga with fade
    
    "???" "{i}Кити и Ирида встали спереди и повели за собой колонну."
    
    if alinaIsAlive == False and arinaIsAlive:
        "???" "{i}Ирида проходя мимо Дивана сильно толкает его плечем."
    elif alinaIsAlive and arinaIsAlive == False:
        "???" "{i}Эриван проходя мимо Дивана сильно толкает его плечем."
    
    katia "Я успела заметить, как в окнах мелькали огни, но когда решила подойти чуть ближе, они исчезли. Это было странно и немного пугающе"
    diana "А я почувствовала, что кто-то наблюдает за нами, мороз по коже пробежал от одной мысли, что сейчас мы попадем в засаду"

    if alinaIsAlive and arinaIsAlive:
        "???" "{i}Тут же Дьяволо обратился к авантюристам, чтобы те были особо внимательны и оглядывались по сторонам."
    else:
        "???" "{i}Тут же Дьяволо обратился к авантюристам, чтобы те были особо внимательны и оглядывались по сторонам, бросив озлобленный взгляд в сторону Дивана"
        divan "Да, признаю вчера была моя вина, но не стоит сейчас тыкать меня носом в любой удобный случай, чтобы потешить свое самолюбие"
        arkaha "Да никто и не пытается как-то тебя задеть, но, друг, все скорбят по своему и от этого быстро не избавиться"
  
    "???" "{i}Вновь между ребятами повисла тишина. Все продолжали двигаться по лесной тропе, внимательно смотря по сторонам"
    arkaha "Скоро прийдем уже?"
    katia "Осталось немного"
    "???" "{i}Деревья вокруг них высокие и величественные, их ветви переплетаются, создавая почти непроглядный зеленый потолок. Легкий ветерок шепчет в листве, и откуда-то доносится мелодичный звук, будто кто-то играет на флейте."
    arkaha "Нам еще долго идти?"
    katia "..."
    "???" "{i} Диван замечает, что его компаньен Дьяволо засмотрелся на одно из величественных деревьев и совершенно не видит, что идет в неглубокую яму."
    menu:
        "{b}Предупридить Дьяволо?"
        "Да":
            divan "Дьяволо, осторожно, яма."
            sergei "Ээээх. {w}Спасибо, Диван"
        "Нет":
            sergei "{w}Бля-я-ять. {w}Сука. {w}Ебаная яма"
            "???" "{i} Дьяволо попадает в яму."
    "???" "{i}По мере приближения к особняку, тропинка становится все более извивающейся и запутанной. Внезапно, они замечают, что воздух вокруг них стал тяжелее, а шум листвы усиливается, будто бы зовет их. Это заставляет их остановиться и задуматься..."
    roma "Что, если это ловушка?"
    nikita "КВа-квА-ква-КВА!"
    katia "А что если это единственное место откуда мы можем выбраться? Ты об этом не подумал?!"
    nikita "КВААААААААА-ква!"
    "???" "{i}Тут же Флирт перебивает этот бесполезный спор"
    arkaha "Ну когда уже прийдем?"     
    katia "Да отъебись ты! Вот он уже"
    scene bg lec osobnak with fade
    "???" "{i}После блужданий по лесу, группа наталкивается на величественный, но заброшенный особняк."
    "???" "{i}Его стены покрыты мхом, а окна заколочены досками, но изнутри доноситься странный свет и звуки. Приблизившись, персонажи чувствуют магическое притяжение и опасение одновременно."
    ivan "И они серьезно хотят туда идти!?"
    if arinaIsAlive:
        arina "Ничего себе он большой"
    else:
        slippi "Ква-ква..."
    arkaha "Да..."
    roma "Ну что {w}идем."
    "???" "{i}Герои аккуратно подходят к двери в полной готовности засады."
    "???" "{i}Флирт подходит к двери и осматривает ее."
    "???" "{i}Дверь сделана из странного материала и выглядит очень старой."
    arkaha "Приготовьтесь, открываю"
    scene bg ocobnak hole:
        zoom 1.7
    with fade
    "???" "{i}Открывая дверь, она издает очень пронзителный скрип, эхом пронесшийся по всему особняку."
    "???" "{i}Входя внутрь, героев встречает грязная, заросшая плесенью лесница."
    "???" "{i}Так же они услышали звуки фортопьяна"
    sergei "Как-то стремно здесь...еще и этот звук."
    nikita "Ква-кВВа-КВА?"
    if alinaIsAlive:
        alina "То есть всю дорогу ты писался от страха, а теперь ты хочешь идти на звук"
    else:
        katia "То есть всю дорогу ты писался от страха, а теперь ты хочешь идти на звук"
    nikita "Ква..."
    diana "Давайте так, я с Флиртом пойду вперед, за нами пойдут Слиппи и Кити."
    divan "Хорошо, я пойду позади, помгу вам с арболетом."
    if alinaIsAlive and arinaIsAlive:
        diana "Хорошо"
    elif alinaIsAlive == False and arinaIsAlive:
        diana "Только внимательно смотри по сторонам..."
    elif alinaIsAlive and arinaIsAlive:
        roma "Только целься лучше..."
    else:
        sergei "Ага, только нас не убей..."
        slippi "Ква-ква-Ква"
        sergei "..."
    "???" "{i} Герои пошли на звук, он донасился из комнаты на первом этаже"
    "???" "{i} Подойдя к двери, за которой донасился звук, они чуствовали запах гнили и разлагающегося мяса"
    if alinaIsAlive:
        alina "С каждой секундой ощущение, что тут твориться зло, все больше и больше..."
    diana "Открываю!"

    scene bg ocobnak stolovai:
        zoom 1.7
    with fade

    show medved_1:
        xalign 0.7
        yalign 0.7
        xzoom -1.0
    "???" "{i}Отворя и зайдя внутрь, герои встречают обеденный зал."
    "???" "{i}На столе лежит бедренная кость, гнилое мясо наложено на блюдцах, а бокалы запачканы алой жидкостью."
    "???" "{i}Так же здесь находиться источник звука."
    "???" "{i}Огромный мужчина, больше похожий на огра сидит и играет по клавишам фортпьяно чужими пальцами"
    ivan "БлЯтЬ, {w}ЭтО чТо ВоОбЩе ТаКоЕ???" with hpunch
    "???" "{i} Он, казалось, полностью погружен в музыку, он играюче создавал завораживающую мелодию.  "
    "???" "{i} Огр почувствовав их пристуствие, оборачивается и с ухмылкой говорит:"
    medved "О, гости! Присаживайтесь, угощайтесь, послушайте мою прекрасную музыку и быть может я дам вам шанс выиграть свободу."
    "???" "{i} Услышав что им нужно будет угощаться гнилым мясом, Флирт одергивает Эривана и щепчет ему на ухо"
    arkaha "Нам нужно валить отсюда и поскорее, он сожрет нас быстрее, чем мы успеем моргнуть"
    roma "Да быть может не все так страшно, как кажется на первый взгляд"
    "???" "{i} Тут Кити одергивает Флирта"
    katia "Может быть хватит ныть сегодня, меня уже трясет от злости, ты ведь не обязан это есть..."
    medved "О чем вы там шушукаетесь? Вы трое? Вас не устраивает мое гостепреимство?"
    "???" "{i} Тут же Ирида обратила его внимание на себя"
    diana "Что вы... Мы благодарим вас, за ваше гостепреимство!"
    sergei "И обязательно...отведаем угощения предложенные вами!"
    medved "Что ж, но это еще не все сюрпризы на сегодня, я ведь правильно понимаю, что вы ищете путь как выбраться из этого леса." 
    medved "Так вот путь тут только один и дорогу к нему знаю лишь я..."
    divan "И что же мы должны будем сделать?"
    medved "Ну во-первых, вы же слышали мелодию которую я играл перед тем как вы вторглись в особняк."
    arkaha "Да..."
    medved "Кто же сможет назвать мне, что это за мелодия, получит от меня запоминающий сюрприз!"
    "???" "{i} Аванюристы начали переглядываться и решать кто же даст правильный ответ"
    sergei "Я знаю, что это была за мелодия."
    sergei "Fredrik Oktel - 2 october."
    medved "Ты же моя умничка, держи презент"
    "???" "{i} Огр подняв свою руку, щелкает пальцем и Дьяволо исчезает с глаз долой"
    diana "Ччччтттооо вы наделали?!"
    if alinaIsAlive: 
        alina "Куда он пропал?"
    elif arinaIsAlive:
        arina "Куда он пропал?"
    else:
        divan "Куда он пропал?"
    "???" "{i} Все прибывали в недоумевании куда же пропал их друг"
    medved "Вернуть своего друга вы сможете лишь одолеете меня угадав все мои загадки приготовленные для одного из вас"
    "???" "{i} И тут Медвед указывает пальцем лишь на одного из всей комнады и это казывается...."
    divan "ЯЯЯЯЯЯЯ? Почему я?"

    show divan:
        xalign 0.53
        yalign 0.7
        zoom 1.4
    "???" "{i} Медвед телепортирует Дивана напротив себя и начинает играть."

    medved "И так. Первый вопрос"
    # вопросы из лаб, стартуем красная армия и т.д.



      


