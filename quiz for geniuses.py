print("#Является ли объект большим, красным, жёлтым, фруктом?")

red_answer = input("красный? да/нет - ")
red = (red_answer == 'да')
red_no = (red_answer == "нет" == print("возможно желтый…"))

big_answer = input("большой? да/нет - ")
big = (big_answer == 'нет')
big_yes = (big_answer == 'да' == print("возможно он маленький…"))

fruit_answer = input("фрукт? да/нет - ")
fruit = (fruit_answer == 'нет')
fruit_yes = (fruit_answer == 'да' == print("возможно это не фрукт…"))

yellow_answer = input("желтый? да/нет - ")
yellow = (yellow_answer == 'да')
yellow_no = (yellow_answer == "нет" == print("Эээ…"))
if red and big and fruit and yellow:
    print("Правильно! Это кортофель")
else:
    print("Неправильно!")
    small_answer = input("маленький? да/нет - ")
    small = (small_answer == "да")
    small_no = (small_answer == "нет" == "да")
    if big and not red and not yellow or small and not yellow and fruit:
        print("Плод дракона")
    else:
        print("НЕ плод дракона(")
        red_fruit_answer = input("красный фрукт? да/нет - ")
        red_fruit = (red_fruit_answer == "да")
        red_fruit_no = (red_fruit_answer == "нет" == "да" == print("Нуууу вообще-то да?.."))

        yellow_fruit_answer = input("жёлтый фрукт? да/нет - ")
        yellow_fruit = (yellow_fruit_answer == "да")
        yellow_fruit_no = (yellow_fruit_answer == "нет" == "да" == print("Ты чё дальтоник?! Он же жёлтый =/"))
        if big and red_fruit or big and yellow_fruit or small and red_fruit or small and yellow_fruit:
            print("Загадка...")
        else:
            print("...")