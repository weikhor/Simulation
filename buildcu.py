from ase import Atoms
from ase.visualize import view
from ase.io.trajectory import Trajectory
from ase import units
from ase.parallel import world
from ase.io import read,write
from ase.lattice.cubic import FaceCenteredCubic


atoms = FaceCenteredCubic(directions=[[1,0,0], [0,1,0], [0,0,1]],
                         size=(90,90,2), symbol='Cu', pbc=(1,1,0))

view(atoms, viewer='VMD')
#view(atoms)

atoms.center()
tag = 'cu_fcc' ## output Trajectory file
write(tag+'.xyz',atoms) 

