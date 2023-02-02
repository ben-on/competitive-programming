class Solution:
    under20=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
             "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen",
             "Eighteen","Nineteen"]
    tens=["","Ten","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    places=["Hundred","Thousand","Million","Billion"]

    def numberToWords(self, num: int) -> str:
        return("Zero" if num == 0 else ' '.join(filter(None,self.evaluate(num))))
    
    def evaluate(self,num):
        if num < 20:
            return [self.under20[num]]
        elif num < 100:
            return [self.tens[num//10]]+self.evaluate(num%10)
        elif num < 1000:
            return self.evaluate(num//100)+[self.places[0]]+self.evaluate(num%100)
        elif num < 1000000: #thousands
            return self.evaluate(num//1000)+[self.places[1]]+self.evaluate(num%1000)
        elif num < 1000000000: #millions
            return self.evaluate(num//1000000)+[self.places[2]]+self.evaluate(num%1000000)     
        else: #billions
            return self.evaluate(num//1000000000)+[self.places[3]]+self.evaluate(num%1000000000) 
    