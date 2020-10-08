"""
    1541. 잃어버린 괄호
"""
expression = input().split('-') # ['55', '50+40']
expression = list(map(lambda x : -sum(map(int, x.split('+'))), expression))
expression[0] = -expression[0]
print(sum(expression))