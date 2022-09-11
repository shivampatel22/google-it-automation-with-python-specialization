import wordcloud
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import os
from tkinter import *
from tkinter import filedialog

USERNAME = os.environ['USERNAME']

class Wordcloud():
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = [
        "", "the", "a", "to", "if", "is", "it", "it's", "It's", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", 
        "out", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them","their", "what", "which", "who",
        "than", "in", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", 
        "did", "but", "at", "by", "with", "from", "here", "when", "where", "how","all", "any", "both", "each", "few", "more", "much",
        "some", "such", "no", "nor", "too", "very", "can", "will", "just"
    ]
    
    def __init__(self):
        self.file_contents = None
        self.count_dict = {}
        self.cloud = None

    # This is the uploader widget to be used with jupiter notebook
    def upload(self):
        """
        a upload widget specificaly to be used with jupiter notebook 
        """
        _upload_widget = fileupload.FileUploadWidget()

        def _cb(change):
            global file_contents
            decoded = io.StringIO(change['owner'].data.decode('utf-8'))
            filename = change['owner'].filename
            print('Uploaded `{}` ({:.2f} kB)'.format(
                filename, len(decoded.read()) / 2 **10))
            file_contents = decoded.getvalue()

        _upload_widget.observe(_cb, names='data')
        display(_upload_widget)

    def open_file(self):
        # set configurations
        root = Tk()
        root.title("Wordcloud")
        root.geometry("500x450")

        def open_txt():
        # open and read file
            file = filedialog.askopenfilename(initialdir='C:/Users/'+USERNAME+'/Desktop/',
                                              title="Open Text file",
                                              filetypes=(("Text Files", "*.txt"),))
            file = open(file, 'r')
            self.file_contents = file.read()
            my_text.insert(END, self.file_contents)
            file.close()

        # create text box
        my_text = Text(root, 
                       width=40, 
                       height=10, 
                       font=("Haveltica", 16))
        my_text.pack(pady=20)
        # create a button
        open_button = Button(root,
                             text='Open text file',
                             command=open_txt)
        open_button.pack(pady=20) 
        root.mainloop()


    def calculate_frequencies(self):
        # Here is a list of punctuations and uninteresting words you can use to process your text
        list_of_words = list(self.file_contents.split())
        for word in list_of_words:
            word = word.lower()
            if word not in Wordcloud.uninteresting_words:
                for letter in word:
                    if letter in Wordcloud.punctuations:
                        word = word.translate({ord(letter):None})
                if word not in self.count_dict.keys():
                    self.count_dict[word] = 1
                else:
                    self.count_dict[word] += 1 
        for key in self.count_dict.keys():
            if key in Wordcloud.uninteresting_words:
                self.count_dict[key] = 0

    # wordcloud
    def gen_wordcloud(self):
        c = wordcloud.WordCloud()
        c.generate_from_frequencies(self.count_dict)
        self.cloud = c.to_array()

    # Display your wordcloud image
    def display_wordcloud(self):
        #myimage = self.calculate_frequencies()
        plt.imshow(self.cloud, interpolation = 'nearest')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    # create wordcloud object
    wc = Wordcloud()
    # open txt file to read
    wc.open_file()
    # calculate frequency of meaningfull words
    wc.calculate_frequencies()
    # generate wordcloud
    wc.gen_wordcloud()
    # display wordcloud
    wc.display_wordcloud()