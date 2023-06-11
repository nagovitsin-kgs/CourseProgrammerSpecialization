with open('file.txt', 'r+') as file:
    text = file.readlines()
    if 'Hello world' not in text:
        file.write('\nHello world')
print(text)
# with open('/Users/daniildudochkin/Downloads/file.txt', 'r+') as f:
#     text = f.readlines()
#     if 'Hello world' not in text:
#         f.write('Hello world')
