import RayTracer
import Scene, Object, Camera


camera = Camera.Camera(fov = 110, rayBounces=1)

rt = RayTracer.RayTracer()


scene = Scene.Scene(camera=camera, directionToLight = [1, 1, 1], ambientLight = [.1, .1, .1])



scene.addObject(Object.Sphere(center=[0, 0, -1], radius=.1, diffuse=[0,0,1], specular=[1,1,1], phong=4,))




#Scene 2




rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
