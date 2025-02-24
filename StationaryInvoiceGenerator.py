from tkinter import *
from tkinter import messagebox
import random, os, tempfile





def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        else:
            messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do You Want To Save The Bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'bill number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Requried')
    elif StationaryItemsPriceEntry.get() == '' or StationaryMaterialPriceEntry.get() == '' or OfficeMaterialsPriceEntry.get() == ' ':
        messagebox.showerror('Error', 'No Items Are Selected')
    elif StationaryItemsPriceEntry.get() == '0 Rs' and StationaryMaterialPriceEntry.get() == '0 Rs' and OfficeMaterialsPriceEntry.get() == ' 0 Rs':
        messagebox.showerror('Error', 'No Items Are Selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**Welcome Coustomer**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}')
        textarea.insert(END, f'\nCustomer Phone Number:{phoneEntry.get()}')
        textarea.insert(END, '\n=======================================================')
        textarea.insert(END, 'Items\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if PenEntry.get() != '0':
            textarea.insert(END, f'\nPen\t\t\t {PenEntry.get()}\t\t\t{Penprice}Rs')
        if PencilEntry.get() != '0':
            textarea.insert(END, f'\nPencil\t\t\t {PencilEntry.get()}\t\t\t{Pencilprice}Rs')
        if ErasorEntry.get() != '0':
            textarea.insert(END, f'\nErasor\t\t\t {ErasorEntry.get()}\t\t\t{Erasorprice}Rs')
        if ScaleEntry.get() != '0':
            textarea.insert(END, f'\nScale\t\t\t {ScaleEntry.get()}\t\t\t{Scaleprice}Rs')
        if SharperEntry.get() != '0':
            textarea.insert(END, f'\nSharper\t\t\t {SharperEntry.get()}\t\t\t{Sharperprice}Rs')
        if CompassEntry.get() != '0':
            textarea.insert(END, f'\nCompass\t\t\t {CompassEntry.get()}\t\t\t{Compassprice}Rs')

        if NotebookEntry.get() != '0':
            textarea.insert(END, f'\nNotebook\t\t\t {NotebookEntry.get()}\t\t\t{Notebookprice}Rs')
        if GraphbookEntry.get() != '0':
            textarea.insert(END, f'\nGraphbook\t\t\t {GraphbookEntry.get()}\t\t\t{Graphbookprice}Rs')
        if HighlighterEntry.get() != '0':
            textarea.insert(END, f'\nHighlighter\t\t\t {HighlighterEntry.get()}\t\t\t{Highlighterprice}Rs')
        if SketchbookEntry.get() != '0':
            textarea.insert(END, f'\nSketchbook\t\t\t {SketchbookEntry.get()}\t\t\t{Sketchbookprice}Rs')
        if CraftpagesEntry.get() != '0':
            textarea.insert(END, f'\nCraftpages\t\t\t {CraftpagesEntry.get()}\t\t\t{Craftpagesprice}Rs')
        if SketchpenEntry.get() != '0':
            textarea.insert(END, f'\nSketchpen\t\t\t {SketchpenEntry.get()}\t\t\t{Sketchpenprice}Rs')

        if FileEntry.get() != '0':
            textarea.insert(END, f'\nFile\t\t\t {FileEntry.get()}\t\t\t{Fileprice}Rs')
        if FolderEntry.get() != '0':
            textarea.insert(END, f'\nFolder\t\t\t {FolderEntry.get()}\t\t\t{Folderprice}Rs')
        if XeroxpagesEntry.get() != '0':
                        textarea.insert(END, f'\nXeroxpages\t\t\t {XeroxpagesEntry.get()}\t\t\t{Xeroxpagesprice}Rs')
        if SteplerEntry.get() != '0':
            textarea.insert(END, f'\nStepler\t\t\t {SteplerEntry.get()}\t\t\t{Steplerprice}Rs')
        if PunchingMachEntry.get() != '0':
            textarea.insert(END, f'\nPunchingMach\t\t\t {PunchingMachEntry.get()}\t\t\t{PunchingMachprice}Rs')
        if WhitenerEntry.get() != '0':
            textarea.insert(END, f'\nWhitener\t\t\t {WhitenerEntry.get()}\t\t\t{Whitenerprice}Rs')
        textarea.insert(END, '\n-------------------------------------------------------')

       
        textarea.insert(END, f'\nTotal Bill\t\t\t\t{totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')
        save_bill()


def total():
    global Penprice, Pencilprice, Erasorprice, Scaleprice, Sharperprice, Compassprice
    global Notebookprice, Graphbookprice, Highlighterprice, Sketchbookprice, Craftpagesprice, Sketchpenprice
    global Fileprice, Xeroxpagesprice, Folderprice, Steplerprice, PunchingMachprice, Whitenerprice
    global totalbill

    Penprice = int(PenEntry.get()) * 7
    Pencilprice = int(PencilEntry.get()) * 5
    Erasorprice = int(ErasorEntry.get()) * 5
    Scaleprice = int(ScaleEntry.get()) * 5
    Sharperprice = int(SharperEntry.get()) * 5
    Compassprice = int(CompassEntry.get()) * 25

    totalStationaryItemsprice = Penprice + Pencilprice + Erasorprice + Scaleprice + Sharperprice + Compassprice
    StationaryItemsPriceEntry.delete(0, END)
    StationaryItemsPriceEntry.insert(0, str(totalStationaryItemsprice) + 'Rs')

    Notebookprice = int(NotebookEntry.get()) * 55
    Graphbookprice = int(GraphbookEntry.get()) * 30
    Highlighterprice = int(HighlighterEntry.get()) * 25
    Sketchbookprice = int(SketchbookEntry.get()) * 35
    Craftpagesprice = int(CraftpagesEntry.get()) * 15
    Sketchpenprice = int(SketchpenEntry.get()) * 20

    totalStationaryMaterialprice = Notebookprice + Graphbookprice + Highlighterprice +Sketchbookprice + Craftpagesprice + Sketchpenprice
    StationaryMaterialPriceEntry.delete(0, END)
    StationaryMaterialPriceEntry.insert(0, str(totalStationaryMaterialprice) + 'Rs')

    Fileprice = int(FileEntry.get()) * 10
    Folderprice = int(FolderEntry.get()) * 30
    Xeroxpagesprice = int(XeroxpagesEntry.get()) * 260
    Steplerprice = int(SteplerEntry.get()) * 40
    PunchingMachprice = int(PunchingMachEntry.get()) * 100
    Whitenerprice = int(WhitenerEntry.get()) * 25

    totalOfficeMaterialsprice = Fileprice + Folderprice + Folderprice + Steplerprice + PunchingMachprice + Whitenerprice
    OfficeMaterialsPriceEntry.delete(0, END)
    OfficeMaterialsPriceEntry.insert(0, str(totalOfficeMaterialsprice) + 'Rs')
    totalbill = totalStationaryItemsprice + totalStationaryMaterialprice + totalOfficeMaterialsprice 


root = Tk()
root.title("Stationary Invoice Generator")
root.geometry("1350x800")
headingLabel = Label(root, text="Stationary Invoice Generator", font=('Monotype Corsiva', 40, 'bold'), bg='light blue',
                     fg='black', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text="Customer Details", font=('times new roman', 15, 'bold'), fg='black',
                                    bd=8, relief=GROOVE, bg='light blue')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='light blue',
                  fg='black')
