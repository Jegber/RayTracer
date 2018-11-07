import RayTracer
import Scene, Object

rt = RayTracer.RayTracer()


scene = Scene.Scene()

#White Ball
#Sphere Center .35 0 -.1 Radius .05 Material Diffuse 1 1 1 SpecularHighlight 1 1 1 PhongConstant 4
scene.addObject(Object.Sphere(center = [.35, 0, -1.1], radius=.05, diffuse=[1,1,1], specular=[1,1,1], phong=4))

#Red Ball
scene.addObject(Object.Sphere(center = [.2, .1, -1.1], radius=.075, diffuse=[1,0,0], specular=[.5,1,.5], phong=32))

#Green Ball
scene.addObject(Object.Sphere(center = [-.6, 0, -1.1], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32))

#Shadow Caster Test Triangle
#scene.addObject(Object.Triangle(vertex1=[-.1, .1, -.5], vertex2=[-.1, -.1, -.5], vertex3=[.1, 0, -1.5], diffuse=[1,1,0], specular=[1,1,1], phong=4))


#Shadow Test Ball
#scene.addObject(Object.Sphere(center = [-.5, 0, -1.1], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32))
#-Z axis Test Ball
#scene.addObject(Object.Sphere(center = [0, 0, -2], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32))

# Blue Triangle
#Triangle .3 -.3 -.4  0 .3 -.1  -.3 -.3 .2 Material Diffuse 0 0 1 SpecularHighlight 1 1 1 PhongConstant 32
scene.addObject(Object.Triangle(vertex1=[.3, -.3, -1.4], vertex2=[0, .3, -1.1], vertex3=[-.3, -.3, -.8], diffuse=[0,0,1], specular=[1,1,1], phong=32))

# Yellow Triangle
#Triangle  -.2 .1 .1   -.2 -.5 .2   -.2 .1 -.3 Material Diffuse 1 1 0 SpecularHighlight 1 1 1 PhongConstant 4
scene.addObject(Object.Triangle(vertex1=[-.2, .1, -.9], vertex2=[-.2, -.5, -.8], vertex3=[-.2, .1, -1.3], diffuse=[1,1,0], specular=[1,1,1], phong=4))




#Scene 2




rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
