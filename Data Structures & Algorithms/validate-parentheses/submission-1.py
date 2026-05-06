class Solution:
    def isValid(self, s: str) -> bool:
        """
        PLAN

        Bracket matching is a "most recent unmatched opening" problem — exactly 
        what a stack is for. Walk the string ONCE, character by character. 
        Two-pass approaches don't work here because the order in which closings 
        appear matters: "([)]" has the same multiset of brackets as "()[]" but 
        is invalid. Validity depends on the interleaving, which is only 
        observable as you go.

        For each character c:
          - If c is an opening bracket: push it onto the stack.
          - If c is a closing bracket:
              * If stack is empty, there's no opening to match — return False.
              * If top of stack matches c (correct partner), pop it.
              * Otherwise, mismatch — return False.

        After the loop, the string is valid only if the stack is empty 
        (every opening was closed). If the stack still has entries, 
        we have unclosed openings — return False.

        Time:  O(n) — single pass, O(1) work per character.
        Space: O(n) — stack can hold up to n openings in the worst case 
               (e.g., "(((((").
        """
        stack = []
        n = len(s)
        
        for i in range(n):
            # opening bracket → push and move on
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])

            # closing bracket → must match the most recent unmatched opening
            else:
                # stack empty means there's no opening to close
                if not stack:
                    return False
                # check each closing against its matching opening
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                # any other case = mismatch (e.g., ')' on top of '[')
                else:
                    return False

        # all chars consumed — valid iff every opening got closed
        return not stack