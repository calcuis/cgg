### GGUF caller

[<img src="https://raw.githubusercontent.com/calcuis/cgg/master/cgg.gif" width="128" height="128">](https://github.com/calcuis/cgg)
[![Static Badge](https://img.shields.io/badge/cgg-release-blue?logo=github)](https://github.com/calcuis/cgg/releases)

This package is a GGUF (GPT-Generated Unified Format) file/model caller. Perfect to run in low end device(s).
#### install the caller via pip/pip3 (once only):
```
pip install cgg
```
#### update the caller (if not in the latest version) by:
```
pip install cgg --upgrade
```
### user manual
This is a cmd-based (command line) package, you can find the user manual by adding the flag -h or --help.
```
cgg -h
```
#### check current version
```
cgg -v
```
#### connector menu
```
cgg menu
```
### graphical user interface (GUI) caller
Simple GUI to interact with a chat model for generating responses (recommended).
#### call cpp connector:
```
cgg cpp
``` 
#### call c connector:
```
cgg c
```
### command line interface (CLI) caller
CLI input also provided for expert/advanced user(s).
#### call gpp connector:
```
cgg gpp
```
#### call g connector:
```
cgg g
```

GGUF file(s) in the same directory will automatically be detected by the caller, hence, a selection menu will be shown in the console as below.

[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo.gif)
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo1.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo1.gif)

### clone feature
```
cgg clone [url]
```
With this fast clone feature, you can clone any (GGUF model) file from URL, save it automatically in the current directory, and get it ready to connect locally (run it with your own machine offline); depends on the file size, as well as the network connectivity, it may take a while to complete the clone process; and you can see a dynamic progress bar showing the downloading status in this latest version. (an universal issue was detected for mac users: ssl cert. verify failed; possible solution: click Install Certificates.command under your Python version folder; details please refer to [issues](https://github.com/calcuis/cgg/issues) reported)

#### sample model(s) available to download (try out)
For general purpose
[chat.gguf] (size: around 2GB or less)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/chat.gguf
```
For coding
[code.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/code.gguf
```
For health/medical advice
[medi.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/medi.gguf
```
***those are all experimental models; no guarantee on quality

#### sample model list
You can either use the clone feature above or opt a sample GGUF straight from the (download ready) lazy list by:
```
cgg s
```
More options might be found on list as it can be updated independently (without affecting the code).