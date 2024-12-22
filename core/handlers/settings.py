import yaml

class Settings:
    def __init__(self, config_path="config/project_config.yaml"):
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def set(self, key, value):
        self.config[key] = value

    def get(self, key, default=None):
        return self.config.get(key, default)