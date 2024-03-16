def func(message):
    msg = message.split()
    print(msg)
    if msg[1].isdigit():
        digit_len = len(msg[1]) + 1
        tags = message[5 + digit_len:]
        return tags
msg = 'tags 20 score:>100 rating:e is:jpg status:deleted yuri dick'
print(func(msg))
