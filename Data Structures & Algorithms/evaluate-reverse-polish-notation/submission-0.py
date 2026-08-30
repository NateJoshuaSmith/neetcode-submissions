class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for c in tokens:
            if c == '+':
                r, l = stack.pop(), stack.pop()
                stack.append(r + l)
            elif c == '-':
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif c == '/':
                r, l = stack.pop(), stack.pop()
                stack.append(int(l / r))
            elif c == '*':
                r, l = stack.pop(), stack.pop()
                stack.append(r * l)
            else:
                stack.append(int(c))

        return stack[0]

                    



        