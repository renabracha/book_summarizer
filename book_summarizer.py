import os
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import requests
from dotenv import load_dotenv
import streamlit as st

# Set up the environment variables
load_dotenv()

# Initialise the language model
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model = "llama-3.3-70b-versatile")

# Get the information on the book from Google Books
def get_book_data(barcode):

    # Example API call - https://www.googleapis.com/books/v1/volumes?q=isbn:9780552176453
    # Define the API endpoint and query parameters
    url = "https://www.googleapis.com/books/v1/volumes"

    # Format location and country for the 'q' parameter
    isbn = f"isbn:{barcode}"
    params = {
        "q": isbn
    }

    # Define the request headers with API key and host
    headers = {
        "Accept": "application/json"
    }

    # Send a GET request to the API endpoint with query parameters and headers
    response = requests.request("GET", url, headers=headers, params=params)

    # Parse the response data
    data = response.json()

    # Return the weather data
    return data

# Define prompts and prompt templates

book_info_prompt = PromptTemplate(
    input_variables=["book_data"],
    template = """Tell me about the book, based on the information in {book_data}.
    Include:
    * Title: Display the title of the book.
    * Authors: List the names of the authors.
    * ISBN: Display the 13-digit ISBN.
    * Synosis: Write a 300-word summary of the book description in friendly, engaging language. Highlight the main themes and characters.
    * Published Date: Display the published date.
    * Published By: Display the publisher.
    * Book Cover: Format the image URL as an HTML img tag like this: <img src="[IMAGE_URL]" alt="Book Cover" width="150">
    """
)

# Run the prompt
def book_summariser(book_data):
    """Get the barcode of a book and display the information about the book.

    Args:
        barcode: A 13-digit ISBN of a book.

    Returns:
        str: A summary of the storyline, authors, publisher, published date, an image of the book cover.
    """
  
    book_summary = (book_info_prompt | llm).invoke({"book_data": book_data}).content
    return book_summary

# Streamlit UI
st.title('Book Summarizer')

# Welcome message
st.markdown("""
Hey there! 👋 Found a book you're interested in?
""")

# Create session state to store variables
if 'current_step' not in st.session_state:
    st.session_state.current_step = 'book_barcode'
if 'book_barcode' not in st.session_state:
    st.session_state.book_barcode = None
if 'book_data' not in st.session_state:
    st.session_state.book_data = None
if 'book_summary' not in st.session_state:
    st.session_state.book_summary = None

# Step 1: Get book barcode
if st.session_state.current_step == 'book_barcode':
    barcode_input = st.text_input("Give me the barcode and I'll let you know what it's about.: ", key="barcode_input")
    if st.button("Let's find out!", key="barcode_button"):
        if barcode_input:
            st.session_state.book_barcode = barcode_input
            st.spinner(f'Book barcode: {barcode_input}')
            st.session_state.current_step = 'process'
            st.rerun()

# Step 2: Process book barcode and produce results
elif st.session_state.current_step == 'process':

    # Validate that we have all required data
    if not (st.session_state.book_barcode):
        st.session_state.current_step = 'book_barcode'
        st.rerun()
    try:
        # Fetch book information
        with st.spinner('Fetching book details...'):
            st.session_state.book_data = get_book_data(st.session_state.book_barcode)
            st.success('Successfully received book details')        

        # Summarize and format book plot
        with st.spinner('Summarizing and formatting book content...'):
            st.session_state.book_summary = book_summariser(st.session_state.book_data)
            st.markdown(st.session_state.book_summary, unsafe_allow_html=True)
         
        # Reset button
        if st.button("Start over", key="reset_button"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.session_state.current_step = 'book_barcode'  # Set initial step explicitly
            st.rerun()
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        if st.button("Try again", key="error_button"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()