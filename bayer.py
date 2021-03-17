'''
modul, kje bi bral sliko duhov za uporabo v igro
'''

from matplotlib import pyplot as plt
import numpy as np

def bayer_v_rgb(slika_bayer, vzorec, interpoliraj=False):
    w, h = slika_bayer.shape

    g1 = vzorec.index('G')
    g2 = 3 - g1
    r = vzorec.index('R')
    b = vzorec.index('B')

    if not interpoliraj:
        resArray = np.zeros((w//2, h//2, 3), dtype=np.uint8)

        resArray[:, :, 0] = slika_bayer[r//2::2, r%2::2]
        resArray[:, :, 1] = slika_bayer[g1//2::2, g1%2::2]/2 + slika_bayer[g2//2::2, g2%2::2]/2
        resArray[:, :, 2] = slika_bayer[b//2::2, b%2::2]
    else:
        resArray = np.zeros((w, h, 3), dtype=np.uint8)

        if vzorec == 'BGGR':
            resArray[::2, ::2, 2] = slika_bayer[::2, ::2]

            resArray[::2, 1:h-3:2, 2] = slika_bayer[::2, :h-4:2]/2 + slika_bayer[::2, 2:h-2:2]/2
            resArray[::2, h-1, 2] = slika_bayer[::2, h-2]

            resArray[1:w-3:2, ::2, 2] = slika_bayer[:w-4:2, ::2]/2 + slika_bayer[2:w-2:2, ::2]/2
            resArray[w-1, ::2, 2] = slika_bayer[w-2, ::2]

            resArray[1:w-3:2, 1:h-3:2, 2] = slika_bayer[:w-4:2, :h-4:2]/4 + slika_bayer[:w-4:2, 2:h-2:2]/4 + slika_bayer[2:w-2:2, :h-4:2]/4 + slika_bayer[2:w-2:2, 2:h-2:2]/4
            resArray[1:w-3:2, h-1, 2] = slika_bayer[:w-4:2, h-2]/2 + slika_bayer[2:w-2:2, h-2]/2
            resArray[w-1, 1:h-3:2, 2] = slika_bayer[w-2, :h-4:2]/2 + slika_bayer[w-2, 2:h-2:2]/2
            resArray[w-1, h-1, 2] = slika_bayer[w-2, h-2]


            resArray[0, 0, 1] = slika_bayer[0, 1]/2 + slika_bayer[1, 0]/2
            resArray[2:w-2:2, 0, 1] = slika_bayer[1:w-3:2, 0]/3 + slika_bayer[3:w-1:2, 0]/3 + slika_bayer[2:w-2:2, 1]/3
            resArray[0, 2:h-2:2, 1] = slika_bayer[0, 1:h-3:2]/3 + slika_bayer[0, 3:h-1:2]/3 + slika_bayer[1, 2:h-2:2]/3
            resArray[2:w-2:2, 2:h-2:2, 1] = slika_bayer[1:w-3:2, 2:h-2:2]/4 + slika_bayer[3:w-1:2, 2:h-2:2]/4 + slika_bayer[2:w-2:2, 1:h-3:2]/4 + slika_bayer[2:w-2:2, 3:h-1:2]

            resArray[::2, 1::2, 1] = slika_bayer[::2, 1::2]
            resArray[1::2, ::2, 1] = slika_bayer[1::2, ::2]

            resArray[1:w-3:2, 1:h-3:2, 1] = slika_bayer[:w-4:2, 1:h-3:2]/4 + slika_bayer[2:w-2:2, 1:h-3:2]/4 + slika_bayer[1:w-3:2, :h-4:2]/4 + slika_bayer[1:w-3:2, 2:h-2:2]/4
            resArray[1:w-3:2, h-1, 1] = slika_bayer[:w-4:2, h-1]/3 + slika_bayer[2:w-2:2, h-1]/3 + slika_bayer[1:w-3:2, h-2]/3
            resArray[w-1, 1:h-3:2, 1] = slika_bayer[w-2, 1:h-3:2]/3 + slika_bayer[w-1, :h-4:2]/3 + slika_bayer[w-1, 2:h-2:2]/3 
            resArray[w-1, h-1, 1] = slika_bayer[w-1, h-2]/2 + slika_bayer[w-2, h-1]/2

            resArray[0, 0, 0] = slika_bayer[1, 1]
            resArray[2:w-2:2, 2:h-2:2, 0] = slika_bayer[1:w-3:2, 1:h-3:2]/4 + slika_bayer[1:w-3:2, 3:h-1:2]/4 + slika_bayer[3:w-1:2, 1:h-3:2]/4 + slika_bayer[3:w-1:2, 3:h-1:2]/4
            resArray[0, 2:h-2:2, 0] = slika_bayer[1, 1:h-3:2]/2 + slika_bayer[1, 3:h-1:2]/2
            resArray[2:w-2:2, 0, 0] = slika_bayer[1:w-3:2, 1]/2 + slika_bayer[3:w-1:2, 1]/2

            resArray[0, 1::2, 0] = slika_bayer[1, 1::2]
            resArray[2:w-2:2, 1::2, 0] = slika_bayer[1:w-3:2, 1::2]/2 + slika_bayer[3:w-1:2, 1::2]/2

            resArray[1::2, 0, 0] = slika_bayer[1::2, 1]
            resArray[1::2, 2:h-2:2, 0] = slika_bayer[1::2, 1:h-3:2]/2 + slika_bayer[1::2, 3:h-1:2]/2

            resArray[1::2, 1::2, 0] = slika_bayer[1::2, 1::2]
        elif vzorec == 'RGGB':
            resArray[::2, ::2, 0] = slika_bayer[::2, ::2]

            resArray[::2, 1:h-3:2, 0] = slika_bayer[::2, :h-4:2]/2 + slika_bayer[::2, 2:h-2:2]/2
            resArray[::2, h-1, 0] = slika_bayer[::2, h-2]

            resArray[1:w-3:2, ::2, 0] = slika_bayer[:w-4:2, ::2]/2 + slika_bayer[2:w-2:2, ::2]/2
            resArray[w-1, ::2, 0] = slika_bayer[w-2, ::2]

            resArray[1:w-3:2, 1:h-3:2, 0] = slika_bayer[:w-4:2, :h-4:2]/4 + slika_bayer[:w-4:2, 2:h-2:2]/4 + slika_bayer[2:w-2:2, :h-4:2]/4 + slika_bayer[2:w-2:2, 2:h-2:2]/4
            resArray[1:w-3:2, h-1, 0] = slika_bayer[:w-4:2, h-2]/2 + slika_bayer[2:w-2:2, h-2]/2
            resArray[w-1, 1:h-3:2, 0] = slika_bayer[w-2, :h-4:2]/2 + slika_bayer[w-2, 2:h-2:2]/2
            resArray[w-1, h-1, 0] = slika_bayer[w-2, h-2]


            resArray[0, 0, 1] = slika_bayer[0, 1]/2 + slika_bayer[1, 0]/2
            resArray[2:w-2:2, 0, 1] = slika_bayer[1:w-3:2, 0]/3 + slika_bayer[3:w-1:2, 0]/3 + slika_bayer[2:w-2:2, 1]/3
            resArray[0, 2:h-2:2, 1] = slika_bayer[0, 1:h-3:2]/3 + slika_bayer[0, 3:h-1:2]/3 + slika_bayer[1, 2:h-2:2]/3
            resArray[2:w-2:2, 2:h-2:2, 1] = slika_bayer[1:w-3:2, 2:h-2:2]/4 + slika_bayer[3:w-1:2, 2:h-2:2]/4 + slika_bayer[2:w-2:2, 1:h-3:2]/4 + slika_bayer[2:w-2:2, 3:h-1:2]

            resArray[::2, 1::2, 1] = slika_bayer[::2, 1::2]
            resArray[1::2, ::2, 1] = slika_bayer[1::2, ::2]

            resArray[1:w-3:2, 1:h-3:2, 1] = slika_bayer[:w-4:2, 1:h-3:2]/4 + slika_bayer[2:w-2:2, 1:h-3:2]/4 + slika_bayer[1:w-3:2, :h-4:2]/4 + slika_bayer[1:w-3:2, 2:h-2:2]/4
            resArray[1:w-3:2, h-1, 1] = slika_bayer[:w-4:2, h-1]/3 + slika_bayer[2:w-2:2, h-1]/3 + slika_bayer[1:w-3:2, h-2]/3
            resArray[w-1, 1:h-3:2, 1] = slika_bayer[w-2, 1:h-3:2]/3 + slika_bayer[w-1, :h-4:2]/3 + slika_bayer[w-1, 2:h-2:2]/3 
            resArray[w-1, h-1, 1] = slika_bayer[w-1, h-2]/2 + slika_bayer[w-2, h-1]/2

            resArray[0, 0, 2] = slika_bayer[1, 1]
            resArray[2:w-2:2, 2:h-2:2, 2] = slika_bayer[1:w-3:2, 1:h-3:2]/4 + slika_bayer[1:w-3:2, 3:h-1:2]/4 + slika_bayer[3:w-1:2, 1:h-3:2]/4 + slika_bayer[3:w-1:2, 3:h-1:2]/4
            resArray[0, 2:h-2:2, 2] = slika_bayer[1, 1:h-3:2]/2 + slika_bayer[1, 3:h-1:2]/2
            resArray[2:w-2:2, 0, 2] = slika_bayer[1:w-3:2, 1]/2 + slika_bayer[3:w-1:2, 1]/2

            resArray[0, 1::2, 2] = slika_bayer[1, 1::2]
            resArray[2:w-2:2, 1::2, 2] = slika_bayer[1:w-3:2, 1::2]/2 + slika_bayer[3:w-1:2, 1::2]/2

            resArray[1::2, 0, 2] = slika_bayer[1::2, 1]
            resArray[1::2, 2:h-2:2, 2] = slika_bayer[1::2, 1:h-3:2]/2 + slika_bayer[1::2, 3:h-1:2]/2

            resArray[1::2, 1::2, 2] = slika_bayer[1::2, 1::2]

    plt.imsave('originali/rgb.jpg', resArray)
