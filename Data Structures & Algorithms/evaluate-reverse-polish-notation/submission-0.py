class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        we need to check that wre have a t least 2 operands to perform the operation , so as long as the 
        elemtns are integers we keep appending them in the stack 
        mayube we can use isalnum() here for building it 
        then for applyingthe operations 
        we need to have 4 cases 
        but also we need to check the length of the stack to be >= 2 
        then we pop each operand in a dummy variable, apply the operation on it 
        push the reults back and keep the loop 
        """
        stack = []

        for token in tokens:

            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b -a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b /a))
            else:
                stack.append(int(token))
        return stack[0]

           