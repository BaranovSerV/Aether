import numpy as np


class Grid1D():
    def __init__(self, dx: float, nx: int, origin: float = 0.0):
        self.dx = dx
        self.nx = nx
        self.origin = origin


    @property
    def faceCenters(self):
        return np.linspace(self.origin, self.origin + self.nx * self.dx, self.nx + 1)
    

    @property
    def cellCenters(self):
        return (self.faceCenters[:-1] + self.faceCenters[1:]) / 2
    

    @property
    def numberOfCells(self):
        return self.nx
    

    @property
    def numberOfFaces(self):
        return self.nx + 1


    @property
    def facesLeft(self):
        return np.array([True] + [False] * (self.numberOfFaces - 1))


    @property
    def facesRight(self):
        return np.array([False] * (self.numberOfFaces - 1) + [True])
    

    @property
    def faceToCellIDs(self):
        ids = np.zeros((2, self.numberOfFaces), dtype=int)
        ids[0] = np.arange(-1, self.numberOfCells)
        ids[1] = np.arange(0, self.numberOfCells + 1)
        ids[1][-1] = -1  
        return ids