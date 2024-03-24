
def input_error(func):
    def inner(*args, **kwargs):
        try:
            # Перевірка аргументів перед викликом функції
            if func.__name__ in ["add_contact", "change_contact"]:
                if len(args[0]) != 2:  # args[0] тут це список аргументів
                    return "Give me name and phone please."
            elif func.__name__ == "phone_username":
                if len(args[0]) != 1:
                    return "Enter the name for the command."

            result = func(*args, **kwargs)
            if result is None:  # Специфічна логіка для функції, яка може повернути None
                return "Contact not found."
            return result
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter the argument for the command."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return  # Використання return без значення вказує на помилку
    contacts[name] = phone
    return "Contact changed."


@input_error
def phone_username(args, contacts):
    name = args[0]
    return contacts.get(name)  # .get() поверне None, якщо ключ не знайдений


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change_username_phone":
            print(change_contact(args, contacts))
        elif command == "phone_username":
            print(phone_username(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()