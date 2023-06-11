with open('C:\Users\nagovitsin\Desktop\CourseProgrammerSpecialization/file.txt', 'r+') as f:
    text = f.readlines()
    if 'Hello world' not in text:
        f.write('Hello world')

# with open('/Users/daniildudochkin/Downloads/file.txt', 'r+') as f:
#     text = f.readlines()
#     if 'Hello world' not in text:
#         f.write('Hello world')
