def spiralTraversal(mat):
  top = 0; left = 0;
  bottom = len(mat)-1;
  right = len(mat[0])-1;
  
  while (top<=bottom or left <=right):
    moved=False
    # if left not surpassed right 
    # move left to right
    i=left
    if (left<=right and top<=bottom):
      moved=True
      while (i<=right):
        print(mat[top][i])
        i+=1
      top+=1

    # if top not surpassed bottom
    # move top to bottom
    i = top;
    if (top<=bottom and left<=right):
      moved=True
      while (i<=bottom):
        print(mat[i][right])
        i+=1;
      right-=1
    
    # if left not surpassed right
    # move right to left
    i=right
    if (left <= right and top<=bottom):
      moved=True
      while (i>=left):
        print(mat[bottom][i])
        i-=1
      bottom-=1
        
    # if top not surpassed bottom
    # move bottom to top
    i = bottom;
    if (top<=bottom and left<=right):
      moved=True
      while (i>=top):
        print(mat[i][left])
        i-=1
      left+=1


    if not moved: break;

# mat=[
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# mat=[
#   [1,2,3,4],
#   [8,7,6,5]
# ]

# mat=[
#   [1,2,3],
#   [10,11,4],
#   [9,12,5],
#   [8,7,6]
# ]

mat=[
  [1,2],
  [2,3],
  [1,4],
  [0,5],
  [9,6],
  [8,7],
]
spiralTraversal(mat)
