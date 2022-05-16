grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
         
#'''
sol =  [ [ 3, 1, 6 ,5, 7 ,8 ,4, 9 ,2],
            [ 5, 2, 9 , 1 ,3 ,4 ,7 ,6 ,8],
            [ 4 ,8 ,7, 6 ,2 ,9 ,5 ,3 ,1],
            [ 2 ,6 ,3 ,4 ,1 ,5 ,9, 8 ,7],
            [ 9 ,7 ,4 ,8 ,6 ,3 ,1 ,2 ,5],
            [ 8 ,5 ,1, 7 ,9 ,2 ,6 ,4, 3],
            [ 1 ,3 ,8, 9 ,4 ,7 ,2 ,5 ,6],
            [ 6 ,9, 2 ,3 ,5, 1 ,8 ,7 ,4],
            [ 7 ,4 ,5 ,2 ,8 ,6 ,3 ,1 ,9] ]
         
#'''
'''
a =[[1,2,3,4,5,6,7,8,9],
      [9,8,7,6,5,4,3,2,1],
      [3,6,5,7,2,4,9,8,1]]
'''
# Function to check Duplicates in given row 

def checkrow(arr,row,num):
	for i in range(9):
		if arr[row][i] ==num:
			return False
	return True

# Function to check Duplicates in given Column

def checkcol(arr,col,num):
	colval =[]
	for i in range(9):
		colval.append(arr[i][col])
	
	for i in colval:
		if i ==num:
			return False
	
	return True
		
# function to check duplicates in current 3 By 3 Matrix

def threebythreematrix(arr,r,c,num):
	for i in range(r,r+3):
		for j in range(c,c+3):
			if arr[i][j] ==num:
				return False				
	return True
	

# Function to check if Board if valid for
#given guess it returns a dictionary  with
#value if row passed , column passed and
#3by3 matrix passed and sum based on
#three checks if sum ==3 it means board
#is valid

def valid(arr,row,col,guess):
	res={}
	res['sum']=0
		
	testRow =checkrow(arr,row,guess)
	if testRow ==False:
		#return False
		res['row'] ="fail"
		
	else:
		res['row']='pass'
		res['sum'] +=1
				
	testColumn =checkcol(arr,col,guess)
	if testColumn ==False:
		#return False
		res['col']='fail'
	else:
		res['col']='pass'
		res['sum'] += 1
			
	rowStart =(row//3) * 3
	colStart =(col//3) * 3
		
	test3by3matrix = threebythreematrix(arr,rowStart,colStart,guess)
	
	if test3by3matrix ==False:
		#return False
		res['matrix']='fail'
	else:
		res['matrix']='pass'
		res['sum'] += 1
			
	#return True
	return res
	


#testR =checkrow(a,0,0)
#print("Row",testR)

#testC = checkcol(a,0,9)

#print("column",testC)

#testM =threebythreematrix(a,0,3,8)
#print("3 x 3 matrix", testM)
print()	
#testB = valid(a,0,3,0)
#for key , value in testB.items():
#	print(key,value)
#print("test Board",testB)




# a utility function that prints all empty value (0) in 9 x 9 matrix
	
def allempty(board):		
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				print(i,j,board[i][j])	
	
#a utility function that returns next empty spot in a 9x9 matrix

def nextempty(board):
	for r in range(9):
		for c in range(9):
			if board[r][c] == 0 :
				return r,c
	return None,None

#a utility function that prints 9x9 matrix
def printBoard(board):
	for I in range(9):
			for j in range(9):
				print(board[I][j],end="  ")
			print()
			
# function that  solves Sudoku using backtracking
		
def SudokuSolver(board):
			
			#Step 1 : find first empty spot
			row , column = nextempty(board)
			
			#step 2: if there is no empty spot return true ie, puzzle solved
			
			if row ==None:
				return True
			
			#Step 3: get guess fro 1 to 9 and check if for our guess board holds true
			
			for guess in range(1,10):
				isvalid = valid(board,row,column,guess)
				if isvalid['sum']==3:
					#step 4 if board is valid for guess insert guess in empty spot
					board[row][column]=guess	
					
					# step 5 pass new board recursively to check next combination
					# if it returns true puzzle is solved 	
					if SudokuSolver(board):
						return True
				#step 6 if puzzle is not solved for that guess reset the empty spot 
				board[row][column]=0
				
			#step 7  : at end of loop our
#function checked every possible#
#combination , and it still not returned True
#it means given puzzle is unsolvable hence
#return false			
			return False
			
#allempty(grid)
print()			
printBoard(grid)
solved = SudokuSolver(grid)
print()
print(solved)
print()
printBoard(grid)

#r,c =nextempty(grid)
#print(r,c)
#print(grid[r][c])
			

				
#allempty(grid)



