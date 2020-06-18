import time
import tkinter as tk
from tkinter import messagebox
from ex12.ai import AI
from ex12.game import Game

PERSON_VS_COMPUTER = 'person vs computer'
PERSON_VS_PERSON = 'person vs person'
COMP_VS_COMP = 'computer vs computer'


class Gui:
    def __init__(self):
        """
        the constactor of the game gui,and creating the first user's menu.
        """
        self._game_modes_options = {1: PERSON_VS_COMPUTER
        , 2: PERSON_VS_PERSON, 3: COMP_VS_COMP}
        self._player_colors = {1: 'red', 2: 'blue'}
        self._column = 0
        self._root = tk.Tk()
        self._disks = []
        self._game_logic = Game()
        self._choice = tk.StringVar()
        self._choice.set('choose game type, Default game is p vs p')
        self._menu = tk.OptionMenu(self._root, self._choice
            , PERSON_VS_COMPUTER, PERSON_VS_PERSON, COMP_VS_COMP)
        self._choose_button = tk.Button(self._root, text='press OK', command=self.init_single_game)
        self._choose_button.pack()
        self._menu.pack()
        self._ai_first = None
        self._ai_second = None

    def init_single_game(self):
        """
        the initiator of the first game, creating the game by the user's choices.
        creating the board and the instructions menu and the game itself.
        """
        top = tk.Frame(self._root, bg='burlywood4')
        instruction = tk.Label(top,
                                     text="Move instructions:\n move right- right arrow\nmove left - left arrow\nshoot ball: Space",
                                     font=('Helvetica', 13))
        instruction.pack(side=tk.RIGHT)
        arba_beshora = tk.Label(top,
         text="Four in a row", font=('Helvetica', 10))
        arba_beshora.pack(side=tk.TOP)
        top.pack(side=tk.TOP, fill=tk.BOTH)
        self._canvas = tk.Canvas(top, bg='saddle brown', height=700, width=700)
        self._root.bind('<Left>', lambda event: self.move_pointer(-1, True))
        self._root.bind('<Right>', lambda event: self.move_pointer(1, True))
        self._root.bind('<space>', lambda event: self.one_turn(True))
        self._pointer = self._canvas.\
            create_oval(0, 0, 100, 100, fill='red', outline='red')
        self._canvas.pack()
        self.check_if_over()
        self._choose_button.pack_forget()
        self._menu.pack_forget()
        self.create_board()
        # creating the computers according the the user's choice
        if (self._choice.get() == COMP_VS_COMP):
            self._ai_first = AI(self._game_logic, 1)
            self._ai_second = AI(self._game_logic, 2)
            self.comp_turn(self._ai_first)
        elif (self._choice.get() == PERSON_VS_COMPUTER):
            self._ai_first = AI(self._game_logic, 2)

    def comp_turn(self, ai_player_x):
        """
        this function is creating the move of the computer,
        according to the ai, and creates it in a way that it is visible
        for the user if the game is comp vs comp.
        :param ai_player_x: an ai type.
        :return: None
        """
        # so the game wont sleep before its started.
        if not self._game_logic.is_board_empty():
            time.sleep(0.7)
        # finding the computer's move.
        comp_move = ai_player_x.find_legal_move()
        # if the function returns None, the board is full or 1 player won the game.
        if comp_move is None:
            self.check_if_over()
            return
        # moving the pointer to the place that the comp is playing the turn,
        # so we can see the comp turn visible.
        while self._column != comp_move:
            if self._column < comp_move:
                self.move_pointer(1)
            else:
                self.move_pointer(-1)
        self.one_turn()

    def reset(self):
        """
        the function that is resetting the game if the user chooses to
        play another game. filling the board with empty slots and the
        pointer to player 1 turn.
        and also creating a new game and updating the computers in that game.
        """
        for row in self._disks:
            for element in row:
                self._canvas.itemconfig(element, fill='white')
        self._game_logic = Game()
        self._canvas.itemconfig(self._pointer,
                        fill=self._player_colors
                        [self._game_logic.get_current_player()])
        if self._choice.get() == COMP_VS_COMP:
            self._ai_first.set_game(self._game_logic)
            self._ai_second.set_game(self._game_logic)
            self.comp_turn(self._ai_first)
        if self._choice.get() == PERSON_VS_COMPUTER:
            self._ai_first.set_game(self._game_logic)

    def one_turn(self, clicked=False):
        """
        this function is running one turn in
         the game, both user's turn and computer's
        turn if there are computers playing.
        :param clicked: a bool expression, which shows if the function
        launched from a click by the user, or by the computer.
        True if by user, False if by the computer.
        :return: None, but updates the board.
        """
        # so we wont be able to change the game of the computers.
        if (clicked and self._choice.get() == COMP_VS_COMP) or (
                clicked and self._ai_first and self._game_logic.get_current_player() == 2):
            return
        if self._game_logic.is_possible_move(self._column):
            position = self._game_logic.make_move(self._column)
            self._canvas.itemconfigure(self._disks[position[0]][position[1]],
                                       fill=self._canvas.itemcget(self._pointer, 'fill'))
            self._canvas.itemconfig(self._pointer,
                            fill=self._player_colors[self._game_logic.get_current_player()])
            self._root.update()
        if (self._ai_first and self._ai_second) or \
                (self._ai_first and self._game_logic.get_current_player() == 2):
            self.comp_turn(self._ai_first)
        self.check_if_over()

    def check_if_over(self):
        """
        a function that checks if the game is over, if the board is full
        or if there is a winner.
        also this function asks the user if
         he would like to play another game,
        or if he wishes to exit. and the function
        does what the user asked.
        """
        winner = self._game_logic.get_winner()
        if winner is not None:
            if winner == 0:
                result = messagebox.askokcancel\
                    ("Hello ", "Its a tie" +
                     " Would you like to Play again?")
            else:
                result = messagebox.askokcancel("Hello ", "Player " + str(
                    winner) + ' ' + "Won! "
                + "Would you like to Play again?")
            if result:
                self.reset()
            else:
                exit()

    def move_pointer(self, direction, clicked=False):
        """
        this function moves the "pointer ball" which is the ball on top
        of the board.
        :param direction: -1 if moves to the left, 1 if moves to the right.
        :param clicked: if the function got called by a user click, or
        if the function called by the computer's turn.
        True if by the user's click, False if by the computer.
        :return: None
        """
        if clicked and self._choice.get() == COMP_VS_COMP:
            return
        if self._ai_first and clicked:
            if self._game_logic.get_current_player() == 2:
                return
        if self._column == 0 and direction == -1 or \
                self._column == 6 and direction == 1:
            return
        else:
            self._column += direction
            self._canvas.move(self._pointer, direction * 100, 0)
            self._root.update()
            time.sleep(0.2)

    def create_board(self):
        """
        this function creates a game board for the four in a row game,
        alse if creates a list of all the empty places in the board,
        and updates the disks list.
        """
        temporary_lst = []
        for i in range(6):
            for j in range(7):
                temporary_lst.append(
                    self._canvas.create_oval(0 + 100 * j,
        200 + 100 * i, 100 + 100 * j, 100 + 100 * i, fill='white',
                                             outline='black'))
            self._disks.append(temporary_lst)
            temporary_lst = []

    def run(self):
        """
        the function that starts the game, by the mainloop.
        :return:
        """
        self._root.mainloop()


if __name__ == '__main__':
    gui = Gui()
    gui.run()
