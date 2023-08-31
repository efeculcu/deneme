import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emoji()
    emoji = [":)", ":(", ":\", ":\"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 3)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
