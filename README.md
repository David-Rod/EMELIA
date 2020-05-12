<p align="center">
  <img src="https://github.com/David-Rod/EMELIA/blob/master/images/blackLogo.png">
</p>

# Event-Driven Machine Learning Intelligent Assessor (EMELIA)

## Quick Start

### Run Program

#### 1. Classify
`python <Filename> --Classify <CSV Alarm Filename> <CSV Ticket Filename> <CSV Test Alarm Filename> <CSV Prediction Filename>`

#### 2. Train
`python <Filename> --Train <CSV Alarm Filename> <CSV Ticket Filename>`

#### 3. Train & Classify (Both)
`python <Filename> --Both <CSV Alarm Filename> <CSV Ticket Filename> <CSV Test Alarm Filename> <CSV Prediction Filename>`

#### 4. Help
`python <Filename> --Help`

**Note:**

Files containing alarm data and ticket data are required. Please acquire these files from General Dynamics personnel prior to attempting to run this program. 

## Overview
The development of this product was inspired by the U.S Coast Guard and General Dynamics
partnership program, Rescue 21. Together these two parties have created an advanced command,
control, and direction finding communication system. The motivation behind Rescue 21 was to
use state-of-the-market technology to execute search and rescue (SAR) missions such as locating
mariners in distress and saving live with a higher level of efficiency.
General Dynamics has implemented a large scale communication infrastructure throughout the
continental United States to allow Rescue 21 to operate along all major waterways such as the
Atlantic, Pacific, Great Lakes and other U.S territories. With this large infrastructure must come
the ability to reliably maintain it. General Dynamics current communications system used by
Rescue 21 relies on a ticket system to generate reports regarding system or hardware failures.
These tickets contain data regarding:

- Code identifier for the error
- Length of time for which the error was present
- Location for where the error occurred
- How the error was received
- Description of the error
- Description of what was impacted by the system error
- Information regarding the resolution for reported error
- The component impacted by the system failure


Each error is classified according to the error type to assist system engineers in preventing future
failures and restoring current ones.

The development of EMELIA was motivated by the current process of classification of tickets in
their failure reporting, analysis, and corrective action system(FRACAS). In this system, System
Engineers manually parse through the tickets and classify it in multiple categories.

Specifically, the manual classification of a single ticket can be a time consuming process that
requires two engineers to complete. A ticket takes approximately ten minutes to classify fully by
a single engineer and must be agreed on by both. This presents the problem of added time when
there are discrepancies between engineers.

Our envisioned solution is an Event-driven MachinE Learning Intelligence Accessor (EMELIA).
EMELIA will automate the categorization of failure reports with machine learning in order to
minimize time and resources significantly while still classifying at a high rate of accuracy. These
tickets are rarely unique and most have common characteristics engineers use to categorize. This
makes the data ideal to be trained and predicted with a Neural Network model. Similarly, this
model reduces classification time from twenty minutes at best to fractions of a second at worse
per ticket.

## Architecture

### Key Module Features

Understanding EMELIA requires a basic understanding of the key responsibilities and features
of each module. The system is composed of four major components: Data Processing, Model
Training, Prediction Model, and Prediction Metrics. The combination of all these components
produces an accurate predicting system for General Dynamics Error Reporting Ticketing system.
Each module plays an important role in that process.

The data processing module essentially formats the chosen tickets and the relative information in
such a way for the Neural Network Prediction Model to compute. However, the data formatting
will vary slightly for input for the prediction model and training the model. The Prediction
Model will take the formatted data and use machine learning to predict the corresponding
classifications for the data. The Metrics Analysis Model will take the output from the Neural
Network and consolidate it in a readable fashion, producing output files and provides metrics on
the system’s performance. The last component, the Training Module, will not be essential to the
process every time the program runs. It will only be used for initially training the Neural
Network and retraining when new features to predicting are introduced.

### Control Flow and Communication

Control of the program will be dictated from a command-line environment. Arguments will be
passed from the terminal to the main driver program. The EMELIA architecture will be
structured in a procedural fashion; Each module’s functionality will be called from the driver and
data will flow through there between modules.

### Architectural Influences

The architectural influences shaping the software are a high percentage of procedural
architecture, as previously mentioned. This is a result of our programming requiring more of a
pipeline of processing structure. However, the Neural Network model will be organized as an
object allowing the user to store, save, and recreate. Overall the system will implement
procedural methods with small object-oriented influences.

