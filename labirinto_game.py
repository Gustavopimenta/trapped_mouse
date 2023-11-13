# Python3 program to solve Rat in a maze
# problem with backtracking using stack

N=4
M=5

class node:
	def __init__(self,i,j):
		self.x=i
		self.y=j
		self.dirn=0

# maze of n*m matrix
n = N; m = M

# Coordinates of food
fx=0; fy=0
visited=[[True]*N for _ in range(M)]

def isReachable(maze):

	# Initially starting at (0, 0).
	i = 0; j = 0
	
	s=[]
	
	temp=node(i, j)
	
	s.append(temp)

	while s:

		# Pop the top node and move to the
		# left, right, top, down or retract 
		# back according the value of node's
		# dirn variable.
		temp = s.pop()
		d = temp.dirn
		i = temp.x; j = temp.y

		# Increment the direction and
		# push the node in the stack again.
		temp.dirn+=1
		s.append(temp)

		# If we reach the Food coordinates
		# return true
		if (i == fx and j == fy):
			return True


		# Checking the Up direction.
		if (d == 0):
			if (i - 1 >= 0 and maze[i - 1][j] and visited[i - 1][j]):
				temp1=node(i - 1, j)
				visited[i - 1][j] = False
				s.append(temp1)
			

		# Checking the left direction
		elif (d == 1):
			if(j - 1 >= 0 and maze[i][j - 1] and visited[i][j - 1]):
				temp1=node(i, j - 1)
				visited[i][j - 1] = False
				s.append(temp1)


		# Checking the down direction
		elif (d == 2):
			if(i + 1 < n and maze[i + 1][j] and visited[i + 1][j]):
				temp1=node(i + 1, j)
				visited[i + 1][j] = False
				s.append(temp1)
			
		
		# Checking the right direction
		elif (d == 3):
			if (j + 1 < m and maze[i][j + 1] and visited[i][j + 1]):
				temp1=node(i, j + 1)
				visited[i][j + 1] = False
				s.append(temp1)

		# If none of the direction can take 
		# the rat to the Food, retract back 
		# to the path where the rat came from.
		else:
			visited[temp.x][temp.y] = True
			s.pop()


	# If the stack is empty and
	# no path is found return false.
	return False

# Driver code
if __name__ == '__main__':

	# Initially setting the visited
	# array to true (unvisited)
	
	# Maze matrix
	maze = [
		[ 1, 0, 1, 1, 0 ],
		[ 1, 1, 1, 0, 1 ],
		[ 0, 1, 0, 1, 1 ],
		[ 1, 1, 1, 1, 1 ]
	]

	# Food coordinates
	fx = 2
	fy = 3

	if (isReachable(maze)):
		print("Path Found!")
	else:
		print("No Path Found!")
