from termcolor import colored, cprint


if __name__ == '__main__':
    print("Hello World!")
    text = colored("Hello World!", "red", attrs=["reverse", "blink"])
    print(text)
    cprint("Hello World!", "blue", "on_white")

    print(bytes(4))