### Module and Interface Descriptions

This section will provide detailed descriptions of the modules and interfaces that will be utilized
in creating EMELIA. The interface of this system will only include exporting of data and/or
functionality and importing of data and/or functionality depending on the responsibility of the
module. There will be no graphical interface for this system. All commands will be ran via a
command line. The purpose of this system is to allow each module to access data or functions in
a sequential manner that will make troubleshooting easier for development.

Included with every module is a detailed description of the correlation that the module has with
the other components of the project, interface mockups, and overview of the coding practices
needed to have a successful implementation. Before discussing each module, we have developed
the following system diagram for the entire process that our project will undergo from data
processing to output of the data.

Overview of the Architecture:

<p align="center">
  <img width="750px" height="1000px" src="https://github.com/David-Rod/EMELIA/blob/master/images/Architecture_Design.png">
</p>

---
#### 1. Data Processing

***Component Responsibilities***

This component will be responsible for acquiring all necessary ticket data and alarm data needed
to pass to the neural network layers located in a different module of the system. This module will
configure the data properly using basic coding practices in order for it to be passed to the neural
network. Our system will need to be able to receive input data in the format of a CSV file
representing several “tickets”. We will then retrieve this data by implementing a program to read
in the arguments through the command-line interface.

Since the ticket will be in two csv files this module will have to parse through each “ticket” and
join the two tables of data to make all incident identifiers for tickets and alarm hex codes
available in a single file. These tickets will be similar in structure but may differentiate by the
number of classifications or category values as seen in Figure 3. With that being said, this
module will need to create data structures containing both ticket and alarm data that can be used
within this module along with the other modules. In order for this structure to be accessed in the
future, this module will store OneHotEncoded ticket data in an array. The program will need to
utilize function calls to OneHot encoded ticket data that will serve as input to the learning model.

The purpose of this array will be to store all related data in an ordered fashion, while remaining
accessible to developers. The values in this nested 2-Dimensional array will allow the developers
to OneHot encode its contents, and make comparisons to prediction data in later modules.

***Program Module Relationship***

This module has a direct relationship with other components and advances data to downstream
modules. During this processing component, a master list of data will be created that will be used
for relational mapping in other modules. In order for the training model, which is the next
module in the system, to be accurate the data needs to be configured correctly and thoroughly
examined to prevent loss of training data and reduce bias in the data provided to the neural
network model.

***Program Interface***

This module will interface with the other modules in the system by moving data down the
pipeline. Data will be stored in an array and exported to the next module for use. Since this
module is the root of all functionality for the other modules, it is crucial that we implement this
module so that it organizes data in a way that accurately reflects each ticket. This is to ensure the
data can be used for the training module and be successfully displayed for the output metrics.

#### 2. Learning Model

The neural network model will be used to train on the test data provided by the client. The
learning model will be contained within a single function, inside a module, to be exported for use
by each of the features that will need to be classified for the ticket system.

***Component Responsibilities***

Construction of the learning model is the primary responsibility of this component. The learning
model will be constructed within a single function. Each of the models will be part of a larger
pipeline that feeds data into a learning model.
The number of dense layers will not be dynamically created. Since the learning model will be
“tuned” to create the highest accuracy results, the user(s) will not be able to control the number
of dense layers or specify a different activation function for the model. The activation function
will be a “softmax” function in order to generate confidence value prediction data as an output of
the model.

***Program Module Relationship***

This module will be exported to the model classification module within the system. This module
is only meant to construct the learning model. By modularizing the system in this way, the
learning model can be adjusted by future users and engineers without negative side effects or
need for reconstruction. The implementation for this module provides the highest amount of
integration and the least amount of coupling to the ticket data and the resulting classification of
ticket data.

***Program Interface***

The interface for this module will be easy to implement and use by the design team. Since
Python is the programming language used in this project, the team will need to import the file
containing the learning model and make a single function call to a function containing the
learning model. This design will be most scalable for future development and allows engineers to
import and run the learning model for classification or perform operations in the module without
the learning model.

#### 3. Classification

This model will have the data processing module functionality and functionality from the
learning module imported to perform work on the output. This will include helper functions that
format data and have functions to check the validity of the learning model when training on data
and generating data using test data.

***Component Responsibilities***

