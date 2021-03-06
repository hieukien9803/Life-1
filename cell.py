import toolbox
class Cell(object):

    displaySets = {'basic': {'liveChar': 'X', 'deadChar': '.'},
                    'binary': {'liveChar': '1', 'deadChar': '0'},
                    'circles': {'liveChar': '\u26AA', 'deadChar': '\u26AB'},
                    'baseball': {'liveChar': '\u26BE', 'deadChar': '\u26F3'},
                    'atsign': {'liveChar': '@', 'deadChar': ' '},
                    'check': {'liveChar': '\u2705', 'deadChar': '\u274C'}

    }

    displaySet = 'basic'
    currentDisplaySet = 'basic'
    liveChar = displaySets[displaySet]['liveChar']
    deadChar = displaySets[displaySet]['deadChar']

    @classmethod
    def set_display(cls, displaySet):
        """
        Change the character that is displayed for cells.
        :param liveChar: The character to display for live cells
        :param deadChar: The character to display for dead cells
        :return:

        example:
        Cell.change_display(Cell, '@', ' ')
        """
        legalValues = cls.displaySets.keys()
        if displaySet in legalValues:
            cls.displaySet = displaySet
            cls.liveChar = cls.displaySets[displaySet]['liveChar']
            cls.deadChar = cls.displaySets[displaySet]['deadChar']
        #cls.liveChar = liveChar
        #cls.deadChar = deadChar
        else:
            raise ValueError(f'DisplaySet must be in {legalValues}.')

    @classmethod
    def set_display_user_values(cls, alive, dead):
        """
        Add an item to the displaySets for user defined characters.
        :param alive: character string that represents alive cells.
        :param dead: character string that represents dead cells.
        :return: None
        """
        numberOfCharacterSets = len(Cell.displaySets)
        key = f'user defined {numberOfCharacterSets}'
        Cell.displaySets[key] = {'liveChar': alive, 'deadChar': dead}

    def __init__(self, row, column):
        """
        Given a row and a column, creates a cell that knows its row,
           column, living (all cells start off with living as False), and
           neighbors (all cells start off with an empty list for neighbors).
        :param row: amount of rows
        :param column: amount of columns
        """
        self.__row = row
        self.__column = column
        self.living = False
        self.__neighbors = []


    def __str__(self):
        """
        Returns either the liveChar or the deadChar for the Cell class
        depending on the state of the cell.
        :return: the state of the cell
        """
        if self.living:
            return Cell.liveChar
        else:
            return Cell.deadChar

    def get_living(self):
        """Returns whether the cell is alive."""
        return self.living

    def set_living(self, state):
        """
        Sets whether the cell is alive or dead.
        :param state: if the cell is alive or dead
        :return:
        """
        if isinstance(state, bool):
            self.living = state
        else:
            raise TypeError('state must be boolean.')

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def add_neighbor(self, cell):
        """
        adds the neighbor cell to the list of neighhbors
        :param cell: the cell that is a neighbor to a given cell
        :return:
        """
        #
        # Print statement below is for debugging. Comment
        # out you know all the neighbors are working.
        #
        #print(f'{self.__repr__()} add neighbor {cell.__repr__()}')
        self.__neighbors.append(cell)

    def living_neighbors(self):
        """
        counts of the number of living cells a given cell has.
        :return: the number of living cells
        """
        neighborCount = 0
        for neighbor in self.__neighbors:
            if neighbor.get_living() == True:
                neighborCount += 1
        return neighborCount

    def __repr__(self):
        #
        # Here's a handy way to use if..else that we haven't talked about.
        #
        state = 'alive' if self.living else 'dead'
        return f'Cell({self.__row},{self.__column}) [{state}]'

    def debug(self):
        """
        Sometimes you just need to know about a cell.
        :return:
        """
        neighbors = len(self.__neighbors)
        string = self.__repr__() + f' neighbors: {self.living_neighbors()}/{neighbors}'
        for neighbor in self.__neighbors:
            string += '\n     ' + neighbor.__repr__()
        print(string)
