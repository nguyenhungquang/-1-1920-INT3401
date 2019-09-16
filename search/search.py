# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())[1][2]
    """

    a=set()
    from util import Stack
    vertexList=Stack()
    t=(problem.getStartState(),[])
    vertexList.push(t)

    "while (not bool(sum([problem.isGoalState(x[0]) for x in problem.getSuccessors(t[0])]))) and (not vertexList.isEmpty()):"
    while  not vertexList.isEmpty():
        t= vertexList.pop()
        if problem.isGoalState(t[0]):
            return t[1]
        if t[0] not in a:
            a.add(t[0])
            for x in problem.getSuccessors(t[0]):
                vertexList.push((x[0],t[1]+[x[1]]))
        "[vertexList.push((x[0],t[1]+[x[1]])) for x in problem.getSuccessors(t[0]) if x[0] not in a]"
    "lastMove=[x[1] for x in problem.getSuccessors(t[0]) if problem.isGoalState(x[0])]"
    "return  t[1]"
    "print t[1]+sum([x[1] for x in problem.getSuccessors(t[0])])"
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    from Queue import PriorityQueue
    result=[]
    vertexList=util.Queue()
    currentPos=(problem.getStartState(),[])
    vertexList.push((problem.getStartState(),[]))
    visited=[]
    while not vertexList.isEmpty():
        currentPos= vertexList.pop()
        if problem.isGoalState(currentPos[0]):
            return currentPos[1]
        if currentPos[0] not in visited:
            visited.append(currentPos[0])
            for x in problem.getSuccessors(currentPos[0]):
                temp =(x[0],currentPos[1]+[x[1]])
                vertexList.push(temp)
    "[vertexList.put((x[2]+currentPos[0],x[0],currentPos[2]+[x[1]])) for x in problem.getSuccessors(currentPos[1])]"
    """return currentPos[2]"""
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "util.raiseNotDefined()"

def uniformCostSearch(problem):
    from Queue import PriorityQueue
    result=[]
    vertexList=util.PriorityQueue()
    currentPos=(problem.getStartState(),[],0)
    vertexList.push(currentPos,0)
    visited=[]
    while not vertexList.isEmpty():
        currentPos= vertexList.pop()
        if problem.isGoalState(currentPos[0]):
            return currentPos[1]
        if currentPos[0] not in visited:
            visited.append(currentPos[0])
            for x in problem.getSuccessors(currentPos[0]):
                temp =(x[0],currentPos[1]+[x[1]],currentPos[2]+x[2])
                vertexList.push(temp,currentPos[2]+x[2])
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "util.raiseNotDefined()"

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    from Queue import PriorityQueue
    result=[]
    vertexList=util.PriorityQueue()
    currentPos=(problem.getStartState(),[],0)
    vertexList.push(currentPos,0)
    visited=[]
    while not vertexList.isEmpty():
        currentPos= vertexList.pop()
        if problem.isGoalState(currentPos[0]):
            return currentPos[1]
        if currentPos[0] not in visited:
            visited.append(currentPos[0])
            for x in problem.getSuccessors(currentPos[0]):
                temp =(x[0],currentPos[1]+[x[1]],currentPos[2]+x[2])
                vertexList.push(temp,currentPos[2]+x[2]+heuristic(x[0],problem))
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
