### GGUF caller

[<img src="https://raw.githubusercontent.com/calcuis/cgg/master/cgg.gif" width="128" height="128">](https://github.com/calcuis/cgg/blob/main/cgg.gif)

This package is a GGUF (GPT-Generated Unified Format) file/model caller.
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

### clone feature: cgg clone [URL]
With this feature, you can clone any GGUF model/file from URL, save it in the current directory, and get it ready to connect locally (run it with your own machine); depends on the file size, it may take a while to complete the clone process, please be patient.

A known issue for Mac user(s): <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED](https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica) > (solution: Install Certificates.command)

#### sample model(s) available to download (try out)
For general purpose
https://huggingface.co/calcuis/chat/blob/main/chat.gguf (size: around 2GB or less)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/chat.gguf
```
For coding
https://huggingface.co/calcuis/code_mini/blob/main/code.gguf (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/code.gguf
```
For health/medical advice
https://huggingface.co/calcuis/medi_mini/blob/main/medi.gguf (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/medi.gguf
```
***those are all experimental models; no guarantee on quality
