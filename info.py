info = {
    "name": "Александр Сополев",
    "age": 17,
    "hobbies": "программировать, иногда учиться, кушать пиццу, пить чай и смотреть аниме",
    "interests": "естественными науками и немецким",
    "projects": {1: "Текстовый квест",
                 2: "Фильтр текстов",
                 3: "Консольный фоторедактор"},
    "author": "St1Ng3r"
}
projects_info = {
    info["projects"][1]: "Консольная текстовая квест-игра о побеге из Саратова",
    info["projects"][2]: "Консольное приложение с фильтрами для текста",
    info["projects"][3]: "Редактор изображений с тремя фильтрами"
}


def sort_project_info():
    res = ""
    for i in info["projects"]:
        res += info["projects"][i] + ": " + projects_info[info["projects"][i]] + ".\n"
    return res


def age_count(age):
    if 4 < age < 21:
        age_counting = 0
    elif 110 < age < 115:
        age_counting = 0
    elif 210 < age < 215:
        age_counting = 0
    else:
        age_counting = age % 10
    if age_counting == 1:
        years = "год"
    elif 1 < age_counting < 5:
        years = "года"
    else:
        years = "лет"
    return str(age) + " " + years