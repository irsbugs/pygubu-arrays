# Pygubu-arrays

The objective is to demonstrate: 

* Manually adding a label array to a *Pygubu Designer* created tkinter application. 
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
Coding for the individual labels is cumbersome, and is more efficiently performed using an array, or list, of label objects.
```
for i in range(0, len(self.label_list), 2):
    self.label_list[i].config(text="0")
    self.label_list[i+1].config(text="1")
```
The following describes how to use *Pygubu Designer* to create a basic GUI application, then how to manually add a label array to the application.

## Test Application Example

Using *Pygubu Designer* a simple application is created 
![pygubu_designer](/images/pygubu_designer.png)

This application has the following tkinter objects: A Toplevel container, two LabelFrame containers, and three Buttons.

![objects](/images/objects.png)

This application is saved as XML script in the UI file [test.ui](test.ui)

The *Pygubu Designer* then generates the following python code to launch the application. During launching the XML in the `test.ui` file is used to build the GUI

![generated_code](/images/generated_code.png)

On running the python application [testapp_designer_code.py](testapp_designer_code.py) it will be displayed as follows.

![testapp_designer_code](/images/testapp_designer_code.png)

The top Labelframe does not contain any labels. The python *Pygubu Designer* code needs to be manually enhanced to add a label array so the application will look like this:

![label_array_demo](/images/label_array_demo.png)

## Enhancing the Python Code

The original *Pygubu Designer* generated code, [testappp_designer_code.py](testapp_designer_code.py), is enhanced as follows to create the file [testapp_label_array.py](testapp_label_array.py)

* Add class wide variables for the two labelframes.
* Add the ttk.style() library for use in setup of labels.
* Change the text in both labeframes.
* Run a method to setup the label array
* Enhance the button callback method to perfrom updates of the label array.

The python code added / changed is:

### Add class wide variables for the two labelframes.
```
        self.labelframe_0 = builder.get_object("labelframe1", master)
        self.labelframe_1 = builder.get_object("labelframe2", master)
```

### Add the ttk.style() library for use in setup of labels.
```
        self.style = ttk.Style()
```

###  Change the text in both labeframes.
Normally these text changes would be done in *Pygubu Designer* mode. They are done using `.config(text="")` just for demonstration purposes: 
```
        #  See what text the top label frame has from Design mode.
        print(self.labelframe_0.cget("text"))
        #  See if the text of the top label frame can be changed to something else
        self.labelframe_0.config(text="Register bits")
        print(self.labelframe_0.cget("text"))

        # Set text on bottom label frame.
        self.labelframe_1.config(text="Select Register Contents")
```

### Run a method to setup the label array
The following method is added to setup the label array in `self.labelframe_0`. This method is called at the end of the `def __init__(self, master=None):` with the code `self.setup_register_bits()`

```
    def setup_register_bits(self):
        """
        Create an array of labels in the Register Bits Labelframe, self.labelframe_0.
        Fill labels with spaces.
        """
        self.style.configure("Bits.TLabel", borderwidth=1, font=('Helvetica', 11),
                                relief="solid", width = 2, anchor="center")
        self.label_list = []
        for i in range(16):
            self.label_list.append(ttk.Label(self.labelframe_0, text=str(" "),
                                    style="Bits.TLabel",))
            self.label_list[i].grid(row=0, column=i,)
```
###  Enhance the button callback method to perfrom updates of the label array.
*Pygubu Designer* provides a callback template method, based on how it was setup for the three buttons. The callback also passes each buttons id as a string, so which button has been clicked on can be easily determined. The code below shows the advantages of using a label array, `self.label_list[]`, and the little code that is required to fill the label array with data.

```
    def button_cb(self, widget_id):  # <-- Method heading provided by pygubu designer
        #pass
        """
        Manually added...
        Callback for buttons was set in pygubu design mode with Type:"Set Widgit ID".
        Set all register bits to either zeros or ones or a mix of zero and ones.
        Simple loop to update label_list. More complex to update if this was a
        series of individual label objects.
        """
        #print(widget_id)  #  button1, or button2, etc...

        #  zeros
        if  widget_id == "button1":
            for i in range(len(self.label_list)):
                self.label_list[i].config(text = "0")
        #  ones
        if widget_id == "button2":
            for i in range(len(self.label_list)):
                self.label_list[i].config(text = "1")

        #  mix of ones and zeros
        if widget_id == "button3":
            for i in range(0, len(self.label_list), 2):
                self.label_list[i].config(text = "0")
                self.label_list[i+1].config(text = "1")
```

For an alternative to what button3 does, then change `if widget_id == "button3":` to `if widget_id == "buttonx":`, and change  `if widget_id == "buttonx":` to: `if widget_id == "button3":`. On clicking the *Mix* button a randomly generated 16-bit binary number will then be placed into the label array. The following is the alternative button3 code:

```
        if widget_id == "buttonx":
            """
            Alternative for button3.
            Manually edit 'if widget_id == "button3":' to "buttonx" and vica versa
            Fill label array with a random number between 0 and 65535 / hex FFFF
            """
            import random
            dec_integer = random.randint(0, 65535)
            print(dec_integer)
            bin_integer_list = list(bin(dec_integer)[2:].zfill(16))
            for i in range(0, len(self.label_list)):
                self.label_list[i].config(text = bin_integer_list[i])
```
## Running the demonstration:

On a computer ensure the following are installed:
* A recent version of python3
* Tkinter
* Pygubu
* Pybugu-Designer

Download from this repository the following files:
* test.ui
* testapp_designer_code.py
* testapp_label_array.py

Run the two programs, and try clicking on the buttons:
* $ python3 testapp_designer_code.py
* $ python3 testapp_label_array.py

## Note:
The code in this repository was developed and tested on:
* Ubuntu Mate 22.04
* Python 3.10.12
* tkinter 8.6.12, tkinter.ttk.__version__ 0.3.1'
* pygubu 0.31 
* pygubu-designer 0.36 










