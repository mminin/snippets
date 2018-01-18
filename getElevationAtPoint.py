# obtain elevation from DTM knowing a point location.
from osgeo import gdal, ogr
class elevationMeasurer():
    def __init__(self, src_filename):
        self.src_filename=src_filename
        self.src_ds=gdal.Open(src_filename)
        self.gt=self.src_ds.GetGeoTransform()
        self.rb=self.src_ds.GetRasterBand(1)
    def getEleAtPoint(self, mx, my):
        return self.rb.ReadAsArray(int((mx-self.gt[0])/self.gt[1]),int((my-self.gt[3])/self.gt[5]),1,1)[0][0]

## Use example:
#q=elevationMeasurer('../../0_MIKHAIL/mosaic_DTM-lanzarote.tif')
#q.getEleAtPoint(629488,3211998)
