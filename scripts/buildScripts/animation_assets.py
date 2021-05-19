#!/usr/bin/env python2

import os
import sys
import shutil
import argparse

# DDL modules/packages
import binary_conversion

PROJECT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
ASSETS_DIR = os.path.abspath(os.path.join(PROJECT_DIR, 'assets'))
BUILT_ASSETS_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '_built_assets'))
BINARY_CONVERSION_FOLDERS = ['animations']

def parse_args(argv=[]):
    """
    Parse the arguments provided by the user
    :param argv: List of arguments
    :return: Parsed user provided arguments
    """
    parser = argparse.ArgumentParser(description='Place animation assets')
    parser.add_argument('--verbose',
                        action='store_true',
                        help='Prints extra output')
    parser.add_argument('--replace-existing-assets',
                        action='store_true',
                        default=False,
                        help='Replaces existing assets')
    parser.add_argument('--asset-relocation-dir',
                        action='store',
                        default=BUILT_ASSETS_DIR,
                        help='Absolute path to the dir you want to export the assets')
    parser.add_argument('--flatc',
                        action='store',
                        default='',
                        help='Absolute path from the root of your system to the dir containing flatc executables')

    options, _ = parser.parse_known_args(argv)
    return options

def listdir_nohidden(path):
    """
    Get a non-hidden files from a directory
    :param path: Absolute path to directory
    :return: List of items at the top level of the directory
    """
    dir_list = []
    for dir in os.listdir(path):
        if not dir.startswith('.'):
            dir_list.append(dir)
    return dir_list

def convert_json_to_binary(json_files, bin_name, dest_dir, flatc_loc=''):
    """
    Convert given JSON files into a single binary
    :param json_files: List of JSON file to convert (list contains absolute path to each file)
    :param bin_name: Name of the binary to be generated
    :param dest_dir: Absolute path to the directory where binary is to be stored
    :param flatc_loc: Absolute path to the flatc binaries
    :return: Nothing
    """
    bin_name = bin_name.lower()
    try:
        bin_file = binary_conversion.main(json_files, bin_name, flatc_loc)
    except Exception as e:
        print("%s: %s" % (type(e).__name__, e.message))
        # If binary conversion failed, use the json files...
        for json_file in json_files:
            json_dest = os.path.join(dest_dir, os.path.basename(json_file))
            shutil.copy(json_file, json_dest)
            print("Restored %s" % json_dest)
    else:
        bin_dest = os.path.join(dest_dir, os.path.split(bin_file)[1])
        shutil.move(bin_file, bin_dest)
        
def place_animation_assets(location, flatc_loc='', replace_existing_assets=False):
    """
    Place required animation assets into a desired directory
    :param location: Absolute path to the directory where the assets need to be placed
    :param flatc_loc: Absolute path to the flatc binaries
    :param replace_existing_assets: Replaces existing assets; Set to true if you want to replace existing assets
    :return: Nothing
    """
    if replace_existing_assets:
        print("[WARN] Existing assets will be replaced!")
    # Go through each type of assets
    for dir in listdir_nohidden(ASSETS_DIR):
        dst_path = os.path.join(location, dir)
        if (os.path.isdir(dst_path) and replace_existing_assets) or (os.path.isdir(dst_path) and not listdir_nohidden(dst_path)):
            shutil.rmtree(dst_path)
        if not os.path.isdir(dst_path):
            print('Working on ' + dir + '...')
            if dir not in BINARY_CONVERSION_FOLDERS:
                shutil.copytree(os.path.join(ASSETS_DIR, dir), dst_path)
            else:
                os.makedirs(dst_path)
                conv_dir_path = os.path.join(ASSETS_DIR, dir)
                for sub_dir in listdir_nohidden(conv_dir_path):
                    src_path = os.path.join(conv_dir_path, sub_dir)
                    files = list(listdir_nohidden(src_path))
                    files = map(lambda x: os.path.join(src_path, x), files)
                    convert_json_to_binary(files, sub_dir, dst_path, flatc_loc)
        else:
            print(dir + ' already exists!')
    
    
if __name__ == '__main__':
    options = parse_args(sys.argv[1:])
    relocation_dir = os.path.abspath(options.asset_relocation_dir)
    if options.verbose:
        print("asset-relocation-dir: {}".format(relocation_dir))
    if not options.flatc:
        print("[WARN] Path to flatc binaries not provided!\nChecking if flatc is installed on the system...")
        if not binary_conversion.is_flatc_installed():
            sys.exit("[ERROR] Flatc not found! Try installing it using the package manager of your choice.")
    place_animation_assets(relocation_dir, options.flatc, options.replace_existing_assets)
