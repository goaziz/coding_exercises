from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for i in items:
            if ruleKey == "type" and ruleValue == i[0]:
                count += 1
            elif ruleKey == "color" and ruleValue == i[1]:
                count += 1
            elif ruleKey == "name" and ruleValue == i[2]:
                count += 1
        return count


# other solution
class Solution2:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rules = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        rule = rules[ruleKey]
        for item in items:
            if item[rule] == ruleValue:
                count += 1
        return count
