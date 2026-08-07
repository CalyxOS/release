#!/usr/bin/env python3
#
# SPDX-FileCopyrightText: The Calyx Institute
# SPDX-License-Identifier: Apache-2.0
#

import os
import shutil
import fnmatch
import argparse

def copy_and_rename_files(old_channel, new_channel):
    # Always prepend a hyphen to the channel names
    old_keyword = f"-{old_channel}"
    new_keyword = f"-{new_channel}"

    patterns = [f'*{old_keyword}']
    # Skip changelog for factory and oldstable
    if new_channel not in ('factory', 'oldstable'):
        patterns.append(f'*{old_keyword}-changelog.html')

    for root, dirs, files in os.walk('.'):
        if 'ro' in dirs:
            dirs.remove('ro')

        for filename in files:
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                target_filename = filename.replace(old_keyword, new_keyword)

                src_file = os.path.join(root, filename)
                dst_file = os.path.join(root, target_filename)

                print(f"Copying: {filename} -> {target_filename}")
                shutil.copy2(src_file, dst_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy and rename files in-place within current directory.")
    parser.add_argument("old_channel", help="The channel to find (e.g., 'testing')")
    parser.add_argument("new_channel", help="The channel to replace (e.g., 'beta')")

    args = parser.parse_args()

    copy_and_rename_files(args.old_channel, args.new_channel)
