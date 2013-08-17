

#include <cstdlib>
#include <cstddef> /* for NULL */
#include <cmath>   /* for pow */

#include "ossimNetCdfReader.h"
#include <ossim/imaging/ossimImageDataFactory.h>
#include <ossim/base/ossimConstants.h>
#include <ossim/base/ossimIpt.h>
#include <ossim/base/ossimDpt.h>
#include <ossim/base/ossimEndian.h>
#include <ossim/base/ossimIrect.h>
#include <ossim/base/ossimFilename.h>
#include <ossim/base/ossimKeywordlist.h>
#include <ossim/base/ossimTrace.h>
#include <ossim/base/ossimNotifyContext.h>


RTTI_DEF1(ossimNetCdfReader, "ossimNetCdfReader", ossimImageHandler)

#ifdef OSSIM_ID_ENABLED
   static const char OSSIM_ID[] = "$Id: ossimNetCdfReader.cpp 141991 2013-08-13 19:33:27Z rashadkm $";
#endif
   
static ossimTrace traceDebug("ossimNetCdfReader:degug");  

ossimNetCdfReader::ossimNetCdfReader()
   :
      ossimImageHandler(),
      theProcessor(0)
{
}

ossimNetCdfReader::~ossimNetCdfReader()
{
   if (isOpen())
   {
      close();
   }
}

void ossimNetCdfReader::destroy()
{
   if(theProcessor)
   {
      delete theProcessor;
      theProcessor = 0;
   }
   theTile = 0;
   theMemoryTile = 0;
}

ossimRefPtr<ossimImageData> ossimNetCdfReader::getTile(
                                                         const  ossimIrect& tile_rect,
                                                         ossim_uint32 resLevel)
{
   if(!theTile.valid()||!theMemoryTile.valid())
   {
      cacheImage();
   }
   if (theTile.valid())
   {
      // Image rectangle must be set prior to calling getTile.
      theTile->setImageRectangle(tile_rect);
      
      if ( getTile( theTile.get(), resLevel ) == false )
      {
         if (theTile->getDataObjectStatus() != OSSIM_NULL)
         {
            theTile->makeBlank();
         }
      }
   }
   
   return theTile;
}

bool ossimNetCdfReader::getTile(ossimImageData* result,
                                  ossim_uint32 resLevel)
{
   bool status = false;
   status = getOverviewTile(resLevel, result);
   
   ossimIrect rect = result->getImageRectangle();
   if (!status) // Did not get an overview tile.
   {
      if(!theTile.valid()||!theMemoryTile.valid())
      {
         cacheImage();
      }
      if (theTile.valid())
      {
         // Image rectangle must be set prior to calling getTile.
         theTile->setImageRectangle(rect);
         
         theTile->makeBlank();
         
         ossimIrect memRect = theMemoryTile->getImageRectangle();
         
         if(memRect.intersects(rect))
         {
            ossimIrect clampRect = theMemoryTile->getImageRectangle().clipToRect(rect);
            
            theTile->loadTile(theMemoryTile->getBuf(),
                              memRect,
                              OSSIM_BSQ);
            
            theTile->validate();
            status = true;
         }
      }
   }
   return status;
}



ossimIrect
ossimNetCdfReader::getImageRectangle(ossim_uint32 reduced_res_level) const
{
   return ossimIrect(0,
                     0,
                     getNumberOfSamples(reduced_res_level) - 1,
                     getNumberOfLines(reduced_res_level)   - 1);
}

bool ossimNetCdfReader::saveState(ossimKeywordlist& kwl,
                               const char* prefix) const
{
   return ossimImageHandler::saveState(kwl, prefix);
}

bool ossimNetCdfReader::loadState(const ossimKeywordlist& kwl,
                               const char* prefix)
{
   if (ossimImageHandler::loadState(kwl, prefix))
   {
      return open();
   }

   return false;
}

bool ossimNetCdfReader::open()
{
   OpenThreads::ScopedLock<OpenThreads::Mutex> lock(theMutex);
   int ret = 0;
   static const char MODULE[] = "ossimNetCdfReader::open";

   if (traceDebug())
   {
      ossimNotify(ossimNotifyLevel_DEBUG)
         << "ossimNetCdfReader::open entered..."
         << "File:  " << theImageFile.c_str()
         << std::endl;
   }

   // Start with a clean slate.
   if (isOpen())
   {
      close();
   }
   
   // Check for empty filename.
   if (theImageFile.empty())
   {
      return false;
   }
//necdf reader instance:::   theProcessor = new netcdf();
   //read from netcdf c++ lib if( (ret = theProcessor->open_file(theImageFile.c_str()) != LIBRAW_SUCCESS))
   {
      destroy();
      return false;
   }
   
   ossimImageHandler::completeOpen();


   return true;
}

