# Clover-Time-Development
This code is to be used with the NMAG micromagnetic simulation package developed at the University of Southampton with substantial contributions from Hans Fangohr, Thomas Fischbacher, Matteo Franchin. More information can be found at http://nmag.soton.ac.uk/nmag/

This simulation computes the time-development and magnetic ground state of a system of 4 triangular nanomagnets arranged in a clover configuration. The system is initialized with a magnetization vector of [0,0,1] which points in the direction of the positive z-axis. The magnetization then relaxes for 500 time steps which leads to the final magnetization.

The arrangment of triangles was first created using AutoDesk Inventor. The CAD file was then exported and used with NETGEN to generate the mesh necessary for use with NMAG simulations.
