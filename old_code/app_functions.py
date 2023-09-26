import os
import re
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

# AI BOT functions


def bot_request(messages):
    """Takes all the messages needed for response in this format:
    [
        {"role": "system", "content": "setting the context"},
        {"role": "user", "content": "user input"},
        {"role": "assistant", "content": "bot reply to keep the context history"},
        {"role": "user", "content": "last user input..."}
    ]"""
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content


def bot_message(role, content):
    """Takes the role and content for bot and put them in the suitable format:
    {"role": "system", "content": "setting the context"}"""
    message = {"role": role, "content": content}
    return message


# INPUT functions


def input_strict(string, list, clear=""):
    """A function to restrict the answers to the given options in the list.
    The function take a message to prompt and a list of valid options.
    Example: input_strict('The message for user: ', ['1','2','x'], 'clear')"""
    while True:
        answer = input(string).lower()
        if answer in [item.lower() for item in list]:
            return answer
        else:
            if clear == "clear":
                os.system("clear")
            print("Please insert just one of the given options.")


# def input_int(string):
#     """A function to prevent string inputs.
#     The function take a message to prompt.
#     Example: input_int('The message for user: ')"""
#     while True:
#         answer = input(string)
#         if answer.isdecimal() and answer != "":  # escape alphas
#             return int(answer)
#         else:
#             print("Please insert only numbers.")


# def input_alfa(string):
#     """A function to restrict inputs to letters and spaces only.
#     The function take a message to prompt.
#     Example: input_alfa('The message for user: ')"""
#     pattern = r"^[a-zA-Z ]*$"
#     while True:
#         answer = input(string)
#         if re.match(pattern, answer) and len(answer) >= 1:
#             return answer
#         else:
#             print("Please insert only letters and 'space'.")


def input_date(string):
    """A function to restrict inputs to date format only.
    The function take a message to prompt.
    Example: input_date('The message for user: ')"""
    pattern = r"^\d{2}\.\d{2}\.\d{4}$"
    while True:
        answer = input(string)
        if re.match(pattern, answer):
            return answer
        else:
            print("Please insert only a valid date in this format dd.mm.yyyy")


def input_email(string):
    """A function to restrict inputs to e-mails only.
    The function take a message to prompt.
    Example: input_email('The message for user: ')"""
    pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    while True:
        answer = input(string)
        if re.match(pattern, answer):
            return answer
        else:
            print("Please insert a valid e-mail address.")
