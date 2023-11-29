class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        pathList = path.split('/')
        for i in pathList:
            if i == '' or i == '.':
                continue
            if i == '..':
                if result:
                    result.pop()
            else:
                result.append(i)

        return '/' + '/'.join(result)