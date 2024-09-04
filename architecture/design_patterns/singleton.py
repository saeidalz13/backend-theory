import json
from typing import Any 

class ConfigManager:
    _configs = None
    # _instance = None
    
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
            
    #     return cls._instance
    
    @classmethod
    def load_config(cls, config_path: str):
        if cls._configs is None:
            with open(config_path, "r") as f:
                cls._configs = json.load(f)
                
    @classmethod
    def get(cls, key: str) -> Any:
        if cls._configs is None:
            ValueError("no config file has been loaded yet")
            
        return cls._configs.get(key)

    def __str__(self) -> str:
        return f"{self._configs}"
    
    
if __name__ == "__main__":
    ConfigManager.load_config("somefile.json")
    pass
    