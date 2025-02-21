import os

# Dictionary mapping screenshots to new names
rename_map = {
    'Screenshot 2025-02-20 at 6.10.47 PM.png': 'portfolio-preview.jpg',
    'Screenshot 2025-02-20 at 6.10.59 PM.png': 'impulsoyz-preview.jpg',
    'Screenshot 2025-02-20 at 6.11.10 PM.png': 'bella-nails-preview.jpg',
    'Screenshot 2025-02-20 at 6.11.19 PM.png': 'casa-estilo-preview.jpg',
    'Screenshot 2025-02-20 at 6.11.27 PM.png': 'urban-style-preview.jpg',
    'Screenshot 2025-02-20 at 6.11.35 PM.png': 'la-mesa-preview.jpg'
}

# Change to images directory
os.chdir('images')

# Remove old preview files if they exist
old_files = ['casa-estilo-preview.jpg', 'la-mesa-preview.jpg']
for old_file in old_files:
    if os.path.exists(old_file):
        os.remove(old_file)

# Rename files
for old_name, new_name in rename_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f'Renamed {old_name} to {new_name}')