ossim_uint32 ossimNetCdfReader::getNumberOfLines(ossim_uint32 reduced_res_level) const
{
   cacheImage();
   if (reduced_res_level == 0)
   {
      if(theMemoryTile.valid())
      {
         return theMemoryTile->getHeight();
      }
   }
   else if ( theOverview.valid() )
   {
      return theOverview->getNumberOfLines(reduced_res_level);
   }

   return 0;
}

ossim_uint32 ossimNetCdfReader::getNumberOfSamples(ossim_uint32 reduced_res_level) const
{
   cacheImage();
   if (reduced_res_level == 0)
   {
      if(theMemoryTile.valid())
      {
         return theMemoryTile->getWidth();
      }
   }
   else if ( theOverview.valid() )
   {
      return theOverview->getNumberOfSamples(reduced_res_level);
   }

   return 0;
}

ossim_uint32 ossimNetCdfReader::getImageTileWidth() const
{
   return 0;
}

ossim_uint32 ossimNetCdfReader::getImageTileHeight() const
{
   return 0;
}

ossimString ossimNetCdfReader::getShortName()const
{
   return ossimString("ossim_netcdf_reader");
}
   
ossimString ossimNetCdfReader::getLongName()const
{
   return ossimString("ossim netcdf reader");
}

ossimString  ossimNetCdfReader::getClassName()const
{
   return ossimString("ossimNetCdfReader");
}

ossim_uint32 ossimNetCdfReader::getNumberOfInputBands() const
{
   ossim_uint32 result = 0;
   cacheImage();
   if(theMemoryTile.valid())
   {
      result = theMemoryTile->getNumberOfBands();
   }
   return result;
}

ossim_uint32 ossimNetCdfReader::getNumberOfOutputBands()const
{
   return getNumberOfInputBands();
}

ossimScalarType ossimNetCdfReader::getOutputScalarType() const
{
   cacheImage();
   if(theMemoryTile.valid())
   {
      return theMemoryTile->getScalarType();
   }
   return ossimImageHandler::getOutputScalarType();
}

bool ossimNetCdfReader::isOpen()const
{
   return ((theProcessor != 0)||
           (theMemoryTile.valid()));
}

double ossimNetCdfReader::getMaxPixelValue(ossim_uint32 band)const
{
   cacheImage();
   if(theMemoryTile.valid())
   {
      return theMemoryTile->getMaxPix(band);
   }
   return ossimImageHandler::getMaxPixelValue(band);
}

void ossimNetCdfReader::close()
{
   destroy();
   ossimImageHandler::close();
}

bool ossimNetCdfReader::cacheImage()const
{
   OpenThreads::ScopedLock<OpenThreads::Mutex> lock(theMutex);
   
   bool result = false;
   if(theMemoryTile.valid()) return true;
   if(!theProcessor) return result;
   int ret = 0;
  //read from netcdf c++ if( (ret = theProcessor->unpack() ) == LIBRAW_SUCCESS)
   {
      theProcessor->imgdata.params.output_bps = 16;
      theProcessor->imgdata.params.output_color = 1;
      theProcessor->imgdata.params.no_auto_bright = 1;
      
      
      ret = theProcessor->dcraw_process();
      if(LIBRAW_SUCCESS ==ret)
      {
         libraw_processed_image_t *image = theProcessor->dcraw_make_mem_image(&ret);
         if(image)
         {
            theMemoryTile = 0;
            theTile = 0;
            ossimScalarType scalarType = OSSIM_UINT16;
            if(image->bits == 8)
            {
               scalarType = OSSIM_UINT8;
            }
            theMemoryTile = new ossimImageData(0, scalarType, image->colors, image->width, image->height);
            theTile       = new ossimImageData(0, scalarType, image->colors, 8,8);
            theTile->initialize();
            theMemoryTile->initialize();
            theMemoryTile->loadTile(image->data, 
                                    theMemoryTile->getImageRectangle(), 
                                    OSSIM_BIP);
            result = true;
            free(image);
            image = 0;
         }
      }
   }
   delete theProcessor;
   theProcessor = 0;
   
   return result;
}

