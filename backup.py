import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, destination_dir):
    try:
        if not os.path.isdir(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found.")
        if not os.path.isdir(destination_dir):
            raise FileNotFoundError(f"Destination directory '{destination_dir}' not found.")

        for filename in os.listdir(source_dir):
            src_path = os.path.join(source_dir, filename)
            if os.path.isfile(src_path):
                dest_path = os.path.join(destination_dir, filename)
                if os.path.exists(dest_path):
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    filename_parts = os.path.splitext(filename)
                    new_filename = f"{filename_parts[0]}_{timestamp}{filename_parts[1]}"
                    dest_path = os.path.join(destination_dir, new_filename)

                shutil.copy2(src_path, dest_path)
                print(f"✔️  Backed up: {filename} -> {os.path.basename(dest_path)}")

    except Exception as e:
        print(f"❌ Error during backup: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
    else:
        backup_files(sys.argv[1], sys.argv[2])
