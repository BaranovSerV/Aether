import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


class DiffusionTerm:
    def __init__(self, coeff=1.0):
        self.coeff = coeff


    def _build_matrix(self, mesh):
        nx = mesh.nx
        dx = mesh.dx
        coeff = self.coeff

        aW = coeff / dx  # Левый коэффициент
        aE = coeff / dx  # Правый коэффициент
        aP = aW + aE    # Главный коэффициент

        diagonals = [
            [-aW] * (nx - 1),  # Нижняя диагональ
            [aP] * nx,         # Главная диагональ
            [-aE] * (nx - 1)   # Верхняя диагональ
        ]
        offsets = [-1, 0, 1]

        A = diags(diagonals, offsets, shape=(nx, nx), format="csr")

        return A

    def solve(self, mesh, initial_condition, boundary_conditions, dt=None, time_steps=1):
        A = self._build_matrix(mesh)

        b = np.zeros(mesh.nx)
        b[0] += self.coeff / mesh.dx * boundary_conditions['left']
        b[-1] += self.coeff / mesh.dx * boundary_conditions['right']

        T = initial_condition.copy()

        if dt is None:
            return spsolve(A, b)

        for step in range(time_steps):
            T = spsolve(A, T + dt * b)

        return T