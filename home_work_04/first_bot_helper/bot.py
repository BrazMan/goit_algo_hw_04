def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contacts(args, contacts):
    if len(args) < 2:
        return "Будь ласка, введіть ім'я та номер телефону."
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return (f"Контакт {name.capitalize()} з номером {phone} додано.")

def change_contact(args, contacts):
    if len(args) < 2:
        return "Будь ласка, введіть ім'я та новий номер телефону." 
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
        return f"Контакт {name.capitalize()} оновлено новим номером {phone}."
    else:
        return f"Контакт {name.capitalize()} не знайдено."

def search_contact(args, contacts):
    try:
        name = args[0]
        name = name.lower()
        if name in contacts:
            return f"Контакт {name.capitalize()}: номер телефону {contacts[name]}."
        else:
            return f"Контакт {name.capitalize()} не знайдено."
    except IndexError:
        return "Будь ласка, введіть ім'я контакту."

def all_contacts(contacts):
    if contacts:
        num_list = [f"{name.capitalize()}: {phone}" for name, phone in contacts.items()]
        return '\n'.join(num_list)
    else:
        return "Список контактів порожній."

def main():
    print("Вас вітає помічник бот!")
    contacts = {}
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)
        match command:
            case "exit":
                print("Вихід з програми. До побачення!")
                break
            case 'hello':
                print("Привіт! Як я можу вам допомогти?")
            case 'help':
                print("Доступні команди: hello, help, exit, add, change, phone, all")
            case 'add':
                print(add_contacts(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(search_contact(args, contacts))
            case 'all':
                print(all_contacts(contacts))
            case _:
                print("Невідома команда. Введіть 'help' для списку доступних команд.")


if __name__ == "__main__":
    main()