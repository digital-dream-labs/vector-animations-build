
import argparse
import os
import re
import shutil


PATH_TO_SPRITE_SEQ = ""

preSeqString = '''
{
  "loop" : "doNothing", 
  "sequence" :[
    {
      "segmentType" : "straightThrough",
      // file names relative to folder
      "fileList": [
'''

postSequenceString = '''\n      ]
    }
  ]
}
'''


if __name__ == "__main__":
    fullPath = "./"
    

    files = os.listdir(fullPath)
    files = [f for f in files if (re.search(".png", f) != None)]



    fileList = ""

    for entry in files:
        fileList += "        \"" + (entry + "\",\n")


    outString = preSeqString + fileList + postSequenceString

    # remove final comma
    commaIdx = outString.rfind(",")
    outString = outString[:commaIdx] + outString[commaIdx + 1:]

    fullJSONPath = fullPath + "definition.json"
    if os.path.exists(fullJSONPath):
        os.remove(fullJSONPath)

    f = open(fullJSONPath,"w")
    f.write(outString)
    f.close()


