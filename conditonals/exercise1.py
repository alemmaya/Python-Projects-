"""
- Ask the user for their name and display a greeting. Then, in a new line, echo the name back in all capitals
    > user's input: 'Marcus'
    > output: 'Greetings Marcus'
    > output: '...MARCUS...'
"""

name = input('what is your name?')

print(f'Greetings, {name}!')
print(f'...{name.upper()}...')