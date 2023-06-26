# note for the future. . . this is a shit code, improve it when you get good 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        print("hih")
        if len(prices) < 2:
            return 0
        profite = [prices[0],prices[1]]

        if len(prices) >= 3:
            pointer = 2
            while pointer < len(prices):
                p3 = prices[pointer]
                pset = [ p3 - profite[0], p3 - profite[1], profite[1]-profite[0]]
                if max(pset) == pset[0] :
                    profite[1] = p3

                elif max(pset) == pset[1] :
                    profite[0] = profite[1]
                    profite[1] = p3
                
                if p3 < profite[0] and len(profite) == 2:
                    profite.append(p3)
                    
                if len(profite) == 3:
                    if p3 < profite[2]:
                        profite[2] = p3

                if len(profite) == 3 and ((p3 - profite[2]) > max(pset)):
                    profite[0]=profite[2]
                    profite[1] = p3
    
                pointer +=1



        if (profite[1] - profite[0]) > 0:
            return profite[1] - profite[0]
        else:
            return 0
