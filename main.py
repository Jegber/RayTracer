import RayTracer as rt
import Scene, Object

charles = rt.RayTracer()


charles.renderToFile(Scene.Scene(), 'generatedImages/raytracerTest.ppm')
