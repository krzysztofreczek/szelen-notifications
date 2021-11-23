import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def add_two_numbers(n1, n2):
    return n1 + n2


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    v = add_two_numbers(1, 20)
    notify('Szelen update:', 'result is:' + str(v))
