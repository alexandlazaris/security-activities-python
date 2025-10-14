import os
import PyInstaller.__main__

# Define the script to convert and the output executable name
script_name = 'alternate_data_streams.py'
output_name = 'ads_app.exe'

# Use PyInstaller to create the executable
PyInstaller.__main__.run([
    '--name=%s' % output_name,
    '--onefile',  # Create a single executable file
    script_name
])