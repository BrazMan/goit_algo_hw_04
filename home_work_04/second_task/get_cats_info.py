import pathlib

def get_cats_info(cats_info):
    cats_info = pathlib.Path(cats_info)
    list_dict_cats = []
    try:
        with open(cats_info, 'r', encoding='utf-8') as file:
            file_data = file.readlines()
    except (FileNotFoundError, OSError) as e:
        print(f"Файл не знайдено або неможливо відкрити. Перевірте шлях до файлу. Помилка: {e}")
        return list_dict_cats
    for line in file_data:
        try:
            cat_id, cat_name, cat_age = line.strip().split(',')
        except ValueError:
            print("Некоректний формат рядка у файлі. Пропускаємо цей запис.")
            continue
        try:
            cat_age = int(cat_age)
        except ValueError:
            print(f"Некоректне значення віку для кота з ID {cat_id}: '{cat_age}'. Пропускаємо цей запис.")
            continue
        list_dict_cats.append({
            'iD': cat_id,
            'name': cat_name,
            'age': cat_age
            })

    return list_dict_cats

cats_info = get_cats_info('home_work_04/second_task/cats_info.txt')
print(*cats_info,sep='\n')