import Scene, Object, Ray

#def __init__(self, diffuse = (1, 0, 0), specular = (1, 1, 1), phong = 4, center=(1, 1, -10), radius=1):
sphere = Object.Sphere(center = [-.5, 0, -1.1], radius=.3, diffuse=[0,1,0], specular=[.5,1,.5], phong=32)

#def Ray(self, origin, direction, bouncesLeft = 0, shouldNormalize=True):
#ray = Ray.Ray(origin=[0, 0, 0, 0], direction=[0, 0, -1, 0], shouldNormalize = True)

#shadowRay origin:  [-0.4946397718310972, 0.2473199359155486, -0.9302822977682621, 0]    dest:  [ 0.50536023  0.24731991 -0.9302822   0.        ]
ray = Ray.Ray(origin=[-0.4946397718310972, 0.2473199359155486, -0.9302822977682621, 0], direction=[ 0.50536023,  0.24731991, -0.9302822,   0.        ], shouldNormalize = True)



print("rayOrigin: ", ray.origin, "    rayDirection: ",  ray.direction)
intersection = sphere.rayIntersection(ray)

print(intersection)
