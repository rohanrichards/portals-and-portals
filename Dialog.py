from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os

class Dialog(Toplevel):

    def __init__(self, parent, title = None, data = None):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)

        if data:
            self.initial_focus = self.body(body, data)
        else:
            self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        if data:
            self.buttonbox(data)
        else:
            self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master, data = None):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self, data = None):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override

class SetPlayersDialog(Dialog):

    def buttonbox(self, data = None):
        box = Frame(self)

        def set(num):
            self.result = num
            self.ok()

        w = Button(box, text="1", width=10, command=lambda : set(1))
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="2", width=10, command=lambda : set(2))
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="3", width=10, command=lambda : set(3))
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="4", width=10, command=lambda : set(4))
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=BOTTOM, padx=5, pady=5)

        self.bind("<Escape>", self.cancel)

        box.pack()

    def apply(self):
        pass
    # def setPlayerCount(self):

class SelectTokensDialog(Dialog):
    def body(self, master, data = None):

        Label(master, text="Set your name:").grid(row=0)

        self.e1 = Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def buttonbox(self, data = None):
        box = Frame(self)

        # images = []
        # for imagePath in data["images"]:
        #     image = PhotoImage(file=imagePath)
        #     images.append(image)

        def set(num, token):
            self.result = num, token
            self.ok()

        for index, token in enumerate(data['tokens']):
            if token not in data['selectedTokens']:
                image = PhotoImage(file=data["images"][index])
                b = ttk.Button(box, image=image, command=lambda index=index, token=token: set(index, token))
                b.image = image
                b.pack(side=LEFT)

        box.pack()

    def validate(self):
        first= self.e1.get()
        if first.strip():
            return 1
        else:
            messagebox.showwarning(
                "Bad input",
                "Please enter a name"
            )
            return 0

    def apply(self):
        name = self.e1.get()
        token = self.result[0]
        tokenData = self.result[1]
        returnData = name, token, tokenData
        self.result = returnData
        # print first, second # or something