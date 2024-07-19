import argparse
from rgbc import RGBC
from rgbmaker.imgplt import save_fig
parser = argparse.ArgumentParser('rgbmaker',description="""
RGBC - RGBMaker is a python package which communicates to different astronomical services and fetches fits and numerical data.
https://github.com/avialxee/rgbmake
""", formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--position', type=str, help="""(Required)
        The object name or the coordinates of the object in the FK5 (J2000) system. 
        Ex: "14 09 48.86 -03 02 32.6", M87, NGC1243, without quotes.""")
parser.add_argument('-r', '--radius', type=str, help="""(Required) (default = 0.12) (float)
        The size of the image in degrees, this size will be used for the 
        field of view in the resultant image.
        For reference, in the night sky, the moon is about 0.52 degrees across.""")
parser.add_argument('-s', '--surveys', type=str, help="""comma separated survey names to create the desired RGB image
                    Ex. rgbc -s 'DSS2 IR,DSS2 Red, DSS2 Blue' ...
                    """)

parser.add_argument('-cmin', '--contour-min', type=str, help="""give the lower level value for plotting the contour
                    """)

def cli():
    args=parser.parse_args()

    position    =   args.position
    radius      =   args.radius
    surveys     =   args.surveys.split(',')
    surveys     =   [svy.strip() for svy in surveys]
    cmin        =   float(args.contour_min)

    RGBC(position=position, radius=radius, svy=surveys, cmin=cmin, kind='png').plot()