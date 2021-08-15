class decide_player(object):
      def __init__(self):
            self.play_lst = []
      
      def return_player(self):
            if self.play_lst:
                  if (len(self.play_lst)-1) % 2 == 0:
                        self.play_lst.append(6)
                        return 6

                  else:
                        self.play_lst.append(1)
                        return 1

            else:
                  self.play_lst.append(0)
                  return 1