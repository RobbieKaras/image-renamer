# image_renamer.py
# Renames all image files in a folder and its subfolders to a standard format

import os

root_dir = r'C:\Path\To\Your\Folder'  # ← Change this to your actual folder

image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')

renamed_count = 0

for subdir, dirs, files in os.walk(root_dir):
    print(f"\n📁 Scanning folder: {subdir}")
    image_count = 0
    for file in sorted(files):
        print(f"🔍 Found file: {file}")
        if file.lower().endswith(image_extensions):
            old_path = os.path.join(subdir, file)
            ext = os.path.splitext(file)[1].lower()
            new_filename = f"image{'' if image_count == 0 else f'_{image_count}'}{ext}"
            new_path = os.path.join(subdir, new_filename)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ Renamed: {old_path} -> {new_path}")
                    image_count += 1
                    renamed_count += 1
                except Exception as e:
                    print(f"❌ Error renaming {old_path}: {e}")

print(f"\n🎉 Done! Total images renamed: {renamed_count}")
