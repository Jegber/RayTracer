import RayTracer
import Scene, Object

rt = RayTracer.RayTracer()


scene = Scene.Scene()
print(scene)
scene.addObject(Object.Sphere())

rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
