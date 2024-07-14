import os
import pickle

DATA_FILE = 'data/db_data.pkl'  # File to save database

class MiniDatabase:
    def __init__(self):
        self.data = {}
        self.load_data()

    def load_data(self):
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
        try:
            f = open(DATA_FILE, 'wb')
            pickle.dump(self.data, f)
        except Exception as e:
            print(f"Error saving data: {e}")

    def set_value(self, key, value):
        self.data[key] = value
        self.save_data()

    def lookup_value(self, key):
        return self.data.get(key, "Key not found")

    def process_command(self, command):
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