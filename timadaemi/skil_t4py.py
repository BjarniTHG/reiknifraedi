import re
import numpy as np
class Skil(object):
    """Timadaemi 2 f. REI Bjarni Þór Guðmundsson(btg7@hi.is)"""
    def mat1(self, m, n, types):
        if types == 'zeros':
            return np.zeros((m, n))
        elif types == 'ones':
            return np.ones((m, n))
        elif types == 'eye':
            return np.eye(m, n)
        elif types == 'diag':
            min_dim = min(m, n)
            return np.diag(range(min_dim))
        else:
            return None
        

    def mat2(self, m1, m2, j1, j2):
        m1_j1 = m1[:, j1]
        m2_j2 = m2[:, j2]
        
        z1 = m1_j1 + m2_j2
        z2 = m1_j1 - m2_j2
        z3 = m1_j1 * m2_j2
        z4 = m1_j1 @ m2_j2
        
        return z1,z2,z3,z4
        
        
if __name__ == '__main__':
    skil = Skil()

