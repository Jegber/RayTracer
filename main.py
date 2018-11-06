import RayTracer
import Scene, Object

rt = RayTracer.RayTracer()


scene = Scene.Scene()

#White Ball
scene.addObject(Object.Sphere(center = [.35, .2, -.9], radius=.05, diffuse=[1,1,1], specular=[1,1,1], phong=4))
#Red Ball
scene.addObject(Object.Sphere(center = [.2, 0, -1.1], radius=.075, diffuse=[1,0,0], specular=[.5,1,.5], phong=32))
#Green Ball
#scene.addObject(Object.Sphere(center = [-.6, 0, -1], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32))
#Shadow Test Ball
scene.addObject(Object.Sphere(center = [-.5, 0, -1.1], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32))
#-Z axis Test Ball
#scene.addObject(Object.Sphere(center = [0, 0, -2], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32))
# Middle Triangle
scene.addObject(Object.Triangle())




rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
