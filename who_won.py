import numpy as np
class who_won(object):
      def __init__(self, arr):
            self.matrix = arr
      
      def check(self):
            if any(np.sum(self.matrix, 1)==3) or any(np.sum(self.matrix, 0)==3) or sum(np.diag(self.matrix)==3) or sum(np.diag(self.matrix[::-1])==3):
                  return [True, 1]

            if any(np.sum(self.matrix, 1)==18) or any(np.sum(self.matrix, 0)==18) or sum(np.diag(self.matrix)==18) or sum(np.diag(self.matrix[::-1])==18):
                  return [True, 2]
            
            else:
                  return [False, 0]