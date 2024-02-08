# Chatbot Installation and Setup Guide

## Installation and Requirements

### Python Version
**Tested Version**: Python 3.10.8 (Likely compatible with other Python 3 versions).

### Required Packages
- Install the necessary packages listed in `requirements.txt`.
- You can also do it by running the following command in the project's main directory:
  ```bash
  sudo pip3 install -r requirements.txt
  ```

## Running the Chatbot

### Development Environment
1. Navigate to the project's main directory.
2. Run the chatbot using the command:
   ```bash
   sudo python3 main.py
   ```
3. The chatbot will be available on **port 80**.

#### Additional Notes for Development:
- To access the chatbot from other computers, ensure the required ports are open in the EC2 instance.
- In an Ubuntu environment, consider using:
  ```bash
  sudo nohup python main.py &
  ```
  for background running.

### Production Environment
1. Add the following import to `main.py`: ```from waitress import serve```.
2. Modify the `main.py` file for production use:
 ```python
if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=80)
 ```
3. Run the chatbot using:
   ```bash
   sudo python3 main.py
   ```
   Alternatively, for background execution, use:
     ```bash
     sudo nohup python3 main.py &
     ```
3. The chatbot will now be available on the default **port 80** (Ensure that port 80 is accessible on your EC2 instance).

### How to check the server statues?
Run the command:
```
ps -ef | grep python
```
And look for process ids of the relevant processes.

### How to kill the server?
Run:
```
sudo kill -9 16904 16905 16906
```
Make sure to substitude the ids with the those you found earlier.

### Optional: If there are still troubles and the server cannot be reached...
Update firewall rules:
```
sudo ufw allow 80/tcp
sudo ufw allow 80
```
