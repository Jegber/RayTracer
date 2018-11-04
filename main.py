import RayTracer
import Scene, Object

rt = RayTracer.RayTracer()


scene = Scene.Scene()
scene.addObject(Object.Sphere(specular=[1, 1, 1], diffuse=[1, 0, 0], center = [.2, 0, -1.1], radius=.075, phong=4))
scene.addObject(Object.Sphere(specular=[.0, .5, .5], diffuse=[.5, .5, .75], center = [1, 1, -9], radius=1, phong=5))
scene.addObject(Object.Sphere(center = [0, 0, -10], radius=2, phong=32))

rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
