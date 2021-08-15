import numpy as np

import decide_player
import who_won

class Matrix(object):
      def __init__(self):
            self.matrix = np.zeros(shape=(3,3))
      # def print_arr(self):
      #       print(self.matrix)
      def input_getter(self, dcd_ply):
            """
            This function gets the input positions on the matrix
            and prints whether the position has been already taken.
            """
            
            player_no = dcd_ply.return_player()
            if  player_no == 1:
                  print("Turn: Player 1 \n Enter position:", end = "")
                  self.inp_row, self.inp_col = list(map(int, input().split()))
                  output = []
                  output.append(self.inp_row)
                  output.append(self.inp_col)
                  # return output
                  self.taken_or_not(output, player_no)
               
            else:
                  print("Turn: Player 2 \n Enter position:", end = "")
                  self.inp_row, self.inp_col = list(map(int, input().split()))
                  output = []
                  output.append(self.inp_row)
                  output.append(self.inp_col)
                  self.taken_or_not(output, player_no)

      def taken_or_not(self, matrix_pos, player_no):            
            try:
                  inp_row, inp_col = matrix_pos[0], matrix_pos[1]
            except IndexError:
                  print("The position entered is invalid!")
            
            if self.matrix[inp_row][inp_col] == 0:
                  self.matrix[inp_row][inp_col] = player_no

            else:
                  print("Position already taken")
            
if __name__ == "__main__":
      my_matrix = Matrix()
      whowon = who_won.who_won(my_matrix.matrix)
      move = 9
      dcd_ply = decide_player.decide_player()
      boolean = False
      while(move > 0):
            print(my_matrix.matrix)

            if whowon.check()[0]:
                  print("Player", whowon.check()[1], "has won the game",)
                  boolean = True
                  break
            my_matrix.input_getter(dcd_ply)
            move -= 1
      if boolean == False:
            print("Draw!")         