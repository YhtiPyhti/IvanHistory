define ivan = Character('Ваня', color="#974141")

define alina_origin = Character('Алина', color="#008800")
define arina_origin = Character('Арина', color="#f5b5db")
define arkaha_origin = Character('Аркаша', color="#e2e956fb")
define diana_origin = Character('Диана', color="#0c8438")
define katia_origin = Character('Катя', color="#72ada9")
define nikita_origin = Character('Никита', color="#0bd80b")
define roma_origin = Character('Рома', color="#b48e05")
define sergei_origin = Character('Сергей', color="#b41405")

label hospital:
    play music "bolnica.mp3" fadein 1 
    show bg black_screen with fade
    "Кажется он приходит в себя!"
    show bg black_screen with fade
    "Иван!!!"
    show bg hospital:
        xzoom 1.3
    with fade

    show ivan:
        xalign 0.8
        yalign 0.8
        rotate 65
        zoom 0.9
    if isNikitaAlive==False:
        show nikita_arkaha:
            zoom 0.2
            xalign 0.8
            yalign 0.8
            xzoom -1
    else:
        show arkaha:
            xalign 0.9
            yalign 0.9
            zoom 0.9
        show nikitanesmog:
            xalign 0.2
            yalign 0.45
            rotate 30
    show alina:
        xalign 0.0
        yalign 0.5
        zoom 0.7
    show arina:
        xalign -0.1
        yalign 0.5
        zoom 0.7
    show katia:
        xalign 0.95
        yalign 0.6
        zoom 1.1
    show sergei:
        xalign 1.0
        yalign 0.8
        zoom 0.2   
    show diana:
        xalign 0.9
        yalign 0.8 
    show roma:
        zoom 0.7
        xalign 0.0
        yalign 0.5
    diana_origin "Ты проснулся! Наконец-то! Мы так переживали!"
    sergei_origin "С днём рождения, дорогой! Мы так рады тебя видеть!"
    ivan  "Где я…? Что происходит?"
    roma_origin "Ты в больнице, друг. Ты был в коме… Но сейчас всё хорошо! Поздравляем тебя с днём рождения!"
    arina_origin "Да, да! Ты не представляешь, как мы ждали этого момента. Мы даже торт принесли!"
    ivan  "Торт? Для кого?"
    if isNikitaAlive:
        nikita_origin "Мнём жжжениовф!!!"
    alina_origin "Для тебя! Мы все здесь, чтобы отметить твой день!"
    arkaha_origin "Ты даже не представляешь, сколько всего произошло, пока тебя не было. Готовься к куче новостей!"
    ivan "Я… я всё равно не понимаю. Как я мог…"
    diana_origin "Не переживай, мы всё расскажем. Главное — ты с нами, и ты снова жив!"
    arkaha_origin "Да, и мы обещаем, что каждый твой день рождения будет особенным. Этот — уже точно незабываемый!"
    ivan  "Я столько пропустил…"
    roma_origin "Это не важно. Важно, что ты здесь, и мы с тобой. Давай отметим это вместе!"
    sergei_origin "Теперь задувай свечи и загадывай желание!"
    ivan "Хорошо… Я хочу, чтобы все были счастливы."
    "Все вместе" "С Днём Рождения!!!"
    historyman "Иван задувает свечи, друзья аплодируют, атмосфера наполняется радостью и надеждой."