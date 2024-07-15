# MiniDB

### Overview

This project implements a simple key-value store database that communicates over a TCP interface. It supports setting and looking up key-value pairs and ensures data durability by saving the database state to a pickle file.

---

### Components

1. **Server (`server.py`)**: Manages client connections and processes commands.
2. **Database (`database.py`)**: Handles key-value storage and persistence.
3. **Client (`client.py`)**: Interface for users to interact with the server.

---

### Requirements

- Python 3.10.12

---

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/alexandredsz/minidb
    cd minidb
    ```

2. **Dependencies**:
   
    This project does not have external dependencies apart from Python standard libraries.

3. **Directory Structure**:
   
    Ensure your directory structure matches the following:

    ```
    minidb/
    ├── README.md
    ├── src/
    │   ├── data/
    │   │   └── db_data.pkl
    │   ├── server.py
    │   ├── database.py
    │   └── client.py
    ```

---

### Running the Server

1. **Navigate to the `src` directory**:

    ```bash
    cd src
    ```

2. **Start the server**:

    ```bash
    python server.py
    ```

    The server will start listening on `127.0.0.1:8000`.

---

### Running the Client

1. **Open a new terminal window**.
2. **Navigate to the `src` directory**:

    ```bash
    cd src
    ```

3. **Start the client**:

    ```bash
    python client.py
    ```

4. **Enter commands**:

    Refer to the [Command Reference](#command-reference) section for details on how to use the commands.

> [!IMPORTANT]
>-  Ensure the server is running before starting the client.
>- The client and server must run on the same machine (`127.0.0.1`) and port (`8000`), unless modified in the code.
>- The client and server should be run in separate terminal windows.

---

### Command Reference

- **SET `key` `value`**:
  
  Stores the value under the specified key.

  Example:

  ```bash
  SET name Alice
  ```

  Response:

  ```
  The key 'name' has been set to 'Alice'.
  ```

- **LOOKUP `key`**:
  
  Retrieves the value associated with the specified key.

  Example:

  ```bash
  LOOKUP name
  ```

  Response:

  ```
  Alice
  ```

- **Invalid Commands**:

  Any command that does not follow the `SET` or `LOOKUP` syntax will result in an error message.

- **Exit the client**:

  ```bash
  exit
  ```

  This will disconnect the client from the server.

---
>[!NOTE]
>The database ensures durability by saving the state to `src/data/db_data.pkl`. When the server starts, it loads the existing data from this file. Any changes during the server's runtime are automatically saved to this file, ensuring data persistence across restarts.

### Project by

[Alexandre Diniz](https://github.com/alexandredsz), Computer Science student at UFMS

