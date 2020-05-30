/*

A network system is defined as a two-dimensional grid. Each cell of the grid has a routing coefficient associated with it. You need to send a packet from the top-left corner to the bottom right corner.
A packet can travel in four directions only - up, down, left and right and only if the cell does not go beyond bounds. A packet needs an energy of |C[x, y] - C[x', y']| to travel from the cell (x,y) to the cell (x', y'), where |x| denotes the absolute value of x.

The effort required by a packet in any path is defined as the maximum energy needed by the packet along that path. Your task is to find the minimum effort required by the packet to traverse the network from top-left corner to the bottom-right corner.

Consider, for example, the packet travels in the given grid with number of rows, N = 3 and number of columns, M = 4. as described below -
12 6 5 3 
6 13 3 15 
8 2 6 9 

Suppose the packet travels from  12 -> 6 -> 5 -> 3 -> 6 -> 9. the maximum effort required in the path is 6.

*/
