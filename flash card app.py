from tkinter import *
from random import choice


class vocabulary:
    def __init__(self):
        self.vocab = {}
        self.read_vocab()

    # randomly selects words(keys) from the vocab_dict
    def flash_card_gen(self):
        word = []
        for words in self.vocab.keys():
            word.append(words)
        gen_word = choice(word)
        return gen_word
    # displays the randomly genrated word

    def click_start_next(self):
        word_gen = self.flash_card_gen()
        disp_word.delete(0, END)
        disp_def.delete(0, END)
        disp_word.insert(0, word_gen)

    # displays the meanng of the randomly generated word
    def click_reveal(self):
        vocab = self.vocab
        try:
            current_word = disp_word.get()
            current_def = vocab[current_word]
            disp_def.delete(0, END)
            disp_def.insert(0, current_def)
        except:
            disp_def.delete(0, END)
            disp_def.insert(
                0, "ERROR!!!! Please, don't alter the word in the entry box.")

    # stores vocab data from file to dictionary within the class
    def read_vocab(self):
        myfile = open("vocablist.txt", "r")
        for line in myfile:
            (key, value) = line.split("=")
            self.vocab[key.strip()] = value.strip()
        myfile.close()

    # saves the entered vocab data in the file
    def save_vocab(self):
        get_word = save_word.get()
        get_def = save_def.get()
        str_entry = get_word+"="+get_def
        myfile = open("vocablist.txt", "a")
        myfile.write("\n")
        myfile.write(str_entry)
        myfile.close()
        save_word.delete(0, END)
        save_def.delete(0, END)


# UI and application loop
my_vocab = vocabulary()
window = Tk()
window.title("GRE vocab flash card")

frame1 = Frame(window)
frame1.grid(row=0, column=0)
Label(frame1, text="My Flash Card", anchor=CENTER).grid(row=0, column=0)
disp_word = Entry(frame1, width=90, bg="light green")
disp_word.grid(row=1, column=0, rowspan=2)
Label(frame1, text="Meaning", anchor=CENTER).grid(row=3, column=0)
disp_def = Entry(frame1, width=90, bg="light green")
disp_def.grid(row=4, column=0, rowspan=2)

frame2 = Frame(window)
frame2.grid(row=1, column=0)
Button(frame2, text="Start/Next", width=30, command=my_vocab.click_start_next,
       bg="cyan").grid(row=6, column=0, sticky=W)
Button(frame2, text="Reveal", width=30, command=my_vocab.click_reveal,
       bg="cyan").grid(row=6, column=2, sticky=E)

frame3 = Frame(window)
frame3.grid(row=2, column=0)
Label(frame3, text=" Vocab saver").grid(row=0, column=0)
Label(frame3, text="Enter the word to add in the vocab list").grid(row=1, column=0)
save_word = Entry(frame3, width=90, bg="light blue")
save_word.grid(row=2, column=0)
Label(frame3, text="Enter the meaning of the word \n example format: /adj/: text").grid(row=3, column=0, rowspan=2)
save_def = Entry(frame3, width=90, bg="light blue")
save_def.grid(row=5, column=0)
Button(frame3, text="Save", width=30, anchor=CENTER,
       command=my_vocab.save_vocab, bg="cyan").grid(row=6, column=0)
Label(frame3).grid(row=7, column=0)

window.mainloop()
