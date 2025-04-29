# Book Summarizer

## Acknowledgment
I would like to thank the following individuals and organisations that made this project possible. 
* Groq for providing me free access to their API key and thereby allowing me to gain hands-on experience in making API calls without having to constantly worry about token limits.
* Google Books for enabling me to perform full-text searches on book content on the Web using their free API.

## Abstract
Recently discovering a barcode scanner app on my Android phone led to this little project that makes use of scanned ISBN's and prompt engineering techniques. Among the basic information about the book, the main feature is the prentation of the synopsis. The length of the synopsis can be adjusted to the user's preference in terms of number of words. All the information is presented in a simple Web app interface. 
<br><br>
The application follows the sequence below:
1. Ask for an ISBN.
2. Get the book information from Google Books.  
3. Summarize the storyline in 300 words.

## Development Notes
* The barcode scannner is an app on my Android phone. The flow can be streamlined by connecting the phone or an external scanning device to the computer to pass scanned barcodes to the program. 
* It was fun to experiment with the book synopsis generating prompt to see how the tone changes from a moderate book promoter to an over-enthusiastic book seller and somewhere in between. 

# Installation
To run book_summarizer.py, do the following:

### Step 1. Place the files in a folder. 
1. Place the `.py` file in a local folder (e.g. `C:\temp\book_summarizer`).
2. Create a file called `.env` and place the GROQ API key in the following format:
	`GROQ_API_KEY = <groq_api_key>`
3. Place the `.env` file in the same local folder. 

### Step 2. Install Python. 
1. In Windows, open the Command Prompt window.
2. Make sure Python is installed. In the Command Prompt window, type:
	`python --version`
If you get an error or "Python is not recognized", you need to install Python:
	1. Go to `https://www.python.org/downloads/`.
	2. Download the latest Python installer for Windows
	3. Run the installer and make sure to check `Add Python to PATH` during installation

### Step 3. Set up a virtual environment. 
This keeps your project dependencies isolated:
1. In the Command Prompt window, go to the script folder. Type:<br>
	`cd C:\<path to your script folder>`
2. In the Command Prompt, create a Python virtual environment named `book_summarizer_env`.<br>
	`python -m venv book_summarizer_env`
3. In the Command Prompt, activate the Python virtual environment.<br>
	`book_summarizer_env\Scripts\activate`
4. Install the required dependencies.<br>
  `pip install -r requirements.txt`

### Step 4. Run the script. 
1. In the Command Prompt window, run the Streamlit application. Type:<br>
	`streamlit run book_summarizer.py`
<br>
<br>
This will start a local web server and open the application in your browser. Press the Analyse button to view the results. 

## Web app in action
![Alt text for screen reader](https://github.com/renabracha/book_summarizer/blob/main/sceenshot_1.JPG?raw=true)
![Alt text for screen reader](https://github.com/renabracha/book_summarizer/blob/main/sceenshot_2.JPG?raw=true)