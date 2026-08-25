class solution:
    def stock_B_S(self,prices)->int:
      min_price=float('inf')
      max_profit=0
      for price in prices:
        min_price=min(min_price,price)
        max_profit=max(max_profit,price - min_price)
      return max_profit  
sol=solution()
prices=[7,1,6,4,3,2]
print(sol.stock_B_S(prices))