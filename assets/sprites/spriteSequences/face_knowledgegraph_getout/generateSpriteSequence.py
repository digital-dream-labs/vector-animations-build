"""
This script can be used to generate the definition.json file.
Run this script from the same directory as the .png image sequence
and it will spit out the definition.json file in the same directory.

This is a modified copy of tools/animationScripts/generateSpriteSequence.py
from the 'victor' git repo.
"""

import os
import glob


preSeqString = """
{
  "loop" : "doNothing", 
  "sequence" :[
    {
      "segmentType" : "straightThrough",
      // file names relative to folder
      "fileList": [
"""


postSequenceString = """\n      ]
    }
  ]
}
"""


def writeJsonFile(fullJSONPath, outString):
    if os.path.exists(fullJSONPath):
        os.remove(fullJSONPath)
    f = open(fullJSONPath,"w")
    f.write(outString)
    f.close()


def main(outputFile="definition.json"):
    thisDir = os.getcwd()
    fullJSONPath = os.path.join(thisDir, outputFile)

    # Make a list of all the .png files and sort them alphabetically
    files = glob.glob(os.path.join(thisDir, "*.png"))
    files = map(os.path.basename, files)
    files.sort()

    fileList = ""
    for entry in files:
        fileList += '        "%s",' % entry + os.linesep

    outString = preSeqString + fileList + postSequenceString

    # remove final comma
    commaIdx = outString.rfind(",")
    outString = outString[:commaIdx] + outString[commaIdx + 1:]

    writeJsonFile(fullJSONPath, outString)


if __name__ == "__main__":
    main()


