import os

def sanitize_filename(filename):
    """Sanitizes a filename to remove problematic characters."""
    return filename.replace("%20", " ").replace("+", " ")

def create_album_folder(album_name):
    """Creates a folder for the album inside 'album_downloaded'."""
    base_folder = "album_downloaded"
    album_path = os.path.join(base_folder, album_name)

    os.makedirs(album_path, exist_ok=True)
    print(f"Created album folder: {album_path}")
    
    return album_path