import random
import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves


def nextMove(board, color, time, movesRemaining):
	depth = 2
	each_move_score = []
	alpha = -9999
	beta = 9999
	bestMove = None
	temp_board = deepcopy(board)
	moves = getAllPossibleMoves(board, color)
	if len(moves) == 0:
		return "pass"
	elif len(moves) == 1:
		return moves[0]

	for move in moves:
		if time > 30 and time < 45:
			depth = 4
		elif time > 15 and time < 30:
			depth = 2
		elif time < 5:
			depth = 1
		else:
			depth = 6
		#print "our color: ", color
		#print "depth : ", depth
		score = alpha_beta_pruning(move, temp_board, alpha, beta, depth,color, time)
		each_move_score.append(score)
	print "score: ", each_move_score
	bestMove = moves[each_move_score.index(max(each_move_score))]
	print "bestMove = ", bestMove
	return bestMove


def evaluation(board, color):
    # Evaluation function 1
    # Count how many more pieces I have than the opponent
    
    opponentColor = gamePlay.getOpponentColor(color)
    
    value = 0
    # Loop through all board positions
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
                
        if board[x][y].upper() == color.upper():
            value = value + 1
            #print "value: in if (add)", value
        elif board[x][y].upper() == opponentColor.upper():
            value = value - 1
            #print "value: in else (subtract)", value
    #print "Value:  ", value
    return value


def alpha_beta_pruning(move, board, alpha, beta, depth, color, time):    

    temp_board = deepcopy(board)
    gamePlay.doMove(temp_board,move)
    moves = []
    #print "our color: inside alpha", color
    if depth <= 0:
        value = evaluation(temp_board,color)
        return value

    moves = getAllPossibleMoves(board, color) 
    #print "moves: ",moves
    if len(moves) == 0:
        value = evaluation(temp_board,color)
        return value

    a= -9999
    b= 9999

    if depth%2 == 1:
        for move in moves:
        	depth = depth-1
        	score= alpha_beta_pruning(move, temp_board, a, min(beta, b),depth, gamePlay.getOpponentColor(color),time)
        	b = min(b,score)
        	if time < 5:
        		return b
        	if alpha>= b:
        		return b
        return b
    else:
      	for move in moves:
      		depth = depth-1
      		score= alpha_beta_pruning(move,temp_board, max(alpha, a), b, depth,color,time)
      		a=max(a,score)
      		if time < 2:
      			return a
      		if a >= beta:
      			return a
      	return a