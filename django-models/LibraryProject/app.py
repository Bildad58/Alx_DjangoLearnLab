import shutil
import os

# Define the old and new paths
old_path = 'django-models/LibraryProject/relationship_app'
new_path = 'django-models/relationship_app'

# Move the directory
shutil.move(old_path, new_path)