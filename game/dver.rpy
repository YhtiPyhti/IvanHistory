
label dver:
    
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
        