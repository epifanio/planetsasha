

#include "ossimNetCdfReaderFactory.h"
#include "ossimNetCdfReader.h"
#include <ossim/base/ossimKeywordlist.h>
#include <ossim/base/ossimRefPtr.h>
#include <ossim/base/ossimString.h>
#include <ossim/imaging/ossimImageHandler.h>
#include <ossim/base/ossimTrace.h>
#include <ossim/base/ossimKeywordNames.h>

static const ossimTrace traceDebug("ossimNetCdfReaderFactory:debug");

RTTI_DEF1(ossimNetCdfReaderFactory,
          "ossimNetCdfReaderFactory",
          ossimImageHandlerFactoryBase);

ossimNetCdfReaderFactory* ossimNetCdfReaderFactory::theInstance = 0;

ossimNetCdfReaderFactory::~ossimNetCdfReaderFactory()
{
   theInstance = 0;
}

ossimNetCdfReaderFactory* ossimNetCdfReaderFactory::instance()
{
   if(!theInstance)
   {
      theInstance = new ossimNetCdfReaderFactory;
   }
   return theInstance;
}
   
ossimImageHandler* ossimNetCdfReaderFactory::open(
   const ossimFilename& fileName, bool openOverview)const
{
   if(traceDebug())
   {
      ossimNotify(ossimNotifyLevel_DEBUG)
         << "ossimNetCdfReaderFactory::open(filename) DEBUG: entered..."
         << "\ntrying ossimNetCdfReader"
         << std::endl;
   }
   
   ossimRefPtr<ossimImageHandler> reader = new ossimNetCdfReader;
   reader->setOpenOverviewFlag(openOverview);
   if(reader->open(fileName) == false)
   {
      reader = 0;
   }
   
   if(traceDebug())
   {
      ossimNotify(ossimNotifyLevel_DEBUG)
         << "ossimNetCdfReaderFactory::open(filename) DEBUG: leaving..."
         << std::endl;
   }
   
   return reader.release();
}

ossimImageHandler* ossimNetCdfReaderFactory::open(const ossimKeywordlist& kwl,
                                               const char* prefix)const
{
   if(traceDebug())
   {
      ossimNotify(ossimNotifyLevel_DEBUG)
         << "ossimNetCdfReaderFactory::open(kwl, prefix) DEBUG: entered..."
         << "Trying ossimNetCdfReader"
         << std::endl;
   }

   ossimRefPtr<ossimImageHandler> reader = new ossimNetCdfReader;
   if(reader->loadState(kwl, prefix) == false)
   {
      reader = 0;
   }
   
   if(traceDebug())
   {
      ossimNotify(ossimNotifyLevel_DEBUG)
         << "ossimNetCdfReaderFactory::open(kwl, prefix) DEBUG: leaving..."
         << std::endl;
   }
   
   return reader.release();
}

ossimObject* ossimNetCdfReaderFactory::createObject(
   const ossimString& typeName)const
{
   ossimRefPtr<ossimObject> result = 0;
   if(typeName == "ossimNetCdfReader")
   {
      result = new ossimNetCdfReader;
   }
   return result.release();
}

ossimObject* ossimNetCdfReaderFactory::createObject(const ossimKeywordlist& kwl,
                                                 const char* prefix)const
{
   return this->open(kwl, prefix);
}
 
void ossimNetCdfReaderFactory::getTypeNameList(std::vector<ossimString>& typeList)const
{
   typeList.push_back(ossimString("ossimNetCdfReader"));
}

void ossimNetCdfReaderFactory::getSupportedExtensions(
   ossimImageHandlerFactoryBase::UniqueStringList& extensionList)const
{
}

ossimNetCdfReaderFactory::ossimNetCdfReaderFactory(){}

ossimNetCdfReaderFactory::ossimNetCdfReaderFactory(const ossimNetCdfReaderFactory&){}

void ossimNetCdfReaderFactory::operator=(const ossimNetCdfReaderFactory&){}
