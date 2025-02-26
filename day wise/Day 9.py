import requests
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def download_image(url):
    # Download the image content
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Hide the root window before opening the save dialog
        root = Tk()
        root.withdraw()

        # Ask the user to where to save the image
        filetypes = [("JPEG Image", "*.jpg"), ("PNG Image", "*.png"), ("All Files", "*.*")]
        save_path = asksaveasfilename(title="Save Image As...", defaultextension=".jpg", filetypes=filetypes)
        if save_path:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print("Image downloaded and saved successfully!")
        else:
            print("Save canceled.")
    else:
        print("Failed to download the image. Check the URL.")

if __name__ == "__main__":
    url = input("Enter the image URL: ")
    download_image(url)
