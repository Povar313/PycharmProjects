def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                cat_id, name, age = line.split(',')

                cat_info = {
                    'id': cat_id,
                    'name': name,
                    'age': int(age)
                }

                cats_list.append(cat_info)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_list

cats_info = get_cats_info('/Users/olegpovaarov/PycharmProjects/pythonProject3/cats_info')
print(cats_info)