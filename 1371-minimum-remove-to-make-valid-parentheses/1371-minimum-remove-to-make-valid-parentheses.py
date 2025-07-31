class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for index, char in enumerate(s):
            if char not in "()":
                continue
            if char=="(":
                stack.append(index)
            elif not stack:
                indexes_to_remove.add(index)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for index,char in enumerate(s):
            if index not in indexes_to_remove:
                string_builder.append(char)
        return "".join(string_builder)