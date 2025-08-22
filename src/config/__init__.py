import src.config._directory as _directory
import src.config._implemented_modules as _implemented_modules
import src.config._imported_modules as _imported_modules
from src.config._directory import DIRECTORY
from src.config._imported_modules import IMPORTED_MODULES

_directory.setup()
_imported_modules.setup()
