"""
Перевести строку "it_step_course" из snake_case в camelCase
"""


snake_str = "it_step_course"

parts = snake_str.split('_')
camelCase = parts[0] + ''.join(word.capitalize() for word in parts[1:])

print(camelCase)