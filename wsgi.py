import inspect
import os
import site

_this_file_path = inspect.getfile(inspect.currentframe())
_this_folder_path = os.path.dirname(_this_file_path)
site.addsitedir(
    os.path.join(_this_folder_path, 'venv/lib/python3.4/site-packages')
)

from argentum import create_app
application = create_app()
