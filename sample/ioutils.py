__author__ = 'sapphire'

import os
import os.path


def list_files_only(folder_path):
    return filter(os.path.isfile, [os.path.join(folder_path, name) for name in os.listdir(folder_path)])
