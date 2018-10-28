
def RGBArrayToPPMFile(rgb, filepath):

    f = open(filepath, 'w')

    f.write("P3\n") # ASCII RGB Header
    f.write(str(len(rgb[0])) + " "); f.write(str(len(rgb)) + "\n") # w h of image
    f.write("15\n") # Max pixel value

    for row in range(len(rgb)):
        for col in range(len(rgb[0])):

            f.write(str(rgb[row][col][0]) + " ")
            f.write(str(rgb[row][col][1]) + " ")
            f.write(str(rgb[row][col][2]) + "   ")

        f.write("\n")


def testRGBArrayToPPMFile():
    
    rgb = [ [(255,255,255), (255,255,255), (255,255,255), (255,255,255), (255,255,255)],
            [(100, 0, 0), (100, 0, 0), (100, 0, 0), (100, 0, 0), (100, 0, 0)],
            [(0, 100, 0), (0, 100, 0), (0, 100, 0), (0, 100, 0), (0, 100, 0)],
            [(0, 0, 100), (0, 0, 100), (0, 0, 100), (0, 0, 100), (0, 0, 100)],
            [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]  ]

    RGBArrayToPPMFile(rgb, 'generatedImages/ppmTest.ppm')
