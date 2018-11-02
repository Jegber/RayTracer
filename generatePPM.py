def RGBPythonArrayToPPMFile(rgb, filepath):

    f = open(filepath, 'w')

    f.write("P3\n") # ASCII RGB Header
    f.write(str(len(rgb[0])) + " "); f.write(str(len(rgb)) + "\n") # w h of image
    f.write("255\n") # Max pixel value

    for row in range(len(rgb)):
        for col in range(len(rgb[0])):

            f.write(str(rgb[row][col][0]) + " ")
            f.write(str(rgb[row][col][1]) + " ")
            f.write(str(rgb[row][col][2]) + "   ")

        f.write("\n")


def RGBNumpyArrayToPPMFile(rgb, filepath):

    f = open(filepath, 'w')

    f.write("P3\n") # ASCII RGB Header
    f.write(str(len(rgb[0])) + " "); f.write(str(len(rgb)) + "\n") # w h of image
    f.write("255\n") # Max pixel value

    for row in range(len(rgb)):
        for col in range(len(rgb[0])):

            f.write(str(rgb[row][col][0]) + " ")
            f.write(str(rgb[row][col][1]) + " ")
            f.write(str(rgb[row][col][2]) + "   ")

        f.write("\n")


def testRGBNumpyArrayToPPMFile():

    rgb = np.array([ [[255,255,255], [255,255,255], [255,255,255], [255,255,255], [255,255,255]],
                     [[100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0]],
                     [[0, 100, 0], [0, 100, 0], [0, 100, 0], [0, 100, 0], [0, 100, 0]],
                     [[0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 0, 100]],
                     [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]  ])

    RGBPythonNumpyArrayToPPMFile(rgb, 'generatedImages/ppmTest.ppm')



def testRGBPythonArrayToPPMFile():

    rgb = [ [(255,255,255), (255,255,255), (255,255,255), (255,255,255), (255,255,255)],
            [(100, 0, 0), (100, 0, 0), (100, 0, 0), (100, 0, 0), (100, 0, 0)],
            [(0, 100, 0), (0, 100, 0), (0, 100, 0), (0, 100, 0), (0, 100, 0)],
            [(0, 0, 100), (0, 0, 100), (0, 0, 100), (0, 0, 100), (0, 0, 100)],
            [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]  ]

    RGBPythonArrayToPPMFile(rgb, 'generatedImages/ppmNumpyTest.ppm')
