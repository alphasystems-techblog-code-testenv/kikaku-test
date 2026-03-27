import sys
import random
from datetime import datetime

GREETINGS = ["Hello", "Hi", "Hey", "Howdy", "Yo", "Bonjour", "Hola", "Ciao"]

FAREWELLS = ["Goodbye", "See you", "Bye", "Adios", "Ciao", "Later"]


def get_greeting(target="GitLab project", lang=None):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word = lang if lang else random.choice(GREETINGS)
    return f"[{now}] {word}, {target}!"


def get_farewell(target="GitLab project"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word = random.choice(FAREWELLS)
    return f"[{now}] {word}, {target}!"


def greet_multiple(*targets):
    if not targets:
        return [get_greeting()]
    return [get_greeting(t) for t in targets]


def count_greetings(*targets):
    return len(targets) if targets else 1


def main(target=None):
    if target is None:
        args = sys.argv[1:]
        if args and args[0] == "--bye":
            targets = args[1:] if len(args) > 1 else [None]
            for t in targets:
                print(get_farewell(t) if t else get_farewell())
        elif args:
            messages = greet_multiple(*args)
            for msg in messages:
                print(msg)
            print(f"--- {count_greetings(*args)} person(s) greeted ---")
        else:
            print(get_greeting())
    else:
        print(get_greeting(target))


if __name__ == "__main__":
    main()
