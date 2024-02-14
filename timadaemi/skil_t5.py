import re
import numpy as np
class Skil(object):
    """Timadaemi 2 f. REI Bjarni Þór Guðmundsson(btg7@hi.is)"""
    def add_2(self, a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a + b
        
        if isinstance(a, np.ndarray) and isinstance(b, float):
            nidurstada = a.astype(float).copy()
            stok = np.diag_indices_from(a)
            nidurstada[stok] += b
            return nidurstada
        
        if isinstance(a, float) and isinstance(b, np.ndarray):
            nidurstada = b.astype(float).copy()
            stok = np.diag_indices_from(b)
            nidurstada[stok] += a
            return nidurstada
            
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray) and a.shape == b.shape:
            return a + b
            
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray) and a.shape != b.shape:
            return np.sum(a) + np.sum(b)
        
if __name__ == '__main__':
    skil = Skil()