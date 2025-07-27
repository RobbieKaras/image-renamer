# 🖼️ Image Renamer Script

This Python script recursively scans a folder and its subdirectories, identifies image files, and renames them using a standardized format (`image.jpg`, `image_1.png`, `image_2.jpeg`, etc.).

## Features

- Recursively scans folders and subfolders  
- Supports common image file types (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp`)  
- Automatically renames images in each folder using a consistent naming pattern  
- Skips non-image files  
- Prints logs for every file processed and renamed

## How It Works

1. Set the `root_dir` variable to the folder path you want to scan.
2. The script walks through the folder and all subfolders.
3. For every image found, it renames it to `image`, `image_1`, `image_2`, etc., within its respective folder.

## Example

If a folder contains:

```
photo.jpg  
dog.png  
cat.jpeg
```

After running the script, it becomes:

```
image.jpg  
image_1.png  
image_2.jpeg
```

## Getting Started

### 1. Make sure Python is installed

Run the following command to check:

```bash
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### 2. Set the folder path in the script

Update the `root_dir` variable to point to your target directory:

```python
root_dir = r'C:\Users\YourName\Desktop\your_folder'
```

### 3. Run the script

From your terminal or command prompt:

```bash
python image_renamer.py
```

## Supported Image Formats

- `.png`  
- `.jpg`  
- `.jpeg`  
- `.gif`  
- `.bmp`  
- `.webp`

## Notes

- Files will be renamed **in place** — original filenames will be overwritten.
- Make a backup if you want to preserve the original names.

## Contributing

Pull requests are welcome!  
Please ensure any changes are tested and clearly documented.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
"# image-renamer" 
