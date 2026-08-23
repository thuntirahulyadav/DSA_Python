def pascal_triangle(num_rows):
   triangle=[]
   for row in range(num_rows):
     curr_row = [1]*(row + 1)
     for j in range(1,row):
        curr_row[j]= triangle[row-1][j-1] + triangle[row-1][j]
     triangle.append(curr_row)
   return triangle
print(pascal_triangle(5))