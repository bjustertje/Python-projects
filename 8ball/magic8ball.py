import random

def magic_8_ball():
    responses = [
        "It is certain.",
        "Without a doubt.",
        "You may rely on it.",
        "Yes, definitely.",
        "It is decidedly so.",
        "As I see it, yes.",
        "Most likely.",
        "Yes.",
        "Outlook good.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    input("Ask me a yes/no question: ")
    print("🎱", random.choice(responses))

if __name__ == "__main__":
    magic_8_ball()