nameLabel.grid(row=0, column=0, padx=10)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=15)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='light blue',
                   fg='black')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=10)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'),
                        bg='light blue', fg='black')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)
billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=5)
billnumberEntry.grid(row=0, column=5, padx=8)

serachButton = Button(customer_details_frame, text="SEARCH", font=('arial', 12, 'bold'), bd=7, width=10,
                      command=search_bill)
serachButton.grid(row=0, column=8, padx=10, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

StationaryItemsFrame = LabelFrame(productsFrame, text='Stationary Items', font=('times new roman', 15, 'bold'), fg='black', bd=8,
                         relief=GROOVE, bg='light blue')
StationaryItemsFrame.grid(row=0, column=0)

PenLabel = Label(StationaryItemsFrame, text='Pen_7Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                        fg='black')
PenLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
PenEntry = Entry(StationaryItemsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
PenEntry.grid(row=0, column=1, pady=9, padx=10)
PenEntry.insert(0, 0)

PencilLabel = Label(StationaryItemsFrame, text='Pencil_5Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                     fg='black')
PencilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
PencilEntry = Entry(StationaryItemsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
PencilEntry.grid(row=1, column=1, pady=9, padx=10)
PencilEntry.insert(0, 0)

ErasorLabel = Label(StationaryItemsFrame, text='Erasor_5Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                       fg='black')
ErasorLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
ErasorEntry = Entry(StationaryItemsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
ErasorEntry.grid(row=2, column=1, pady=9, padx=10)
ErasorEntry.insert(0, 0)

ScaleLabel = Label(StationaryItemsFrame, text='Scale_5Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                        fg='black')
ScaleLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
ScaleEntry = Entry(StationaryItemsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
ScaleEntry.grid(row=3, column=1, pady=9, padx=10)
ScaleEntry.insert(0, 0)

SharperLabel = Label(StationaryItemsFrame, text='Sharper_5Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                      fg='black')
SharperLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
SharperEntry = Entry(StationaryItemsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
SharperEntry.grid(row=4, column=1, pady=9, padx=10)
SharperEntry.insert(0, 0)

CompassLabel = Label(StationaryItemsFrame, text='Compass_25Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                          fg='black')
CompassLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
CompassEntry = Entry(StationaryItemsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
CompassEntry.grid(row=5, column=1, pady=9, padx=10)
CompassEntry.insert(0, 0)

StationaryMaterialFrame = LabelFrame(productsFrame, text='Stationary Material', font=('times new roman', 15, 'bold'), fg='black', bd=8,
                         relief=GROOVE, bg='light blue')
StationaryMaterialFrame.grid(row=0, column=1)

NotebookLabel = Label(StationaryMaterialFrame, text='Notebook _55Rs', font=('times new roman', 15, 'bold'), bg='light blue', fg='black')
NotebookLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
NotebookEntry = Entry(StationaryMaterialFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
NotebookEntry.grid(row=0, column=1, pady=9, padx=10)
NotebookEntry.insert(0, 0)

GraphbookLabel = Label(StationaryMaterialFrame, text='Graphbook_30Rs', font=('times new roman', 15, 'bold'), bg='light blue', fg='black')
GraphbookLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
GraphbookEntry = Entry(StationaryMaterialFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
GraphbookEntry.grid(row=1, column=1, pady=9, padx=10)
GraphbookEntry.insert(0, 0)

HighlighterLabel = Label(StationaryMaterialFrame, text='Highlighter_25Rs', font=('times new roman', 15, 'bold'), bg='light blue', fg='black')
HighlighterLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
HighlighterEntry = Entry(StationaryMaterialFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
HighlighterEntry.grid(row=2, column=1, pady=9, padx=10)
HighlighterEntry.insert(0, 0)

SketchbookLabel = Label(StationaryMaterialFrame, text='Sketchbook_35Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                      fg='black')
SketchbookLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
SketchbookEntry = Entry(StationaryMaterialFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
SketchbookEntry.grid(row=3, column=1, pady=9, padx=10)
SketchbookEntry.insert(0, 0)

CraftpagesLabel = Label(StationaryMaterialFrame, text='Craftpages_15Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                     fg='black')
CraftpagesLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
CraftpagesEntry = Entry(StationaryMaterialFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
CraftpagesEntry.grid(row=4, column=1, pady=9, padx=10)
CraftpagesEntry.insert(0, 0)

SketchpenLabel = Label(StationaryMaterialFrame, text='Sketchpen_20Rs', font=('times new roman', 15, 'bold'), bg='light blue', fg='black')
SketchpenLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
SketchpenEntry = Entry(StationaryMaterialFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
SketchpenEntry.grid(row=5, column=1, pady=9, padx=10)
SketchpenEntry.insert(0, 0)

OfficeMaterialsFrame = LabelFrame(productsFrame, text='Office Materials', font=('times new roman', 15, 'bold'), fg='black', bd=8,
                           relief=GROOVE, bg='light blue')
OfficeMaterialsFrame.grid(row=0, column=2)

FileLabel = Label(OfficeMaterialsFrame, text='File_10Rs', font=('times new roman', 15, 'bold'), bg='light blue', fg='black')
FileLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
FileEntry = Entry(OfficeMaterialsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
FileEntry.grid(row=0, column=1, pady=9, padx=10)
FileEntry.insert(0, 0)

FolderLabel = Label(OfficeMaterialsFrame, text='Folder_30Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                     fg='black')
FolderLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
FolderEntry = Entry(OfficeMaterialsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
FolderEntry.grid(row=1, column=1, pady=9, padx=10)
FolderEntry.insert(0, 0)

XeroxpagesLabel = Label(OfficeMaterialsFrame, text='Xeroxpages_260Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                    fg='black')
XeroxpagesLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
XeroxpagesEntry = Entry(OfficeMaterialsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
XeroxpagesEntry.grid(row=2, column=1, pady=9, padx=10)
XeroxpagesEntry.insert(0, 0)

SteplerLabel = Label(OfficeMaterialsFrame, text='Stepler_40Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                    fg='black')
SteplerLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
SteplerEntry = Entry(OfficeMaterialsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
SteplerEntry.grid(row=3, column=1, pady=9, padx=10)
SteplerEntry.insert(0, 0)

PunchingMachLabel = Label(OfficeMaterialsFrame, text='PunchingMach_100Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                     fg='black')
PunchingMachLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
PunchingMachEntry = Entry(OfficeMaterialsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
PunchingMachEntry.grid(row=4, column=1, pady=9)
PunchingMachEntry.insert(0, 0)

WhitenerLabel = Label(OfficeMaterialsFrame, text='Whitener_25Rs', font=('times new roman', 15, 'bold'), bg='light blue',
                      fg='black')
WhitenerLabel.grid(row=5, column=0, pady=9, sticky='w')
WhitenerEntry = Entry(OfficeMaterialsFrame, font=('times new roman', 12, 'bold'), width=7, bd=5)
WhitenerEntry.grid(row=5, column=1, pady=9)
WhitenerEntry.insert(0, 0)

billframe = Frame(productsFrame)
billframe.grid(row=0, column=3, padx=8)

billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 13, 'bold'), fg='black', bd=8,
                           relief=GROOVE, bg='light blue')
billmenuFrame.pack(fill=X)

StationaryItemsPriceLabel = Label(billmenuFrame, text='StationaryItems Price', font=('times new roman', 13, 'bold'), bg='light blue',
                         fg='black')
StationaryItemsPriceLabel.grid(row=0, column=0, pady=5, padx=10, sticky='w')
StationaryItemsPriceEntry = Entry(billmenuFrame, font=('times new roman', 12, 'bold'), width=12, bd=5)
StationaryItemsPriceEntry.grid(row=0, column=1, pady=5, padx=10)

StationaryMaterialPriceLabel = Label(billmenuFrame, text='StationaryMaterial price', font=('times new roman', 13, 'bold'), bg='light blue',
                         fg='black')
StationaryMaterialPriceLabel.grid(row=1, column=0, pady=5, padx=10, sticky='w')
StationaryMaterialPriceEntry = Entry(billmenuFrame, font=('times new roman', 12, 'bold'), width=12, bd=5)
StationaryMaterialPriceEntry.grid(row=1, column=1, pady=5, padx=10)

OfficeMaterialsPriceLabel = Label(billmenuFrame, text='Office Materials price', font=('times new roman', 13, 'bold'), bg='light blue',
                          fg='black')
OfficeMaterialsPriceLabel.grid(row=2, column=0, pady=5, padx=10, sticky='w')
OfficeMaterialsPriceEntry = Entry(billmenuFrame, font=('times new roman', 12, 'bold'), width=12, bd=5)
OfficeMaterialsPriceEntry.grid(row=2, column=1, pady=5, padx=10)


buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='light blue', fg='black', bd=5,
                     width=10, pady=8, command=total)
totalButton.grid(row=0, column=0, pady=15, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='light blue', fg='black', bd=5, width=10,
                    pady=8, command=bill_area)
billButton.grid(row=0, column=1, pady=15, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='light blue', fg='black', bd=5,
                     width=10, pady=8, command=print_bill)
printButton.grid(row=0, column=3, pady=15, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='light blue', fg='black', bd=5, width=9,
                     pady=8)
clearButton.grid(row=0, column=4, pady=15, padx=5)

root.mainloop()




