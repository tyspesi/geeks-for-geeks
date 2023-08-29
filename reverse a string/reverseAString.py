class Solution:
    def reverseWord(self,s):
  
        #Create a temporary array
        temp = []
      
        for x in s:
            temp += x
      
        #get the length of the string
        x = len(temp) - 1
      
      
        tempString = ""
        while x >= 0:
            tempString += temp[x]
            x = x - 1
      
        return(tempString)
        
if __name__ == "__main__":
	s = "Hello World, My name is Ty Spesi"
	ob = Solution()
	print(ob.reverseWord(s))
	
