
label forest:
    play music "lec.mp3" fadein 1
    #Предысловие после боя
    "???" "{i}Героям удалось одержать победу в этом сражении. Но не все из них смогут насладиться этим."

    if alinaIsAlive == False and arinaIsAlive == False:

        "???" "{i}Тола была подла атакована в спину, а Кэрри стала жертвой несчастного случая."
   
    elif alinaIsAlive == False and arinaIsAlive:

        "???" "{i}К сожалению, Тола была подла атакована в спину, и получила смертельные раны."
    
    elif alinaIsAlive and arinaIsAlive == False:  

        "???" "{i}К сожалению, Кэрри стала жертвой несчастного случая, и получила смертельные раны."

    #Обсуждения после боя
    divan "Это конец?"
    sergei "Наконец-то мы справились"
    nikita "Ква-ква"
    arkaha "Это был тяжелый бой"
    katia "Да, это было невероятно! Я думала, что мы не справимся, когда Архипелаг начала атаку" 
    diana "Хорошо, что справились, но, если бы не Диван, этого сражения и не произошло бы!"
    sergei "Да, Диван. Что на тебя нашло? {w} Ты спровоцировал Архипелаг с её прихвостнями. {w}Потерял сознание в самом начале боя. {w}Ещё и все сражение был бесполезен"

    if alinaIsAlive == False and arinaIsAlive == False:
     
        roma "Мы победили, но какой ценой. Два наших товарища мертвы, и всё из-за тебя, Диван!"
        divan "Я не хотел, чтобы так вышло..."
        diana "Ты знал, что ты делаешь! Если бы ты не допустил этого, они были бы ЖИВЫ!"
        roma "Кэри была моим другом! Ты представляешь как мне больно сейчас?"
        sergei "Мы все рисковали, но ты был слишком беспечен! Подставился сам, подставил Толу, еще и Кэрри..."
        nikita "Ква-ква!"
        divan "Я-я... {w}я не хотел...{w} Я растерялся"
        roma "Мы потеряли их, и ты просто продолжаешь оправдываться. Как нам теперь тебе доверять?"
        arkaha "Возможно, сейчас не время для обвинений, но мы должны разобраться с этим.{w} Мы должны помнить их, а не давить друг на друга."
    
    elif alinaIsAlive == False and arinaIsAlive:

        roma "Мы победили, но какой ценой. Наш товарищ мертв, и всё из-за тебя, Диван!"
        divan "Я не хотел, чтобы так вышло..."
        roma "Ты знал, что ты делаешь! Если бы ты не допустил этого, она была бы ЖИВА!"
        diana "Кэри была моим другом! Ты представляешь как мне больно сейчас?"
        sergei "Мы все рисковали, но ты был слишком беспечен! Зачем было её отталкивать?!"
        alina "Ты должен был просто схватить её!"
        nikita "Ква-ква!"
        divan "Я-я... {w}я не хотел...{w} Я растерялся"
        roma "Мы потеряли её, и ты просто продолжаешь оправдываться. Как нам теперь тебе доверять?"
        arkaha "Возможно, сейчас не время для обвинений, но мы должны разобраться с этим.{w} Мы должны помнить её, а не давить друг на друга."

    elif alinaIsAlive  and arinaIsAlive == False:

        roma "Мы победили, но какой ценой. Наш товарищ мертв, и всё из-за тебя, Диван!"
        divan "Я не хотел, чтобы так вышло..."
        diana "Ты знал, что ты делаешь! Если бы ты не допустил этого, она была бы ЖИВА!"
        roma "Кэри была моим другом! Ты представляешь как мне больно сейчас?"
        sergei "Мы все рисковали, но ты был слишком беспечен! Почему ты оставил Толу одну?!"
        arina "Она тебя вылечила, а ты как ей отплатил?!"
        nikita "Ква-ква!"
        divan "Я-я... {w}я не хотел...{w} Я растерялся"
        roma "Мы потеряли её, и ты просто продолжаешь оправдываться. Как нам теперь тебе доверять?"
        arkaha "Возможно, сейчас не время для обвинений, но мы должны разобраться с этим.{w} Мы должны помнить её, а не давить друг на друга."

    "???" "{i}Обсуждения продолжает нагнетаться, но в конце концов герои понимают, что им нужно найти способ работать вместе, чтобы справится с горем и двигаться вперед."
   
    scene bg lec doroga with fade
    "???" "{i}Идя по лесу, герои сталкиваются с магическими существами: феи, духи и т.д."
    "???" "{i}Чем больше они идут в глубь леса, тем гуще становиться туман, и каждый шаг отзывается странным шорохом..."
    "???" "{i}Деревья стали выглядят как живые существа, их ветви скрипят, будто шепчут что-то..."
    "???" "{i}Луна полностью скрылась за облаками и туманом, единственным источником света стали светлячки."
    
    scene bg lec lager with fade
    "???" "{i}Спустя несколько часов плутания по лесу, герои решают сделать привал под большим деревом."
    "???" "{i}Разбив лагерь, герои распределили задачи."
    "???" "{i}Слиппи и Флирт отправились за добычей еды и воды. Кити и Ирида пошли собирать хворост"
    "???" "{i}Все остальные остались в лагере."
    "???" "{i}Спустя несколько часов из леса выходят Кити и Ирида с интересными новостями."
    katia "Мы заметили странный старинный особняк в километрах трех от лагеря."
    diana "Можно завтра осмотреть его, вдруг там такие же бедняги, как и мы... может вообще найдем подсказку, как нам выбраться."
    arkaha "Ништяк, так и поступим"
    "???" "{i}Большинство поддержали идею пойти в особняк."
    nikita "КВА-ква-ква-КВА!?"
    roma "ДА ВСЕМ ПОХЕР, ХОЧЕШЬ ТЫ ИДТИ ИЛИ НЕТ, МОЖЕШЬ ТУТ ОСТАТЬСЯ!"
    $renpy.notify("Судьба изменина")
    "???" "{i}Приготовив еду и залатав раны, герои составили план дежурства."
    if alinaIsAlive and arinaIsAlive:
        alina "Спасибо, что спас меня и Кэрри. Не было возможности раньше поблагодарить. Если бы не ты..."
        arina "Да, если бы ты не помог нам, возможно мы бы уже были мертвы"
        divan "Так поступил бы каждый! Не стоит благодарить. Ладно я пойду спать, через несколько часов моя со Слиппи смена."
        arina "Спасибо!"
    elif arinaIsAlive:
        arina "Спасибо, что спас меня. Не было возможности раньше поблагодарить. Если бы не ты..."
        divan "Так поступил бы каждый! Не стоит благодарить. Ладно я пойду спать, через несколько часов моя со Слиппи смена."
        arina "Спасибо!"
    elif alinaIsAlive:
        alina "Спасибо, что спас меня. Не было возможности раньше поблагодарить. Если бы не ты..."
        divan "Так поступил бы каждый! Не стоит благодарить. Ладно я пойду спать, через несколько часов моя со Слиппи смена."
        alina "Спасибо!"

    show slippi:
        xalign 0.8
        yalign 0.63
        zoom 1.6
    show divan:
        xalign 0.71
        yalign 0.68
    
    nikita "Ква-ква"
    divan "Мммм"
    nikita "Ква-ква!"
    divan "Отстань"
    nikita "КВА-КВА!"
    divan "Уже наша очередь?"
    nikita "Ква"
    divan "Хорошо, дай мне пять минут, и я выйду"
    play music "lager.mp3" fadein 1
    show slippi:
        xalign 0.53
        yalign 0.73
        zoom 1.6
    with move

    "???" "{i}Спустя пять минут"
    
    show divan:
        xalign 0.73
        yalign 0.73
        zoom 1.6
    with move

    nikita "Ква-ква"
    divan "Что со мной было? Я...я сам не знаю...наверное меня слишком сильно приложила Архипелаг."
    nikita "Ква-ква-ква-ква"
    divan "Да нет я все тот же, просто...просто...да сильно ударился головой, хех."
    ivan "Как я вообще понимаю его??? Он же лягушка и просто квакает!?"
    divan "Слушай, а...а, что мы вообще здесь делаем?"
    nikita "Ква-ква-КВА-ква-кВа"
    divan "Нас перенесло сюда порталом? И теперь мы блуждаем здесь уже больше недели!"
    ivan "ВОТ ДЕРЬМО!!!"

    "???" "{i}После этого повисла тишина"
    "???" "{i}Ее разорвал тяжелый выдох Дивана"

    nikita "Ква?"

    if alinaIsAlive and arinaIsAlive:
        divan "А ты видел быть может, как Тола ловко прихерачила этого чувырлу в кустах это было филигранно"
        nikita "КВАААААА?"
        divan "Да я сам офигел, но если бы я не решил осмотреться, все могло закончится печально..."
        divan "Но Архипелага приложили мы знатно, на сколько эта сучка была в себе уверена и в своих прихвостнях даже как-то жалко ее..."
        nikita "ква-ква-ква-ква-ква-ква-КВА!"
        divan "Ты прав, таких жалеть не нужно, но душнить было не обязательно, Никит..."
        nikita "ккКВАА?"
        divan "Ой, Слиппи, что ж давай выпьем этого прекрасного на вкус эля за победу, но завтра нас ждут новые приключения!"
        "???" "{i}Допив эль, ребята продолжили дежурить в полном молчании и лишь изредка обсуждая душные факты из жизни лягушек."

    elif alinaIsAlive and arinaIsAlive == False:
        divan "Я не могу поверить, что ее больше нет. Это все из-за меня..."
        nikita "Ква-ква..."
        divan "Если бы я только был более аккуратен, рассчитал бы свои силы... Но я не смог, я не справился и лишь только из-за меня мы потеряли товарища"
        divan "Арина..."
        nikita "Ква?"
        divan "Ну, эм-м, в-в смысли Кэри"
        "???" "{i}Слиппи отводит глаза и делает тяжелый вздох"
        nikita "Ква-ква...ква. Ква-ква-ква-Ква-Ква!"
        "???" "{i}Слиппи подсаживается ближе"
        nikita "ква-КВА"
        "???" "{i}Слиппи хочет приобнять своего товарища, но тут же вспоминает, что он ядовит и одно его касание сразу же убьет Дивана"
        divan "Каждый раз, когда я закрываю глаза, я вижу, как Ари.... Кэри медленно закрывает свои глаза. И эта картинка никак не уходит из моей головы…"
        "???" "{i}Тут же после столь откровенного диалога между товарищами, Слиппи подносит кубок с элем Дивану, тем самым предлагая выпить за ушедшую душу."
        "???" "{i}Допив эль, ребята продолжили дежурить в полном молчании и лишь изредка обсуждая душные факты из жизни лягушек."
    
    elif alinaIsAlive == False and arinaIsAlive:
        divan "Я не могу поверить, что ее больше нет. Это все из-за меня..."
        nikita "Ква-ква..."
        divan "Если бы я только осмотрелся, пригляделся бы к тем кустам... Она лечила меня…"
        divan "Алина..."
        nikita "Ква?"
        divan "Ну, эм-м, в-в смысли Тола"
        "???" "{i}Слиппи отводит глаза и делает тяжелый вздох"
        nikita "Ква-ква...ква. Ква-ква-ква-Ква-Ква!"
        "???" "{i}Слиппи подсаживается ближе"
        nikita "ква-КВА"
        "???" "{i}Слиппи хочет приобнять своего товарища, но тут же вспоминает, что он ядовит и одно его касание сразу же убьет Дивана"
        divan "Я уверен, что я должен был быть куда внимательнее и смелее в своих действиях и быть может все вышло бы иначе. Каждый раз, когда я закрываю глаза, я вижу, как Али.... Тола лежит, истекая кровью. Это не уходит…"
        "???" "{i}Тут же после столь откровенного диалога между товарищами, Слиппи подносит кубок с элем Дивану, тем самым предлагая выпить за ушедшую душу."
        "???" "{i}Допив эль, ребята продолжили дежурить в полном молчании и лишь изредка обсуждая душные факты из жизни лягушек."
    else:
        divan "Я не могу поверить, что их больше нет. Это все из-за меня..."
        nikita "Ква-ква..."
        divan "Если бы я только осмотрелся, пригляделся бы к тем кустам... Она лечила меня…"
        divan "Алина..."
        nikita "Ква?"
        divan "Ну, эм-м, в-в смысли Тола"
        nikita "Ква-ква-ква-ква"
        divan "А как же Кэри... Тут виноват только я, ПОНИМАЕШЬ, Я!"
        "???" "{i}Слиппи отводит глаза и делает тяжелый вздох"
        nikita "Ква-ква...ква. Ква-ква-ква-Ква-Ква!"
        "???" "{i}Слиппи подсаживается ближе"
        nikita "ква-КВА"
        "???" "{i}Слиппи хочет приобнять своего товарища, но тут же вспоминает, что он ядовит и одно его касание сразу же убьёт Дивана"
        divan "Я уверен, что я должен был быть куда осторожнее со своими действиями и быть может все вышло бы иначе. Каждый раз, когда я закрываю глаза, я вижу, как Ари.... Кэри уходит в глубокий смертный сон. Это не уходит…"
        "???" "{i}Тут же после столь откровенного диалога между товарищами, Слиппи подносит кубок с элем Дивану, тем самым предлагая выпить за ушедшие души."
        "???" "{i}Допив эль, ребята продолжили дежурить в полном молчании и лишь изредка обсуждая душные факты из жизни лягушек."
    
    nikita "КвА-кВа?"
    divan "Да, ты прав, пора будить следующих, а то время позднее..."
    "???" "{i}Авантюристы поочередно продолжали дежурить целую ночь и вот уже близилось время к утру, а это означало одно, что пора собирать свои вещи и отправляться к тому самому особняку."

    jump ocobniak