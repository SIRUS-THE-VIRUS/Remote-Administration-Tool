# Computer Security - Remote Administration Tool

**I will not be responsible for any direct or indirect damage caused due to the usage of this tool, it is for educational purposes only.**

**Currently, supports the key logging and access to files and directories**

***

It consists of two parts :

* Server side (server.py) : This is what we are going to place on the victims computer

* Client side (client.py) : This is what the attacker will use to connect the server on to control the victims computer

****

## Installation

Use git-clone to download and run with python3

Required Libraries : [Socket](https://docs.python.org/3/library/socket.html), [Pynput](https://pypi.org/project/pynput/), [Subprocess](https://docs.python.org/3/library/subprocess.html), [logging](https://docs.python.org/3/library/logging.html), [OS](https://docs.python.org/3/library/os.html)

```bash
git clone https://github.com/SIRUS-THE-VIRUS/Computer-Security-RAT.git
```

## Usage

* Modify the IP address and Port for the socket connection at your discretion. 

* Get server.py onto the victim computer

* Get the victim to execute the server

* Connect to the server from the attacker's computer using client.py



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
