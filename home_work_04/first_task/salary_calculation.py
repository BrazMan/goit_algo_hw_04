import pathlib


workers_info_path = pathlib.Path(__file__).parent / 'workers_info.txt'



def total_salary(workers_data):
    total_salary_num = 0
    valid_workers = 0
    try:
        with workers_data.open("r", encoding="utf-8") as file:
            workers_data = file.readlines()
            workers_data = [line.strip() for line in workers_data]
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return 0, 0
    
    if not workers_data:
        print("Файл порожній.")
        return 0, 0
    

    for worker in workers_data:
        try:
            worker_data = worker.split(',')
            salary = float(worker_data[1])
            total_salary_num += salary
            valid_workers += 1
        except (IndexError, ValueError):
            print(f"Некоректні дані для працівника: {worker}")
            continue

    avg_salary = total_salary_num / valid_workers

    return total_salary_num, avg_salary

total, avarage = total_salary(workers_info_path)
print(f'Загальний дохід: {total}\n'
      f'Середня заробітна плата: {avarage}')
    
    
    

