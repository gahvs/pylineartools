from copy import deepcopy

class MatrixComponent:

    def __init__(self, row, col, number) -> None:
        try:
            if not all(isinstance(arg, int) for arg in (row, col)) or any(isinstance(arg, bool) for arg in (row, col)):
                raise TypeError("The row and col attributes must be of type int()")
            else:
                self.row = row
                self.col = col
        except TypeError as err:
            print(err)
            exit()
        try:
            if not isinstance(number, (int, float)) or isinstance(number, bool):
                raise TypeError("The number attribute must be of type int() or float()")
            else:
                self.number = number
        except TypeError as err:
            print(err)
            exit()

class Matrix:

    def __init__(self) -> None:
        self.__rows = list()
        self.__cols = list()
        self.__matrix = dict()
    
    def __updateRowColList(self, row, col):
        """
            Add the row and column to their respective lists if they do not already contain them.
        """
        if not row in self.__rows: self.__rows.append(row)
        if not col in self.__cols: self.__cols.append(col)

    def __fill(self) -> None:
        """
            When a new column is added this method is called. 
            Its function is to fill the other columns with the 
            new component added (and with the number = 0)
        """
        for row in self.__rows:
            for col in self.__cols:
                if not col in self.__matrix[row]:
                    self.__matrix[row][col] = None

    def add(self, component) -> None:
        """
            Adds a component to the array. The parameter must be an instance of MatrixComponent().
            If the component already exists the method will do nothing.
            To modify a value in the array use the change() method.
        """
        try:
            if not isinstance(component, MatrixComponent):
                raise TypeError
            else:
                if component.row in self.__matrix:
                    if component.col in self.__matrix[component.row]:
                        if self.__matrix[component.row][component.col] is not None:
                            return # throw error? (component already exists)
                else:
                    self.__matrix[component.row] = dict()
                
                self.__updateRowColList(row=component.row, col=component.col)
                self.__matrix[component.row][component.col] = component.number
                self.__fill()

        except TypeError:
            pass
    
    def change(self, row, col, number) -> None:
        """
            Change the value of matrix[row][col] if row and col 
            are part of the set of row indices and column indices, respectively.
        """
        if row in self.__matrix:
            if col in self.__matrix[row]:
                self.__matrix[row][col] = number

    def matrix(self) -> dict:
        """
            Returns the matrix in a dict {row: {col: number}}
        """
        return deepcopy(self.__matrix)

    def indexes(self) -> list:
        """
            Returns array indices in dicts {row: row, col: col} for all component.
        """
        indexes = list()
        for rowKey in self.__matrix:
            for colKey in self.__matrix[rowKey]:
                indexes.append({'row':rowKey,'col':colKey})
        return indexes

    def numbers(self, rowPart, colPart):
        """
            Returns a list of values ​​only from the array defined on rowPart and colPart.
            When you want the part to be the whole, rowPart or colPart must be ","
        """
        if rowPart == ",": rowPart = self.__rows[:]
        if colPart == ",": colPart = self.__cols[:]
        return [[ self.__matrix[row][col] for col in colPart] for row in rowPart]

    def getRow(self, row) -> list:
        """
            Returns the corresponding row of the matrix.
        """
        return [self.__matrix[row][k] for k in self.__matrix[row]]

    def getCol(self, col) -> list:
        """
            Returns the corresponding column of the matrix.
        """
        return [self.__matrix[k][col] for k in self.__matrix]

    def component(self, row, col):
        """
            Returns the matrix[row][col] number if row and col 
            are part of the set of row indices and column indices, respectively.
        """
        if row in self.__matrix:
            if col in self.__matrix[row]:
                return self.__matrix[row][col]
        return None

    def dimensions(self) -> dict:
        """
            Returns the dimensions of the matrix, that is, the number of rows and the number of columns. 
        """
        return {'rows':len(self.__rows),'cols':len(self.__cols)}

    def isNull(self) -> bool:
        """
            Indicates whether the array is null. 
            A matrix M defined over NxM is null if M[n][m] is 0 for all n, m belonging to N and M, respectively.
        """
        for row in self.__rows:
            for col in self.__cols:
                if self.__matrix[row][col] != 0 and self.__matrix[row][col] != None: return False
        return True

    def restriction(self, rowPart, colPart):
        """
            Returns an array defined over all p and q in rowPart and colPart, respectively.
            When you want the part to be the whole, rowPart or colPart must be ","
        """
        if rowPart == ",": rowPart = self.__rows[:]
        if colPart == ",": colPart = self.__cols[:]
        restriction = Matrix()
        for row in rowPart:
            for col in colPart:
                restriction.add(MatrixComponent(row, col, self.__matrix[row][col]))
        return restriction
    
    def multiplyByEscalar(self, escalar):
        """
            Multiplies each component of the matrix by a scalar.
        """
        for row in self.__rows:
            for col in self.__cols:
                self.__matrix[row][col] *= escalar
    
    def divideByEscalar(self, escalar):
        """
            Divides each component of the matrix by a scalar.
        """
        for row in self.__rows:
            for col in self.__cols:
                self.__matrix[row][col] /= escalar

    @staticmethod
    def copy(matrix):
        """
            Returns a matrix's copy.
        """
        copy = Matrix()
        for i in matrix.indexes():
            copy.add(MatrixComponent(i['row'], i['col'], matrix.component(i['row'], i['col'])))
        return copy

    @staticmethod
    def product(mat_x, mat_y):
        """
            Calculates the product of a matrix defined over L x M by a matrix defined over M x N.
            The product is a matrix defined over L x N.
        """ 
        product = Matrix()
        rows = set(map(lambda i: i['row'], mat_x.indexes()))
        cols = set(map(lambda i: i['col'], mat_y.indexes()))
        for i in rows:
            for j in cols:
                mult = [a * b for a, b in zip(mat_x.getRow(i), mat_y.getCol(j))]
                product.add(MatrixComponent(i, j, sum(mult)))
        
        return product