import os
import pickle

DATA_FILE = 'data/db_data.pkl'  # File to save database

class MiniDatabase:
    r"""
    A simple key-value store database.
    """

    def __init__(self):
        r"""
        Initialize the database and load existing data from file.
        """
        self.data = {}
        self.load_data()

    def load_data(self):
        r"""
        Load database from file if it exists, otherwise create a new file.
        """
        try:
            if os.path.exists(DATA_FILE):
                f = open(DATA_FILE, 'rb')
                self.data = pickle.load(f)
            else:
                f = open(DATA_FILE, 'wb')
                pickle.dump(self.data, f)

        except EOFError:
            pass
        except Exception as e:
            print(f"Error loading data: {e}")

        finally:
            f.close()

    def save_data(self):
        r"""
        Save current database state to file.
        """        
        try:
            f = open(DATA_FILE, 'wb')
            pickle.dump(self.data, f)
        except Exception as e:
            print(f"Error saving data: {e}")

    def set_value(self, key, value):
        r"""
        Set a key-value pair in the database.

        Args:
            key (str): The key to be set.
            value (str): The value to be set for the key.
        """
        self.data[key] = value
        self.save_data()

    def lookup_value(self, key):
        r"""
        Look up a value by key.

        Args:
            key (str): The key to be looked up.

        Returns:
            str: The value associated with the key, or a message if the key is not found.
        """
        return self.data.get(key, "Key not found")

    def process_command(self, command):
        r"""
        Process a command to set or look up a key-value pair.

        Args:
            command (str): The command to be processed, either 'SET key value' or 'LOOKUP key'.

        Returns:
            str: A message indicating the result of the command.
        """
        parts = command.strip().split()
        if len(parts) >= 3 and parts[0] == "SET":
            key = parts[1]
            value = ' '.join(parts[2:])
            self.set_value(key, value)
            return f"The key '{key}' has been set to '{value}'."

        elif len(parts) == 2 and parts[0] == "LOOKUP":
            key = parts[1]
            return self.lookup_value(key)

        else:
            return "Error: Invalid command"