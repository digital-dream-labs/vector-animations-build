#!/usr/bin/env python3

import glob
import json
import enum
import random
import argparse

class ProceduralFaceParams(enum.IntEnum):
  EyeCenterX = 0         # { false, false,  0.f,  0.f, EyeParamCombineMethod::Add,      {-FACE_DISPLAY_WIDTH/2, FACE_DISPLAY_WIDTH/2 }    }     },
  EyeCenterY = 1         # { false, false,  0.f,  0.f, EyeParamCombineMethod::Add,      {-FACE_DISPLAY_HEIGHT/2,FACE_DISPLAY_HEIGHT/2}    }     },
  EyeScaleX = 2          # { false, false,  1.f,  0.f, EyeParamCombineMethod::Multiply, {0.f, 10.f}    }     },
  EyeScaleY = 3          # { false, false,  1.f,  0.f, EyeParamCombineMethod::Multiply, {0.f, 10.f}    }     },
  EyeAngle = 4           # { true,  false,  0.f,  0.f, EyeParamCombineMethod::Add,      {-360, 360}    }     },
  LowerInnerRadiusX = 5  # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  LowerInnerRadiusY = 6  # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  UpperInnerRadiusX = 7  # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  UpperInnerRadiusY = 8  # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  UpperOuterRadiusX = 9  # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  UpperOuterRadiusY = 10 # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  LowerOuterRadiusX = 11 # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  LowerOuterRadiusY = 12 # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  UpperLidY = 13         # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  UpperLidAngle = 14     # { true,  false,  0.f,  0.f, EyeParamCombineMethod::Add,      {-45,  45}    }     },
  UpperLidBend = 15      # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {-1.f, 1.f}    }     },
  LowerLidY = 16         # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {0.f, 1.f}    }     },
  LowerLidAngle = 17     # { true,  false,  0.f,  0.f, EyeParamCombineMethod::Add,      {-45,  45}    }     },
  LowerLidBend = 18      # { false, false,  0.f,  0.f, EyeParamCombineMethod::None,     {-1.f, 1.f}    }     },
  Saturation = 19        # { false, true,  -1.f,  1.f, EyeParamCombineMethod::None,     {-1.f, 1.f}   }     },
  Lightness = 20         # { false, true,  -1.f,  1.f, EyeParamCombineMethod::None,     {-1.f, 1.f}   }     },
  GlowSize = 21          # { false, true,  -1.f, 0.0f, EyeParamCombineMethod::None,     {-1.f, 1.f}   }     },
  HotSpotCenterX = 22    # { false, true,   0.f, 0.0f, EyeParamCombineMethod::Average,  {-1.f, 1.f}   }     },
  HotSpotCenterY = 23    # { false, true,   0.f, 0.0f, EyeParamCombineMethod::Average,  {-1.f, 1.f}   }     },
  GlowLightness = 24     # { false, true,   0.f, 0.f,  EyeParamCombineMethod::None,     {0.f, 1.f}   }     },

def make_scale_transform(params, scale_value):
  def scaler(eye_data):
    for param in params:
      eye_data[param] *= scale_value

  return scaler

def make_add_transform(params, add_value):
  def adder(eye_data):
    for param in params:
      eye_data[param] += add_value

  return adder

def make_replace_transform(params, replace_value):
  def scaler(eye_data):
    for param in params:
      eye_data[param] = replace_value

  return scaler

def make_random_transform(params, lower_limit, upper_limit):
  def scaler(eye_data):
    for param in params:
      eye_data[param] = random.uniform(lower_limit, upper_limit)

  return scaler

def crawl_files(glob_string, transforms, eyes=['leftEye','rightEye']):
  json_files = glob.glob(glob_string)
  for json_file in json_files:
    json_data = json.loads(open(json_file,"r").read())
    for key, vals in json_data.items():
      print(key)
      for val in vals:
        if val["Name"] == "ProceduralFaceKeyFrame":
          for transform in transforms:
            for eye in eyes:
              transform(val[eye])
    with open(json_file,"w") as f:
      f.write(json.dumps(json_data, indent=2))

      
#random_eyes = [make_random_transform([ProceduralFaceParams.EyeScaleX, ProceduralFaceParams.EyeScaleY], 0.35, 1.35)]
#crawl_files("./assets/animations/**/*.json", random_eyes)

parser_desc = """Modify procedural eyes to give Vector a whole new look and feel

This script allows you to modify the contents of Vector's eye animations in a variety of ways. Here are a few examples:

# Give vector beady eyes by making them 25% original size
python3 modifyEyes.py --transform scale --params EyeScaleX EyeScaleY --values 0.25

# Give vector o_O eyes by scaling each one differently.
modifyEyes.py --transform scale --params EyeScaleX EyeScaleY --values 0.25 --eye left
modifyEyes.py --transform scale --params EyeScaleX EyeScaleY --values 1.25 --eye right

# Randomize eye size for each key frame
modifyEyes.py --transform random --params EyeScaleX EyeScaleY  --values 0.35 1.35

# Move eyes further apart
modifyEyes.py --transform add --params EyeCenterX --values -5
modifyEyes.py --transform add --params EyeCenterY --values 5


"""

eye_lookup = {'left': ['leftEye'], 'right': ['rightEye'], 'both': ['leftEye','rightEye']}
transform_lookup = {'scale': make_scale_transform, 'random': make_random_transform,
                      'replace': make_replace_transform, 'add': make_add_transform}

def get_args():
  parser = argparse.ArgumentParser(description=parser_desc, formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument('--transform', nargs=1, required=True, choices=transform_lookup.keys())
  parser.add_argument('--params', nargs='+', required=True, choices=[str(param).split(".")[1] for param in ProceduralFaceParams])
  parser.add_argument('--values', nargs='+', required=True)
  parser.add_argument('--eye', choices=eye_lookup.keys(), default='both')
  return parser.parse_args()

def process_cli_command():

  args = get_args()
  values = [float(x) for x in args.values]

  transform_maker = transform_lookup[args.transform[0]]
  params = [ProceduralFaceParams[x] for x in args.params]
  transform_function = transform_maker(params,*values)

  crawl_files('./assets/animations/**/*.json', [transform_function])

if __name__ == "__main__":
  process_cli_command()
