import sys


def get_message(target="GitLab project"):
    return f"Hello, {target}!"


def main(target=None):
    if target is None:
        args = sys.argv[1:]
        target = " ".join(args) if args else "GitLab project"
    print(get_message(target))

if __name__ == "__main__":
    main()
