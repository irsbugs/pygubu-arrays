# Pygubu-arrays

* Manually add a label array to a Pygubu Designer created tkinter application. 
* Create class-wide instance variables for tkinter widgets.

## Pygubu and Pygubu-Designer 

* [Pygubu](https://pypi.org/project/pygubu/) - A simple GUI builder that loads and builds user interfaces defined in XML, for the python tkinter module.

* [Pygubu-designer](https://pypi.org/project/pygubu-designer/) - A simple GUI designer for the python tkinter module, that helps you create the xml definition graphically.

## Issue

The *Pygubu Designer* will allow a container to have individual labels. It does not support creation of an array of labels within a container.

For example, you may wish to have a tkinter Labelframe container to have 16 Labels to represent individual binary bits in a 16 bit register 
![16bit_register](/images/16bit_register.png)

The *Pygubu Designer* allows the creation of 16 Labels, but setting the text in the labels would require python code like this
```
self.label_0.config(text="0")
self.label_1.config(text="1")
self.label_2.config(text="0")
...
self.label_14.config(text="0")
self.label_15.config(text="1")
```
Coding for the individual labels is cumbersome, and is more efficiently performed using an array or list of label objects.
```
for i in range(0, len(self.label_list), 2):
    self.label_list[i].config(text="0")
for i in range(1, len(self.label_list), 2):
    self.label_list[i].config(text="1")
```
The following describes how to use Pygubu Designer to create a basic GUI application, then how to manually add a label array to the application.

##Test Application Example

Using *Pygubu Designer* a simple application is created 
![pygubu_designer](/images/pygubu_designer.png)

This application has the following tkinter objects: A Toplevel container, two LabelFrame containers, and three Buttons.

![objects](/images/objects.png)

This application is saved as XML script in the UI file [test.ui](test.ui)

The *Pygubu Designer* then generates the following python code to launch the application. During launching the XML in the test.ui file is used to build the GUI

![generated_code](generated_code.png)










