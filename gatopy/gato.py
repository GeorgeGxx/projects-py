import operator, sys, random, time

def todosIguales(list):
    """Retorna si todos los elementos de la lista son iguales o si esta vacia"""
    return not list or list == [list[0]] * len(list)

Vacio = '-'
Jugador_X = 'x'
Jugador_O = 'o'

class Board:
    """Esta clase representa el tablero del gato."""
    def __init__(self):
        """Inicializa los miembros consecutivos."""
        self.pieces = [Vacio]*9
        self.field_names = '123456789'

    def output(self):
        """Muestra el tablero."""
        for line in [self.pieces[0:3], self.pieces[3:6], self.pieces[6:9]]:
            print (' '.join(line))

    def winner(self):
        """Funcion de deteccion de estado final. Returns Jugador_X, Jugador_O or None"""
        winning_rows = [[0,1,2],[3,4,5],[6,7,8], # vertical
                        [0,3,6],[1,4,7],[2,5,8], # horizontal
                        [0,4,8],[2,4,6]]         # diagonal
        for row in winning_rows:
            if self.pieces[row[0]] != Vacio and todosIguales([self.pieces[i] for i in row]):
                return self.pieces[row[0]]

    def getValidMoves(self):
        """Lista de movimientos validos. Son validos los vacios."""
        return [pos for pos in range(9) if self.pieces[pos] == Vacio]

    def gameOver(self):
        """Retorna cierto si ganador o no mas movimientos."""
        return self.winner() or not self.getValidMoves()

    def getMoveName(self, move):
        """Movimiento legible"""
        return self.field_names[move]
    
    def makeMove(self, move, jugador):
        """Mueve"""
        self.pieces[move] = jugador
    
    def undoMove(self, move):
        """Deshace un movimiento de tablero"""
        self.makeMove(move, Vacio)

def jugadorHumano(board, jugador):
    """Funcion para el jugador humano"""
    board.output()
    possible_moves = dict([(board.getMoveName(move), move) for move in board.getValidMoves()])
    move = input("Introduce movimiento (%s): " % (', '.join(sorted(possible_moves))))
    while move not in possible_moves:
        print ("'%s' no es valido. Prueba de nuevo." % move)
        move = input("Introduce movimiento (%s): " % (', '.join(sorted(possible_moves))))
    board.makeMove(possible_moves[move], jugador)

def jugadorMaquina(board, jugador):
    """Funcion para la maquina"""
    t0 = time.time()
    board.output()
    opponent = { Jugador_O : Jugador_X, Jugador_X : Jugador_O }

    """Nodo terminal, evalua valor: 1 gana, 0 nada, -1 pierde"""	
    def judge(winner):
        if winner == jugador:
            return +1
        if winner == None:
            return 0
        return -1

    def evaluateMove(move, p=jugador):
        try:
            board.makeMove(move, p)
            if board.gameOver():
                return judge(board.winner())
            outcomes = (evaluateMove(next_move, opponent[p]) for next_move in board.getValidMoves())

            if p == jugador:
                #return min(outcomes)
                min_element = 1
                for o in outcomes:
                    if o == -1:
                        return o
                    min_element = min(o,min_element)
                return min_element
            else:
                #return max(outcomes)
                max_element = -1
                for o in outcomes:
                    if o == +1:
                        return o
                    max_element = max(o,max_element)
                return max_element

        finally:
            board.undoMove(move)

    moves = [(move, evaluateMove(move)) for move in board.getValidMoves()]
    random.shuffle(moves)
    
    moves.sort(key=lambda winner: winner[1])
    
    
    print ("mueve la maquina: %0.3f ms" % ((time.time()-t0)*1000))

    """ realiza movimiento -1 o en 0 por ese orden """	
    board.makeMove(moves[-1][0], jugador)

def game():
    """Gatito"""
    b = Board()
    turn = 1
    while True:
 
        print ("Turno %i." % turn)
        jugadorHumano(b, Jugador_X)
        if b.gameOver(): 
            break

        jugadorMaquina(b, Jugador_O)
        if b.gameOver(): 
            break
        turn += 1

    b.output()
    if b.winner():
        print ('Jugador "%s" Maquina gana. Humano ser inferior de la naturaleza perdiste' % b.winner())
    else:
        print ('*--Empate Juego Terminado--*')


if __name__ == "__main__":
    game()
