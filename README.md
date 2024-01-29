### GGUF model caller

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
Simple GUI to interact with a chat model for generating responses (recommanded).
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

#### sample model(s) available to download (try out)
For general purpose
https://huggingface.co/calcuis/chat/blob/main/chat.gguf

For coding
https://huggingface.co/calcuis/code_mini/blob/main/code.gguf

For health/medical advice
https://huggingface.co/calcuis/medi_mini/blob/main/medi.gguf

***those are all experimental models; no guarantee on quality
