import numpy as np


class Grid2D:
    def __init__(self, dx: float, dy: float, nx: int, ny: int, origin: tuple = (0.0, 0.0)):
        self.dx = dx
        self.dy = dy
        self.nx = nx
        self.ny = ny
        self.origin = origin


    @property
    def faceCenters(self):
        x_faces = np.linspace(self.origin[0], self.origin[0] + self.nx * self.dx, self.nx + 1)
        y_faces = np.linspace(self.origin[1], self.origin[1] + self.ny * self.dy, self.ny + 1)
        return np.meshgrid(x_faces, y_faces, indexing='ij')


    @property
    def cellCenters(self):
        x_centers = np.linspace(self.origin[0] + self.dx / 2, self.origin[0] + self.nx * self.dx - self.dx / 2, self.nx)
        y_centers = np.linspace(self.origin[1] + self.dy / 2, self.origin[1] + self.ny * self.dy - self.dy / 2, self.ny)
        return np.meshgrid(x_centers, y_centers, indexing='ij')


    @property
    def numberOfCells(self):
        return self.nx * self.ny
    

    @property
    def numberOfFaces(self):
        return (self.nx + 1) * self.ny + (self.ny + 1) * self.nx
    