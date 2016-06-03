#In this simulation we magnetize a set of 4 nanomagnetic triangles arranged in a clover shape in the direction of the positive z-axis then observe the time development of the system as the magnetization relaxes to a ground state.

import nmag
from nmag import SI

#The material (permalloy), saturation magnetization (Ms), exchange coupling, and damping are defined here
mat_Py = nmag.MagMaterial(name="Py",
                          Ms=SI(0.86e6,"A/m"),
                          exchange_coupling=SI(13.0e-12, "J/m"),
                          llg_damping=0.5)

#We create the simulation object
sim = nmag.Simulation("clover")

#Loading the mesh here. The first argument is the mesh file name, the second argument is a list of tuples
#which describe the domains/regions within the mesh. Here we have one-element containing the 2-tuple ("sphere", Py).
#"sphere" is a user-named string given to mesh region 1. The second part of the tuple is the MagMaterial object.
#The third argument of load_mesh is an SI object that defines the physical distance associated with the length 1.0.
#So the distance 1.0 in the mesh file should correspond to 1 nanometer in the real world in this simulation.
sim.load_mesh("clover.nmesh.h5",
              [("Py", mat_Py)],
              unit_length=SI(1e-9,"m"))


#We set the initial magnetization in terms of a field of normalized vectors.
#In this simulation, the initial magnetization is pointing in the direction of the positive z-axis.
sim.set_m([0,0,1])


#To compute the time development of the system we use a time step of dt. This line creates an SI object to represent out timescale.
dt = SI(5e-12, "s") 



#Here we let the system's magnetization relax over 500 time steps. In each iteration we first call advance_time(i*dt) which
#instructs nmag to carry on time integration up to the time i*dt. The save_data call saves the average data into the bar_dat.ndt file.
#The if statement is used to save all the spacially resolved data every ten time steps. So when i = 10, 20, 30, etc all the (spatial) averages of all fields (going into the bar_dat.ndt file), and the spatially resolved data for all fields (that are saved to bar_dat.h5). If the current iteration is not a multiple of ten then only the spatially averaged data is saved.
for i in range(0, 501):
    sim.advance_time(dt*i)                  #compute time development

    if i % 10 == 0:			    #every 10 loop iterations, 
        sim.save_data(fields='all')         #save averages and all
                                            #fields spatially resolved
    else:
        sim.save_data()                     #otherwise just save averages

