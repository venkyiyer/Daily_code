class Solution:
    def interpret(self, command: str):
        x = command.replace('()', 'o')
        x = x.replace('(al)', 'al')
        return x