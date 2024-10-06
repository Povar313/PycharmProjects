def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Error processing line: {line}")
                    continue
        if count == 0:
            return (0, 0)
        average = total / count
        return (total, average)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)

path = "/Users/olegpovaarov/PycharmProjects/goit-algo-hw-04/salary_file.txt"
total, average = total_salary(path)


print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


