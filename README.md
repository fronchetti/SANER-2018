## SANER 2018: How Scientists Develop Scientific Software

This repository contains the main files used in the repositories analysis section of the paper "How Scientists Develop Scientific Software" ([DOI: 10.1109/SANER.2018.8330263](http://doi.org/10.1109/SANER.2018.8330263)). If you want to reproduce our data, please read on the steps.

### Steps for Survey Analysis

The survey material is available at the Survey folder.

1. The survey responses are available [here](https://github.com/fronchetti/SANER-2018/tree/master/Survey/actual.csv). The pilot is available [here](https://github.com/fronchetti/SANER-2018/tree/master/Survey/pilot.csv).
2. To create the likert figures, you just need to run ```Rscript likert.R```
3. To create the histogram figure, you just need to run ```Rscript worktime.R```

### Steps for Mining Scientific Software
1. Clone our repository using: ```git clone https://github.com/fronchetti/SANER-2017```. <br>
2. To reproduce the data collection process: ```python data_collector.py```. This script will create folders and files related to all the projects that are inside <i>responses.csv</i>, and you may need to allow it in your system. The collected data will be available in the <i>Dataset</i> folder.<br>

  If you want to jump this step, just use our compacted version of the <i>Dataset</i> folder:
  https://github.com/fronchetti/SANER-2018/tree/master/Dataset

3. The <i>summary.csv</i> file contains general information about the projects. If you want to recreated this file use: ```python data_information.py```. <b> Step required to generate boxplots</b>.

4. The <i>quarters.csv</i> file contains the frequency of commits in all projects, grouped by quarters. If you want to recreated this file use: ```python data_timeseries.py```. <b> Step required to generate time series</b>.

5. If you want to generate our charts, use <i>summary.R</i>. Ready versions of <i>summary.csv</i> and <i>quarters.csv</i> are available in this repository.

####  Used settings

| Software | Version |
|----------|----------------------|
| Linux | Ubuntu Gnome (16.04) |
| Python | 2.7.12 |
| RStudio  | 1.1.383 |

### * Contact
Troubles? Feel free to get in touch: <br>
Luiz Felipe Fronchetti - fronchetti at usp br <br>
Gustavo Pinto - gpinto at ufpa br
