from pathlib import Path
import importlib


class PluginManager:
    """
    Loads JOY plugins dynamically.
    """

    def __init__(self, plugin_directory="plugins"):

        self.plugin_directory = Path(plugin_directory)

        self.plugins = {}

    def load_plugin(self, module_name):

        module = importlib.import_module(module_name)

        self.plugins[module_name] = module

        return module

    def loaded_plugins(self):

        return list(self.plugins.keys())