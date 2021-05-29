# vector-animations
Raw animation assets and tools to modify existing animations or build new eye animations, weather animations, and more for the Vector Robot! All assets from firmware release 1.0.0 to 1.7.0 are in the [Releases](https://github.com/digital-dream-labs/vector-animations-build/releases) section (just download the zip file and unpack into the /assets directory to use.)

## Requirements:
* OSKR Unlocked Vector Robot 
* Secure Shell on Vector (see [Getting A Secure Shell on Vector](https://oskr.ddl.io/oom/doc/unlock_checklist.html#getting-secure-shell))

HomeBrew (MAC OSX ONLY):
* (MAC OSX Only) [Homebrew for Mac OSX](https://brew.sh/) 

Flatbuffers:
* Mac OSX: ```brew install flatbuffers```
* Linux: ```sudo apt install flatbuffers-compiler```
* Windows: Download [flatc_windows.zip](https://github.com/google/flatbuffers/releases). Unzip the .zip archive and place the "flatc.exe" file in the vector-animations folder.

SSH:
* Mac OSX: SSH is preinstalled- no action needed.
* Linux: SSH is preinstalled- no action needed.
* Windows: Open the Start Menu. Type "manage optional" to search for "manage optional features", click "Add a feature". Install "OpenSSH Client" and "OpenSSH Server" by clicking the checkboxes next to them, then clicking "Install".

## Usage
### Clone
* Clone this repository:
```
git clone https://github.com/digital-dream-labs/vector-animations
```
### Run
* Shift to the project directory:
```
cd vector-animations/
```
- To build the assets that can be copied onto Vector, run the python script called `scripts/buildScripts/animation_assets.py`
- Here's a list of arguments that can be used:
```
--flatc                     Absolute path from the root of your system to the flatc binaries

--verbose                   Prints extra output (No additional argument required)

--replace-existing-assets   Replaces existing assets

--asset-relocation-dir      Absolute path to the dir you want to export the assets
-h, --help                  Show this help message and exit
```
-  Here's an example run command:
```

python scripts/buildScripts/animation_assets.py --flatc-exe-dir <PATH_FLATC_DIR>

```
- The above command will create a folder named `_built_assets`. It contains the required assets in the necessary formats.
- You can change this folder by providing a path to your desired directory
```
python scripts/buildScripts/animation_assets.py --flatc-exe-dir <PATH_FLATC_DIR> --asset-relocation-dir <PATH_DESIRED_DIR>
```
- If you want to replace assets from an existing directory, use the `replace-existing-assets` option
```
python scripts/buildScripts/animation_assets.py --flatc-exe-dir <PATH_FLATC_DIR> --replace-existing-assets
```

## Example Modification Tool

We've included a modification script that lets you make a wide variety
of customizations without having to write any code. To give vector
beady eyes:

```
python3 ./scripts/exampleScripts/modifyEyes.py --transform scale --params EyeScaleX EyeScaleY --values 0.25
python3 ./scripts/buildScripts/animation_assets.py --replace-existing-assets
```

Then deploy changes to the robot (See the "Installation Onto A Vector Robot" section).

To create your own modifications there are four basic transformations
you can apply:

* `scale` multiply existing value by provided value
* `add` add provided value to existing value
* `replace` - replace existing value with provided value
* `random` insert random value with a certain range

There are an extensive amount of options that can be modified with
this tool:

* EyeCenterX
* EyeCenterY
* EyeScaleX
* EyeScaleY
* EyeAngle
* LowerInnerRadiusX
* LowerInnerRadiusY
* UpperInnerRadiusX
* UpperInnerRadiusY
* UpperOuterRadiusX
* UpperOuterRadiusY
* LowerOuterRadiusX
* LowerOuterRadiusY
* UpperLidY
* UpperLidAngle
* UpperLidBend
* LowerLidY
* LowerLidAngle
* LowerLidBend
* Saturation
* Lightness
* GlowSize
* HotSpotCenterX
* HotSpotCenterY
* GlowLightness

Transformations can be chained by running the command multiple
times. Here we make some o_O eyes:

```
./scripts/exampleScripts/modifyEyes.py --transform scale --params EyeScaleX EyeScaleY --values 0.25 --eye left
./scripts/exampleScripts/modifyEyes.py --transform scale --params EyeScaleX EyeScaleY --values 1.25 --eye right
```

Here we move the eyes further apart than normal:

```
./scripts/exampleScripts/modifyEyes.py --transform add --params EyeCenterX --values -5
./scripts/exampleScripts/modifyEyes.py --transform add --params EyeCenterY --values 5
```

Your imagination is the only limit to creating a new look for your
very own Vector!

Once you have the code the way you like it, don't forget to save it:

```
git checkout -b myAwesomeVector
git add assets
git commit -m "My Awesome Vector's new look"
```

Don't like the changes you made this go-around? Reset your changes (This will delete all work since your last commit! Use carefully.):
```
git reset --hard
```

## Installation Onto A Vector Robot
Let's install your new animations onto your Vector!

### Backing Up Existing Animations On the Robot:
* First, we need to make a backup copy of the existing animations that are on the robot. We will use SCP to download these animations and store them in a memorable folder. All of the animation asset subfolders on the robot are stored in the following directory in Vector: ```/anki/data/assets/cozmo_resources/assets/```

* This directory also contains other assets for audio engines, etc., which we won't really touch right now (but we will back them up just to be careful!)

* SCP commands follow the syntax "scp <flags> <origin> <destination>". Using the "-r" flag to make the SCP request recursive, and using the "-i" argument to specify the location of our private SSH key, let's issue an SCP command to copy all of the files on the robot to our local computer. Bear in mind that this may take 5-10 minutes to fully transfer all of the files:

* Command:
```scp -r -i <SSH Key Location> root@<Vector IP Address>:/anki/data/assets/cozmo_resources/assets <Storage Folder on Computer>```

* Example (Windows):
```scp -r -i C:\Users\robbie\.ssh\id_rsa_Vector-F7V3 root@192.168.50.20:/anki/data/assets/cozmo_resources/assets C:\Users\robbie\Downloads```

* Example (Mac/Linux):
```scp -r -i /home/robbie/Downloads/id_rsa_Vector-F7V3 root@192.168.50.20:/anki/data/assets/cozmo_resources/assets /home/robbie/Downloads/assets```

### Placing New Animations On The Robot:
Once we have backed up the animations on the robot (if something goes wrong here and you have no backups, you will have to reload the firmware), then our next step is to use the SCP tool to copy over the new animations to the robot. SCP will keep the permissions of the old file when overwriting files. Bear in mind that this may take 5-10 minutes to fully transfer all of the files.

* Command:
```scp -r -i <SSH Key Location> <Storage Folder on Computer>\* root@<Vector IP Address>:/anki/data/assets/cozmo_resources/assets```

* Example (Windows):
```scp -r -i C:\Users\robbie\.ssh\id_rsa_Vector-F7V3 C:\GitHub\DDL\vector-animations\_built_assets\* root@192.168.50.20:/anki/data/assets/cozmo_resources/assets```

* Example (Mac/Linux):
```scp -r -i /home/robbie/Downloads/id_rsa_Vector-F7V3 /home/robbie/Documents/GitHub/DDL/vector-animations/_built_assets/* root@192.168.50.20:/anki/data/assets/cozmo_resources/assets```

Once all of the animation files have been transferred over, you will need to reboot Vector! Either SSH into your Vector and issue the command ```sudo reboot``` or you can hold his back button for 5 seconds to turn him off. Wait for his screen to go black, then tap the back button again once to boot him back up. 
