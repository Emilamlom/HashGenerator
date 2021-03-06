from tkinter import *
from tkinter import messagebox
from hashes import *

class GUI:
    def __init__(self, window):
        """
        Initializes the GUI
        """
        self.window = window
        
        self.options = ['md5', 'sha256', 'sha512']
        self.opt = StringVar(self.window)
        self.opt.set(self.options[0])

        self.input_frame = Frame(self.window)
        self.input_frame.grid(column=0, row=0, columnspan=3)
        self.wordlist1_label = Label(self.input_frame, text='1st Wordlist:', padx=5, pady=5).grid(column=0, row=0)
        self.wordlist1_entry = Entry(self.input_frame, width=30)
        self.wordlist2_label = Label(self.input_frame, text='2nd Wordlist:', padx=5, pady=5).grid(column=0, row=1)
        self.wordlist2_entry = Entry(self.input_frame, width=30)
        self.suffix_label = Label(self.input_frame, text='Suffix (optional):', padx=5, pady=5).grid(column=0, row=2)
        self.suffix_entry = Entry(self.input_frame, width=30)
        self.algo_label = Label(self.input_frame, text='Select Hash Algorithm:', padx=5, pady=5).grid(column=0, row=3)
        self.algo_entry = OptionMenu(self.input_frame, self.opt, *self.options)
        self.wordlist1_entry.grid(column=1, row=0)
        self.wordlist2_entry.grid(column=1, row=1)
        self.suffix_entry.grid(column=1, row=2)
        self.algo_entry.grid(column=1, row=3)

        self.button_frame = Frame(self.window)
        self.button_frame.grid(column=0, row=1, columnspan=3)
        self.button_test = Button(self.button_frame, text='Test', command=self.testbutton, padx=5, pady=5, width=10).grid(column=0, row=0)
        self.button_compute = Button(self.button_frame, text='Compute', command=self.computebutton, padx=5, pady=5, width=10).grid(column=1, row=0)
        self.button_help = Button(self.button_frame, text='Help', command=self.helpbutton, padx=5, pady=5, width=10).grid(column=2, row=0)

        self.result_frame = Frame(self.window)
        self.result_frame.grid(column=0, row=2, columnspan=3)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.rowconfigure(1, weight=1)

    def helpbutton(self) -> None:
        """
        Displays messagebox with help information.
        """
        messagebox.showinfo('Explanation',
                            "Wordlists and suffix are combined and hashed with the selected algorithm.\n\n"
                            "Wordlist1 and Wordlist2: input the filepath of a wordlist.\n"
                            "Wordlists should be in 'wordlists' directory for easiest access.\n"
                            "Wordlists should be text files with each word separated by linebreaks.\n"
                            "Suffix is for adding an optional suffix to each wordlist combo.\n")
        
    def testbutton(self) -> None:
        """
        Runs a single instance of the hash function to check output and handles display of results
        """
        #Remove results from previous run to avoid weird overlapping of labels
        if hasattr(self, 'label_result'):
            self.label_result.config(text='')

        result = Hashes.hashtest(self.wordlist1_entry.get(), self.wordlist2_entry.get(), self.opt.get(), self.suffix_entry.get())

        self.label_result = Label(self.result_frame, text=result, padx=5, pady=5)
        self.label_result.grid(column=0, row=0)
        
    def computebutton(self) -> None:
        """
        Runs the hashbatch function and handles display of results.
        """
        #Remove results from previous run to avoid weird overlapping of labels
        if hasattr(self, 'label_result'):
            self.label_result.config(text='')

        result = Hashes.hashbatch(self.wordlist1_entry.get(), self.wordlist2_entry.get(), self.opt.get(), self.suffix_entry.get())
        self.wordlist1_entry.delete(0, 'end')
        self.wordlist2_entry.delete(0, 'end')
        self.suffix_entry.delete(0, 'end')
        self.opt.set(self.options[0])

        self.label_result = Label(self.result_frame, text=result, padx=5, pady=5)
        self.label_result.grid(column=0, row=0)