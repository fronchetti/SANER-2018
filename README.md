## SANER 2018: How Scientists Develop Scientific Software

This repository contains the main files used in the repositories analysis section of the paper "How Scientists Develop Scientific Software". If you want to reproduce our data, please read on the steps.

### * Steps
1. Clone this repository using the ```git clone https://github.com/fronchetti/SANER-2017``` command.
2. Inside the repository, use ```python data_collector.py``` to collect all the necessary data. This script will create folders and files related to all the projects inside <i>repositories.txt</i>, and you may need to allow it.
The collected data will be available in a <i>Dataset</i> folder. If you want to jump this step, just use our compacted version of the <i>Dataset</i> folder.
3. To generate <i>summary.csv</i>, a file with general information about the collected projects, use ```python data_information.py```.
4. Finally, open and execute the <i>summary.R</i> script on your RStudio to visualize the repositories analysis and charts. This script just request <i>summary.csv</i> to be executed, and you can use a version of this file available in our repository.

### * Contact
Doubts? Feel free to get in touch: <br>
Luiz Felipe Fronchetti - fronchettiemail@gmail.com
