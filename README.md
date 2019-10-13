# One Voice One Vision
 Fusion of Voice and Vision

In this program we use Speech Recognition using google API, to do speech to text and extract instruction for the AutoDesk Fusion360 API. Furthermore, we made a script to actually do things with these intructrions like: draw a circle, a line, an axis, an sphere, a rectangle; extrude and revolve profiles, loft between objects and even Rectangular or Circular Patterns. 

All are implemented in a straightforward way. Below you will find how to access these instructions:

- NewSketch (plane): make new sketch in that plane (top, front, right). To use it with speech just say: "sketch top" and the rest is handled for you
- Draw Axis (x,y,z,x1,y1,z1): draws axis from one point to the other, to either draw a line o have an axis of rotation. To use it just say: "axis from (value.x,value.y,value.z) to (value.x1, value.y1, value.z1)" 
- Draw Circle (radius,x,y,z): draws circle centered in (x,y,z) and parallel to the plane of the current sketch. To use it just say: "circle with (value.radius) in (value.x, value.y, value.z)"
- Draw Rectangle (plane,x,y,z, x1,y1): draws rectangle in the plane defined with the point given (definition changes for each plane!). To use it just say: "rectangle top in (value.x,value.y,value.z) and (value.x1, value.y1)"
- Draw Sphere (x,y,z,radius): draws sphere centered in (x,y,z) with given radius. To use it just say: "sphere in (value.x,value.y,value.z) with radius (radius)" 
- Extrude profile (distance): extrudes las profile made a given distance. To use it just say: "extrude value.distance symmetric". The symmetric is optional, if not stated non symmetric extrude is assumed.
- Revolve (axis, angle): revolves las profile around a given axis (output from axis command) a certain angle. To use it just say: "Revolve value.angle"
- Loft : Makes a loft between the last two profiles. To use it just say: "loft" 
- Rectangular_Pattern(prof, Nx,distance_x,Ny,distance_y): draws a rectangular patter of [Nx,Ny] copies of the profile with distances [dx,dy]. To use it just say: "Rectangular pattern Nx dx Ny Dy"
- Circular_Pattern (N,Axis): draws circular pattern around an axis of the last object. To use it just say: "Rectangular Pattern N" 

The python script is the one responsible for the speech recognition