This component contains the learning model that will be stored for each feature that will be
classified regarding each ticket. The model will be trained and store the state for each of the
neural network models which are specific for each feature. The state of the learning model will
be saved to a .md5 file or .hd5 file. Each model will be wrapped inside a function and will be
passed ticket feature data via a parameter. By bundling each of the trained neural networks in a
function, these trained networks can be exported to the output module for comparison to the test
data.

***Program Module Relationship***

The module will be responsible for importing the neural network function created in the previous
module. The function that is imported will be used on six separate occasions to train on each
feature of ticket data. The ticket data will be imported from the data processing module as an
array. The array will contain OneHot encoded values that will be used as input for training. Data
processing will be a prerequisite for this step to successfully train on the data that is provided.
This module will be the third step in the pipeline of data. The file will construct and export its
functionality to be used downstream. It simply exports all the functions used to train the neural
network learning models to the next available module.

***Program Interface***

This program will export all functions to be used by the output module. The functions that
contain the trained learning models will be explicitly named so that developers can differentiate
between them in the driver file. The functions from this module are not codependent and may be
used in any order within the driver file.

#### 4. Training

All training on data will take place in this module. Functionality from the classification function
will be used in this module to generate the state files of saved model state for each of the
classifications that require accurate labeling.

***Component Responsibilities***

This component will take a subset of the provided training data and allow the learning model to
train on the input and corresponding output. The subset of training data is randomly generated
and trained upon with the constructed module. This module calls the classification function for
each label and saves the state of the learning model in the .hdf5 file that corresponds to the label.
Next, a set of predictions are made using the remainder of the training data not used for training.
Finally, the validation function is called to determine the accuracy of the system by comparing
the index of the correct label to the index of the confidence value generated by the learning
model. If the positions match, the system correctly trained on that set of data.

***Program Module Relationship***

The functionality in this module will be called in the output module. This will be part of the
control of execution provided in that module. Training is an expensive process. It requires
several minutes of execution for the learning model to successfully train on all the data points
provided on the training data set.

***Program Interface***

All actions in this module are wrapped in a single function that accepts various parameters
provided in the output module. The ‘training’ action must be specified in the output module for
this component to execute.

#### 5. Prediction
This component contains all functionality to generate predictions based on a single input file.
The file is fed into the module, where function calls extract specific fields as input in an attempt
to generate label predictions for each classification column pertaining to a ticket.

***Component Responsibilities***

This component will generate an output CSV file that contains ticket ‘Incident ID’ and
corresponding classification labels. This resulting file contains the ‘Incident ID’ field and the 6
other label columns needed for each ticket. The name of the resulting CSV is specified by the
user as a parameter in the output module. This module is only executed if the user of the program
specifies it as an action.

***Program Module Relationship***

The prediction module is dependent on the parameters passed to the output module. If the action
is specified in the output module, the function for this module will be executed to generate the
expected results. Compared to execution time of the training module, this module is significantly
cheaper to execute. This is due to the fact that the model will be executed frequently on a small
subset of tickets.

***Program Interface***

This module interfaces with both the progress module and the output module. The functionality
from progress is imported to this module. The functionality from this module is exported to the
output module.

#### 6. Progress

This module contains a single function to display execution progress to the user.

***Component Responsibilities***

Render a progress bar to the user while the program executes. This ensures that the user will not
mistake the runtime needed for the learning model to train is not the result of a bug.

***Program Module Relationship***

The functionality in the is module is exported to the prediction and training modules.

***Program Interface***

In both the prediction and training module, a single thread is created from the main process of
execution. This single thread is used to execute the progress bar function, while the core action
of the program is executed. The thread is required so that both functions are executed
concurrently.

#### 7. Output Metrics

***Component Responsibilities***

This module is responsible for accepting user commands via the command line interface. This
module has the ability to process a basic set of commands that control the flow of execution.
Program Module Relationship

This module will import functionality from the prediction and training modules. As the user
passes parameters via the command line, this function will then relay those parameters to the
prediction module, training module, or both depending on the action specified by the user.

***Program Interface***

This module will utilize the functionality from the other modules in the system, and the
command line, to determine which process to execute within the program. The module will
accept a single flag command and up to four file names to complete any action capable of the
system. The files provided can include:

- Input alarm file
- Input ticket file
- Test ticket file
- Name of file that will contain results for the system
 
To understand more about the input for this module, please refer to the ‘Help’ section of the
‘Product_Delivery_User_Manual’ document.
