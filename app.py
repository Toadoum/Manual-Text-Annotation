import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
#import docx2txt
#from PIL import Image 
#from PyPDF2 import PdfFileReader
#import pdfplumber


def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text

def read_pdf2(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        return page.extract_text()


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 



def main():
	st.title("Manual Data Annotation")

	menu = ["Dataset","About"]
	choice = st.sidebar.selectbox("Menu",menu)



	if choice == "Dataset":
		st.subheader("Dataset")
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if st.button("Process"):
			if data_file is not None:
				file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
				st.write(file_details)

				df = pd.read_csv(data_file)
				st.dataframe(df)
	else:
		st.subheader("About")
		st.info("Built with Streamlit")



if __name__ == '__main__':
	main()

import streamlit as st 
import streamlit.components as stc

# Utils
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import pandas as pd 



# Fxn
def text_downloader(raw_text):
	b64 = base64.b64encode(raw_text.encode()).decode()
	new_filename = "new_text_file_{}_.txt".format(timestr)
	st.markdown("#### Download File ###")
	href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
	st.markdown(href,unsafe_allow_html=True)


def csv_downloader(data):
	csvfile = data.to_csv()
	b64 = base64.b64encode(csvfile.encode()).decode()
	new_filename = "new_text_file_{}_.csv".format(timestr)
	st.markdown("#### Download File ###")
	href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
	st.markdown(href,unsafe_allow_html=False)

# Class
class FileDownloader(object):
	"""docstring for FileDownloader
	>>> download = FileDownloader(data,filename,file_ext).download()

	"""
	def __init__(self, data,filename='myfile',file_ext='csv'):
		super(FileDownloader, self).__init__()
		self.data = data
		self.filename = filename
		self.file_ext = file_ext

	def csv_downloader(self,data):
		csvfile = data.to_csv()
		b64 = base64.b64encode(csvfile.encode()).decode()
		new_filename = "new_text_file_{}_.csv".format(timestr)
		st.markdown("#### Download File ###")
		href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
		st.markdown(href,unsafe_allow_html=True)





def main():
	menu = ["Home","About"]

	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		my_text = st.text_area("Question1")
		my_text1=st.text_area("Question2")
		id_is=st.text_area("is_duplicate")
  
		# submit button
		clickSubmit = st.button("Submit")
		d={'Question1':my_text, 'Question2':my_text1, 'is_duplicate':id_is}
		
		df = pd.DataFrame(data=d,index=[0])

		if clickSubmit ==True:
			#df = pd.DataFrame(data=d)
			#df = df.append(d, ignore_index = True)
			st.write(df)
			#open('df.csv', 'w').write(df.to_csv())
			#st.write(my_text,my_text1,id_is)
			# text_downloader(my_text)
			#data={'Question1':my_text, 'Question2':my_text1, 'is_duplicate':id_is}
			#data = data.append(data)
			#df_fin=pd.DataFrame(data, index=[0])
			#df = df.append(pd.DataFrame(data=d))
			download = FileDownloader(df).csv_downloader(df)


	else:
		st.subheader("About")



if __name__ == '__main__':
	main()
