'''
# Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white king. 
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can't be on space '9z'. 
The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
This function should detect when a bug has resulted in an improper chess board.
'''
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 

def isValidChessBoard(board):
    pieceCounts = {'w': {'total': 0, 'pawn': 0, 'knight': 0, 'bishop': 0, 'rook': 0, 'queen': 0, 'king': 0},
                   'b': {'total': 0, 'pawn': 0, 'knight': 0, 'bishop': 0, 'rook': 0, 'queen': 0, 'king': 0}}

    for space, piece in board.items():
        # Validate Board Spaces - Chess Board is 1a-8h
        if  int(space[0]) < 1 or \
            int(space[0]) > 8 or \
            space[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False

        # Validate Piece Names
        if piece[0] not in ['w', 'b'] or \
           piece[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            return False

        # Update Piece Counts
        if piece[0] == 'w':
            pieceCounts['w'][piece[1:]] += 1
            pieceCounts['w']['total'] += 1
        else: 
            pieceCounts['b'][piece[1:]] += 1
            pieceCounts['b']['total'] += 1

    # Validate Piece Counts
    # Total Pieces (per side): 16 | Max Pawns: 8 | Max Knights, Bishops, or Rooks: 2 | Max Queens, or Kings: 1
    for player, pieceCounts in pieceCounts.items():
        totalPlayerPieces = 0
        for piece, count in pieceCounts.items():
            totalPlayerPieces += 1
            if  (piece == 'total' and count > 16)   or \
                (piece == 'pawn' and count > 8)     or \
                (piece == 'knight' and count > 2)   or \
                (piece == 'bishop' and count > 2)   or \
                (piece == 'rook' and count > 2)     or \
                (piece == 'queen' and count > 1)    or \
                (piece == 'king' and count > 1):
                    return False
    
    return True

print(isValidChessBoard(board))