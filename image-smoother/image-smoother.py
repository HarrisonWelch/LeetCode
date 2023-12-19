import math

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        retImg = []
        m = len(img)
        n = len(img[0])
        
        if m == 1 and n == 1:
            return img

        for i in range(m):
            retImg.append([0] * len(img[0]))

        if m == 1:
            # Horizontal Line
            retImg[0][0] = math.floor((img[0][0] + img[0][1]) / 2)

            for i in range(1, n-1):
                retImg[0][i] = math.floor(( \
                    img[0][i-1] + \
                    img[0][i] + \
                    img[0][i+1] \
                ) / 3)

            retImg[0][n-1] = math.floor((img[0][n-2] + img[0][n-1]) / 2)
            return retImg
        
        if n == 1:

            # Vertical Line
            retImg[0][0] = math.floor((img[0][0] + img[1][0]) / 2)

            for i in range(1, m-1):
                retImg[i][0] = math.floor(( \
                    img[i-1][0] + \
                    img[i][0] + \
                    img[i+1][0] \
                ) / 3)

            retImg[m-1][0] = math.floor((img[m-2][0] + img[m-1][0]) / 2)
            return retImg

        # TL corner
        retImg[0][0] = math.floor(( \
            img[0][0] + img[0][1] + \
            img[1][0] + img[1][1]) / 4)
        
        # TR corner
        retImg[0][n-1] = math.floor(( \
            img[0][n-2] + img[0][n-1] + \
            img[1][n-2] + img[1][n-1]) / 4)

        # BL corner
        retImg[m-1][0] = math.floor(( \
            img[m-2][0] + img[m-2][1] + \
            img[m-1][0] + img[m-1][1]) / 4)
        
        # BR corner
        retImg[m-1][n-1] = math.floor(( \
            img[m-2][n-2] + img[m-2][n-1] + \
            img[m-1][n-2] + img[m-1][n-1]) / 4)

        # Top side
        for i in range(1, n-1):
            retImg[0][i] = math.floor(( \
                img[0][i-1] + img[0][i] + img[0][i+1] + \
                img[1][i-1] + img[1][i] + img[1][i+1] \
            ) / 6)

        # Bottom side
        for i in range(1, n-1):
            retImg[m-1][i] = math.floor(( \
                img[m-2][i-1] + img[m-2][i] + img[m-2][i+1] + \
                img[m-1][i-1] + img[m-1][i] + img[m-1][i+1] \
            ) / 6)

        # Left side
        for i in range(1, m-1):
            retImg[i][0] = math.floor(( \
                img[i-1][0] + img[i-1][1] + \
                img[i][0] + img[i][1] + \
                img[i+1][0] + img[i+1][1] \
            ) / 6)

        # Right side
        for i in range(1, m-1):
            retImg[i][n-1] = math.floor(( \
                img[i-1][n-2] + img[i-1][n-1] + \
                img[i][n-2] + img[i][n-1] + \
                img[i+1][n-2] + img[i+1][n-1] \
            ) / 6)

        # Internal
        for i in range(1, len(img) - 1):
            for j in range(1, len(img[i]) - 1):
                total = \
                    img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + \
                    img[i][j-1] + img[i][j] + img[i][j+1] + \
                    img[i+1][j-1] + img[i+1][j] + img[i+1][j+1]
                retImg[i][j] = math.floor(total/9)
            # print(retImg)
        
        return retImg