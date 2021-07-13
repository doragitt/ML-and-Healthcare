Report

Raw data

1) the 'archive' zip contains the three intial raw data files.

Data Mining

2) 'Initialdata' contains the initial data in the excel file processed till the S2N Value and the T-Value. Data 
preprocessing is done in this file

3) 'Finaldata' contains  5 sheets within it: sorted according to S2N values, 
top 50 s2n values, sorted according to t value, top 50 t value genes, common genes to sheet 2 and sheet 4
respectively

4) The file named 'codes for excel files' is the code file which contains all the code/ formulae 
used in the excel file. 

Scatter plot visualisation

5) The file named scatter plot_code_file is the python file which contains the code for plotting the scatter plots. Run it a python IDE 
like pycharm

6) Result 1,2,3 contain the three images which are the graphs. These are results of data
visualisation. These  are scatter plots.

Readme File for codes for classification and the most important documents of this project

7) We have total 4 files of code after the completion of Report-4. 

8)Three code files are as follows:'Set-1 AML_ALL_graphs_likelihood', 'Set-2 AML_ALL_graphs_likelihood', 'Set-3 AML_ALL_graphs_likelihood'

9)In these 3 files we can get the Normal distribution curve for set-1, set-2, set-3 data which will help us calculate the likelihood and posterior.

10)It plots graph and give us the value of likelihood for AML and ALL graphs.

11)You can simply run this file by providing the value of variable (gene data of patient which will be input to the graph to calculate the likelihood) which you can choose fron 'finaldata.xlsx' sheet (sheet5). 

12)However I have already chosen the data and plotted the graph taking the data of the X59417_at, M92287_at, M31523_at  genes.

13) Just with the help of Run command( in pycharm ide)  you could get the graph plotted in all three cases as well as values of likelihood also.

14) x, y, z  in the three files denotes the three genes chosen and their corresponding data for training the model.

15) In file 4, which is named as 'Final Code' we have computed the Posterior with the help of all these three graphs. The posterior is computed for data chosen for three patients from the sheet.

16) If the desired input is matched to output the test get passed otherwise it will fail. If the patient class is ALL and the posterior for ALL is greater than that for AML, then the case is passed and our model is correct.

17) We have taken two data of AML and one of ALL for testing our model. 

18) We obtained 100% efficiency in all the three test cases. This proves our model is correct. 

19) This file can simply by run by hitting on Run command(pycharm).

20)All required comments are added in every graphs.

21)A lot of comments are added for the easy understanding in the code also. 

22) By the name 'Report 4', we have the word file and the pdf of the report 4, the final report



