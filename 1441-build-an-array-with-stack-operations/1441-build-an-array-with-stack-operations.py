class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_index = 0
        operations = []

        for i in range(1, n + 1):
            operations.append("Push")

            if i == target[target_index]:
                target_index += 1
                if target_index == len(target):
                    break
            else:
                operations.append("Pop")

        return operations