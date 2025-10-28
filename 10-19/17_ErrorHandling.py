# Error Handling in Python
try:
    print(1/0)
    print('Hello')
except ZeroDivisionError:
    print('**Error happened!**')
    # import traceback
    # print(traceback.format_exc())

print('The End.')