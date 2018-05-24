# *****************************************************************************
# NAME: editEnviHeader.py
# DEV: J. Heath Harwood
# DATE: 24  May 2018
#
#
# DESCRIPTION:  Script to will copy first 13 lines of the envi header file (*.hdr) associated with *.img files
#               in order to specify the correct information in a new header file (e.g.
#               Band names, wavelength/wavelenght units, system, default bands to display)
#               *.img.hdr.  This is a better naming convention for the header as most programs
#               need this association.
#
# DEPENDENCIES: OGR/GDAL, Python Standard Library, easygui, utm
#
# SOURCE(S):    -
#
#*****************************************************************************

'''
Change log:
2018-May-24 J. Heath Harwood, tool is operational

TODO:
 -

'''

###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.IMPORT STATEMENTs.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###


import os, glob, sys, re, fnmatch


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.CONSTANTS.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###

sensorType = '''sensor type = CASI 1500'''

wvLenthUnits = '''
wavelength_units = Nanometers'''

defaultBands = '''
default bands = {20, 13, 6}
'''
band_names = '''band names = {
 Mosaic (Band 1), Mosaic (Band 2), Mosaic (Band 3), Mosaic (Band 4), 
 Mosaic (Band 5), Mosaic (Band 6), Mosaic (Band 7), Mosaic (Band 8), 
 Mosaic (Band 9), Mosaic (Band 10), Mosaic (Band 11), Mosaic (Band 12), 
 Mosaic (Band 13), Mosaic (Band 14), Mosaic (Band 15), Mosaic (Band 16), 
 Mosaic (Band 17), Mosaic (Band 18), Mosaic (Band 19), Mosaic (Band 20), 
 Mosaic (Band 21), Mosaic (Band 22), Mosaic (Band 23), Mosaic (Band 24), 
 Mosaic (Band 25), Mosaic (Band 26), Mosaic (Band 27), Mosaic (Band 28), 
 Mosaic (Band 29), Mosaic (Band 30), Mosaic (Band 31), Mosaic (Band 32), 
 Mosaic (Band 33), Mosaic (Band 34), Mosaic (Band 35), Mosaic (Band 36), 
 Mosaic (Band 37), Mosaic (Band 38), Mosaic (Band 39), Mosaic (Band 40), 
 Mosaic (Band 41), Mosaic (Band 42), Mosaic (Band 43), Mosaic (Band 44), 
 Mosaic (Band 45), Mosaic (Band 46), Mosaic (Band 47), Mosaic (Band 48)}
'''
wavelength = '''wavelength = {
  371.100006,  385.399994,  399.700012,  413.899994,  428.200012,  442.399994,
  456.700012,  471.000000,  485.200012,  499.500000,  513.700012,  528.000000,
  542.299988,  556.500000,  570.799988,  585.000000,  599.299988,  613.500000,
  627.799988,  642.000000,  656.299988,  670.500000,  684.799988,  699.000000,
  713.299988,  727.500000,  741.799988,  756.000000,  770.299988,  784.500000,
  798.799988,  813.000000,  827.299988,  841.500000,  855.799988,  870.000000,
  884.299988,  898.500000,  912.700012,  927.000000,  941.299988,  955.500000,
  969.799988,  984.000000,  998.299988, 1012.000000, 1026.000000, 1041.000000}
'''

###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.FUNCTIONS.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###

###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.MAIN.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
# Get the common working directory
cwd = os.getcwd()
# Define the location of the header files
hdrPath = cwd
# get all the header files
hdrFiles = [os.path.join(dirPath, f)
            for dirPath, dirNames, files in os.walk(hdrPath)
            for f in files if f.endswith('.hdr')]

#print hdrFiles
# Loop through the header file list
for hFile in hdrFiles:
    # Grab a header file
    with open(hFile, 'r') as hData:
        #print hFile
        # Split the header file name in order to creat a new header file
        newHdr = hFile.split('.')[0] + '.img.hdr'
        #print newHdr
        # Read the first 13 lines
        # For example
        '''
        ENVI
description = {
  Mosaic Result [Fri Apr 20 12:29:22 2018]}
samples = 15609
lines   = 4203
bands   = 48
header offset = 0
file type = ENVI Standard
data type = 2
interleave = bip
sensor type = Unknown
byte order = 0
map info = {UTM, 1.000, 1.000, 499670.029, 4311719.953, 1.0000000000e+000, 1.0000000000e+000, 18, North, WGS-84, units=Meters}
coordinate system string = {PROJCS["UTM_Zone_18N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER\
["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]}
        '''
        hdrData = hData.readlines()[0:13]
        #print hdrData
        # Open the new header file in order to write the data formatted correctly
        with open(newHdr, 'w') as hdrText:
            hdrText.writelines(hdrData)
            print "Wrote header data to file"
            hdrText.writelines(sensorType)
            hdrText.writelines(wvLenthUnits)
            hdrText.writelines(defaultBands)
            hdrText.writelines(band_names)
            hdrText.writelines(wavelength)
            hdrText.close
    print "Going to next file"





