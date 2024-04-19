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

#### metadata reader:
You can check model metadata by:
```
cgg r
```
### clone feature
```
cgg clone [url]
```
With this fast clone feature, you can clone any (GGUF model) file from URL, save it automatically in the current directory, and get it ready to connect locally (run it with your own machine offline); depends on the file size, as well as the network connectivity, it may take a while to complete the clone process; and you are able to see a dynamic progress bar showing the downloading status.

#### sample model(s) available to download (try out)
For general purpose
[chat.gguf] (size: around 2GB or less)
```
cgg clone https://huggingface.co/calcuis/chat/resolve/main/chat.gguf
```
For coding assistance
[code.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/code_mini/resolve/main/code.gguf
```
For health/medical advice
[medi.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/medi_mini/resolve/main/medi.gguf
```
For law/legal opinion
[law.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/law_mini/resolve/main/law.gguf
```
For wealth/financial plan
[finance.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/gguf/resolve/main/finance.gguf
```
For calculation/math solution
[math.gguf] (size: around 3GB or more)
```
cgg clone https://huggingface.co/calcuis/gguf/resolve/main/math.gguf
```
***those are all experimental models; no guarantee on quality

#### sample model list
You can either use the clone feature above or opt it straight from the lazy list by:
```
cgg s
```
[<img src="https://raw.githubusercontent.com/calcuis/gguf-connector/master/demo2.gif" width="350" height="225">](https://github.com/calcuis/gguf-connector/blob/main/demo2.gif)

#### pdf analyzor (beta)
You can load PDF into the model for analysis right away by (analyzor c):
```
cgg pc
```
Or by (analyzor p):
```
cgg pp
```
#### wav recognizor (beta)
You can prompt voice/speech (wav file) as input by (recognizor c):
```
cgg vc
```
Or by (recognizor p):
```
cgg vp
```

#### website
Click [gguf.us](https://gguf.us) or launch it straight from console by:
```
cgg us
```
