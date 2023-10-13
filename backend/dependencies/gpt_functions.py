import openai


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
