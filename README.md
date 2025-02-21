File Organizer Script
Version: 1.0
Author: Sean Tripp

Description:
This tool automatically organizes files in a folder based on file type categories specified in settings.txt. It also includes a revert function to restore files to their original locations if needed.

How to Use

1. Setup
Extract the .zip file and place it in the folder you want to organize.
Open settings.txt to configure file categories and extensions.

2. Editing settings.txt
The settings file allows you to customize how files are organized.

Example Format:
Use_Revert: False  
Use_Misc: True  

Images: .png, .jpg, .jpeg, .gif  
Documents: .txt, .pdf, .docx, .csv  
Scripts: .py, .js, .html  
Videos: .mp4, .avi, .mov
  
Explanation:

Use_Revert: True → Moves files back to their original locations.
Use_Misc: True → Moves unknown file types to a Misc folder.
Each category (e.g., Images) has a list of extensions to be sorted.

3. Running the Organizer
Double-click organize_folder.exe.
It will organize files based on settings.txt.
If Use_Revert is enabled, it will undo the last organization.

4. Reverting Files
If Use_Revert: True, files will be restored using history.log.
After reverting, history.log will be deleted.

Important Notes
✔ Ensure settings.txt is in the same folder as organize_folder.exe.
✔ The script does not validate extensions, so double-check your settings.
✔ Windows does not allow duplicate file names, so files will not be overwritten.
✔ Run in a folder with files, not an empty one.

Need Help?
For support, contact trippiscoding@gmail.com
