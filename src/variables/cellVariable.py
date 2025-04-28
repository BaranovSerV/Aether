import numpy as np


class CellVariable:
    def __init__(self, mesh, name: str = "", value=0.0):
        self.mesh = mesh
        self.name = name

        self.value = np.full(self.mesh.numberOfCells, value)


    def constrain(self, value, where):
        boundary_face_ids = np.where(where)[0]

        boundary_cell_ids = []
        for face_id in boundary_face_ids:
            cell_ids = self.mesh.faceToCellIDs[:, face_id]
            
            for cell_id in cell_ids:
                if cell_id != -1:  
                    boundary_cell_ids.append(cell_id)

            boundary_cell_ids = np.unique(boundary_cell_ids)

        self.value[boundary_cell_ids] = value