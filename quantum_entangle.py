import qutip as qt
import numpy as np

phase = 2.34912
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 083 Entangled Density Matrix (core: 'no drinking and the whore goes on to a job to do real work versus talk on twitter to ni**ers who say they don't do what I do. And he thinks he's special bcs he's in the group with kids all fucking creepy toe to think let life get so bad.'):")
print(rho)
