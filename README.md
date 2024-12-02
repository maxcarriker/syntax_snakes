# syntax_snakes
A* maze final project <br/>
This maze game compares human and computer pathfinding performance <br/>
The code generates a maze, and then an A* algorithm is used for pathfinding. Once the user plays the game the results are compared and displayed.

# Install the Following Packages
Pyamaze <br/>
Pygame <br/>
Numpy <br/>
Heaqp <br/>

# Pyamaze Package 
For more information about the Pyamaze package: https://github.com/MAN1986/pyamaze <br/>

Creates a maze of a specified size
- Loop percent can be set to determine if there is more than one path (0% = 1 path)

Creates an Agent (player)
- Controlled using arrow or WASD keys

Creates path from start to goal using recursive backtracker

![pyamaze1](https://github.com/maxcarriker/syntax_snakes/blob/main/Pyamaze%20img1.png)

Places within the maze have the indexes as seen in the picture below <br/>
A maze_map creates a dictionary of the map
- {(1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (2, 1): . . .}
- 1 = Space
- 0 = Wall

![pyamaze2](https://github.com/maxcarriker/syntax_snakes/blob/main/Pyamaze%20img2.png)

# Maze Matrix Creation
To make use of a pathfinding algorithm we decided to create a binary matrix from the maze_map dictionary <br/>
- The numbers along the top and left correspond to a Python matrix
- The numbers inside the image ((#,#)) correspond to the Pyamaze location

![pyamaze3](https://github.com/maxcarriker/syntax_snakes/blob/main/Pyamaze%20img3.png)

A loop is used to run through the dictionary and expand the max into a binary matrix where and a matrix like the one below is created
- 1 = Wall
- 0 = Space

![pyamaze4](https://github.com/maxcarriker/syntax_snakes/blob/main/Pyamaze%20img4.png)

# A* Algorithm
The A* code was taken and adjusted from the following: https://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/ 

For more information on the A* algorithm
- https://www.geeksforgeeks.org/a-search-algorithm/
- https://www.analytics-link.com/post/2018/09/14/applying-the-a-path-finding-algorithm-in-python-part-1-2d-square-grid

The A* algorithm finds the best path but not necessarily the shortest path. It makes use of the following equation:

f(n) = g(n) + h(n)
- the n_th node
- f(n): total estimated cost
- g(n): cost from start point to n_th node
- h(n): cost from n_th node to end point

STEP
- Treat start point as parent node
- Calculate f(n) for neighbors
- Pick least one as new parent nodes
- Reach target node

Cost Calculation is found using a heuristic function which can be made of the following equations
- Manhattan Distance 
- Diagonal Distance 
- Euclidean distance

The path with the lowest cost is the next place the algoithm goes

# Pygame 
For documentation, syntax (classes, functions, etc.), installation instructions: https://www.pygame.org/wiki/GettingStarted

Our game makes use of sprites with allows for collision detection 
- Player
- Walls

It is able to take in use input to change between screens and move the player. As well as display the users path verses the algoithms path.

The following is the end screen to compare paths 
![pygame1](https://github.com/maxcarriker/syntax_snakes/blob/main/Pygame%20img1.png)

The following is the end screen which shows whether you lost or won based on the number of moves
![pygame2](https://github.com/maxcarriker/syntax_snakes/blob/main/Pygame%20img2.png)

  
