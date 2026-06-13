
# 4. @classmethod vs @staticmethod
# Real-world use case: classmethods are heavily used as "Alternative Constructors" (e.g., parsing a dictionary to build an object), and staticmethods are used for utility functions that belong in the class namespace but don't need class/instance data.

# The Scenario: Parsing configuration files for an app.
# The Task: Create an AppConfig class with an __init__ that takes db_url and debug_mode.
# Class Method: Create an alternative constructor using @classmethod called from_dict(cls, data_dict). It should take a dictionary like {"db": "mysql://...", "debug": True} and return a new instance of AppConfig.
# Static Method: Create a @staticmethod called is_valid_db_url(url) that takes a string and returns True if it starts with "postgresql://" or "mysql://", and False otherwise. You don't need self or cls for this check.


class AppConfig:

    def __init__(self, db_url, debug_mode):
        self.db_url = db_url
        self.debug_mode = debug_mode

    @classmethod
    def from_dict(cls, data_dict):
        appconfig = AppConfig(data_dict['db'], data_dict['debug'])
        return appconfig
    
    @staticmethod
    def is_valid_db_url(url):
        if url.startswith('mysql://'):
            return True
        return False
    

dictionary = {'db':'mysql://...', 'debug':False}
print(AppConfig.from_dict(dictionary).db_url)

print(AppConfig.is_valid_db_url('mysql://'))