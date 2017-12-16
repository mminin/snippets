from astropy.io import fits
import gdal
import numpy as np

dataset = gdal.Open('hrl00006f40_07_if181s_trr3.tiff', gdal.GA_ReadOnly)
z=[dataset.GetRasterBand(i).ReadAsArray() for i in range(1,dataset.RasterCount+1)]
data=np.asarray(z)

hdu = fits.PrimaryHDU(data)
hdulist = fits.HDUList([hdu])
hdu = fits.PrimaryHDU(data)
hdulist.writeto('test02.fits')
