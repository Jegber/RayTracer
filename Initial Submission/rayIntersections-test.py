import Scene, Object, Ray

#def __init__(self, diffuse = (0, 0, 1), specular = (1, 1, 1), phong = 32, vertex1=(.3, -.3, -1.4), vertex2=(0, .3, -1.1), vertex3=(-.3, -.3, -.8) ):
triangle = Object.Triangle(vertex1=[-1, 1, -3], vertex2=[-1, -1, -3], vertex3=[1, 0, -1])

#def Ray(self, origin, direction, bouncesLeft = 0, shouldNormalize=True):
#ray = Ray.Ray(origin=[0, 0, 0, 0], direction=[0, 0, -1, 0], shouldNormalize = True)

#shadowRay origin:  [-0.4946397718310972, 0.2473199359155486, -0.9302822977682621, 0]    dest:  [ 0.50536023  0.24731991 -0.9302822   0.        ]
ray = Ray.Ray(origin=[0, 0, 0, 0], direction=[ 0,  0, -1,   0.        ], shouldNormalize = True)



print("rayOrigin: ", ray.origin, "    rayDirection: ",  ray.direction)
intersection = triangle.rayIntersection(ray)

print(intersection)
