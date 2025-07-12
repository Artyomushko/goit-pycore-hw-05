def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: tuple[str, str], contacts: dict) -> dict:
    name, phone = args
    contacts[name] = phone
    return contacts

def change_contact(args: tuple[str, str], contacts: dict) -> dict:
    name, phone = args

    if name not in contacts:
        raise ValueError('No such contact')

    contacts[name] = phone
    return contacts

def show_phone(args: tuple[str], contacts: dict) -> str:
    name = args[0]

    if name not in contacts:
        raise ValueError('No such contact')

    return contacts[name]

def show_all(args: tuple[str, str], contacts: dict) -> dict:
    return contacts

def main() -> None:
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
            add_contact(args, contacts)
            print("Contact added.")
        elif command == "change":
            try:
                change_contact(args, contacts)
                print("Contact updated.")
            except ValueError as e:
                print(e)
        elif command == "show":
            try:
                print(show_phone(args, contacts))
            except ValueError as e:
                print(e)
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()