class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        PLAN

        Reverse Polish Notation: operators come AFTER their operands. 
        Example: "3 4 +" means 3 + 4. "5 1 2 + 4 * + 3 -" means 5 + ((1+2) * 4) - 3.

        A stack is the natural fit. Walk tokens left to right:
          - Number token → push it.
          - Operator token → pop the top TWO values, apply the operator, push 
            the result.

        Why this works: in valid RPN, an operator's operands are always the most 
        recent values on the stack. The stack ends with exactly one element — 
        the final answer.

        ORDER MATTERS for - and /:
          - First pop = right operand (most recent).
          - Second pop = left operand.
          - Compute as: left OP right.
        For + and *, order doesn't matter (commutative).

        DIVISION GOTCHA:
          The problem requires truncation toward zero. Python's // is FLOOR 
          division (rounds toward -∞), which differs for negatives:
              -7 // 2     == -4   (floor)
              int(-7 / 2) == -3   (truncate toward zero)  ← what we need
          So use int(left / right), NOT left // right.

        No length checks needed: the problem guarantees a valid RPN expression, 
        so every operator is reached with ≥ 2 operands already on the stack.

        Time:  O(n) — single pass, O(1) work per token.
        Space: O(n) — stack holds up to ~n/2 numbers in the worst case.
        """
        stack = []

        for token in tokens:
            # commutative ops — pop order doesn't matter
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            # non-commutative ops — first pop is the RIGHT operand
            elif token == "-":
                a, b = stack.pop(), stack.pop()   # a = right, b = left
                stack.append(b - a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()   # a = right, b = left
                # int(b / a) truncates toward zero (not floor like //)
                stack.append(int(b / a))
            
            # not an operator → must be a number; convert and push
            # (int() handles negative numbers like "-5" correctly,
            # which is why we don't use isalnum() to detect numbers)
            else:
                stack.append(int(token))

        # exactly one value remains: the result
        return stack[0]