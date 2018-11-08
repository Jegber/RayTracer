import RayTracer
import Scene, Object, Camera


camera = Camera.Camera(fov = 110, rayBounces=1)

rt = RayTracer.RayTracer()


scene = Scene.Scene(camera=camera, directionToLight = [0, 1, 0], ambientLight = [0, 0, 0])


# Yellow Triangle
c = 1.2
#Triangle  -.2 .1 .1   -.2 -.5 .2   -.2 .1 -.3 Material Diffuse 1 1 0 SpecularHighlight 1 1 1 PhongConstant 4
scene.addObject(Object.Sphere(center=[0, .3, 0-c], radius=.2, diffuse=[0,0,1], specular=[1,1,1], phong=4, reflective=[.75, .75, .75]))
#scene.addObject(Object.Sphere(center=[0, 0, -1.4], radius=.2, diffuse=[0,0,1], specular=[1,1,1], phong=4, reflective=[.75, .75, .75]))

#scene.addObject(Object.Sphere(center=[0, 0, -2], radius=1, diffuse=[0,0,1], specular=[1,1,1], phong=4, reflective=[.75, .75, .75]))
#scene.addObject(Object.Triangle(vertex1=[0, -1, .5-c], vertex2=[1, -1, 0-c], vertex3=[0, -1, -.5-c], diffuse=[0,0,1], specular=[1,1,1], phong=4))
#scene.addObject(Object.Triangle(vertex1=[0, -1, .5-c], vertex2=[0, -1, -.5-c], vertex3=[-1, -1, 0-c], diffuse=[1,1,0], specular=[1,1,1], phong=4))
scene.addObject(Object.Triangle(vertex1=[0, -.5, .5-c], vertex2=[1, .5, 0-c], vertex3=[0, -.5, -.5-c], diffuse=[0,0,1], specular=[1,1,1], phong=4))
scene.addObject(Object.Triangle(vertex1=[0, -.5, .5-c], vertex2=[0, -.5, -.5-c], vertex3=[-1, .5, 0-c], diffuse=[1,1,0], specular=[1,1,1], phong=4))




#Scene 2




rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
