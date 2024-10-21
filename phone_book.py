from colorama import Fore, Style

COMMANDS = """
    Available commands:
    - hello: Greet the assistant.
    - add <name> <phone>: Add a new contact.
    - change <name> <phone>: Change the phone number of a contact.
    - phone <name>: Get the phone number of a contact.
    - all: List all contacts.
    - help: List available commands.
    - close/exit: Close the assistant.
    """

COMMAND_NAMES = {
    "add": "add",
    "change": "change",
    "phone": "phone",
    "all": "all",
    "help": "help",
    "close": "close",
    "exit": "exit",
}


def input_error(command_name):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                match command_name:
                    case "add":
                        return f"Error in '{command_name}' command: Give me a name and a phone number."
                    case "change":
                        return f"Error in '{command_name}' command: Give me a name and a phone number."
                    case "phone":
                        return f"Error in '{command_name}' command: Enter user nam."
                    case _:
                        return f"Error in '{command_name}' command: Invalid input."
            except IndexError:
                return (
                    f"Error in '{command_name}' command: Not enough arguments provided."
                )
            except KeyError:
                return (
                    f"Error in '{command_name}' command: Contact {args[0]} not found."
                )

        return inner

    return decorator


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(COMMAND_NAMES["add"])
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error(COMMAND_NAMES["change"])
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."


@input_error(COMMAND_NAMES["phone"])
def get_phone(args, contacts):
    return contacts[args[0]]


def get_all_contacts(contacts):
    if len(contacts) == 0:
        return "No contacts found."
    for k, v in contacts.items():
        print(f"{k}: {v}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input(f"{Style.RESET_ALL}Enter a command: ")
        command, *args = parse_input(user_input)
        if command in COMMAND_NAMES:
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(get_phone(args, contacts))
                case "all":
                    get_all_contacts(contacts)
                case "help":
                    print(COMMANDS)
        else:
            print(
                f"{Fore.RED}Invalid command.\n{Style.RESET_ALL}To see all commands available type 'help'"
            )


if __name__ == "__main__":
    main()
