class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # print('bank:',bank)

        ls = []

        for i in range(len(bank)):
            n = self.numberOfDevicesInRow(bank[i])
            if n != 0:
                ls.append(n)
        
        beams = 0
        for i in range(len(ls)-1):
            beams += ls[i] * ls[i+1]
        
        return beams

    def numberOfDevicesInRow(self, row: List[str]) -> int:
        # print('row:', row)

        count = 0
        for pos in row:
            if pos == '1':
                count += 1

        return count

# Runtime
# Details
# 159ms
# Beats 36.73%of users with Python3
# Memory
# Details
# 19.58MB
# Beats 6.86%of users with Python3