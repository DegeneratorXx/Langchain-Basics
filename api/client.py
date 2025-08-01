import streamlit as st
import requests as req

def getOllama_response(input_text):
    """
    Send a request to the FastAPI server to get historical overview.
    
    Args:
        input_text (str): The place name to get historical overview for
        
    Returns:
        str: Historical overview of the place
    """
    try:
        response = req.post(
            "http://localhost:8000/history",
            json={'place': input_text}  # Fixed: Match server's expected format
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['historical_summary']  # Fixed: Match server's response format
    except req.exceptions.RequestException as e:
        return f"Error connecting to server: {str(e)}"
    except KeyError as e:
        return f"Unexpected response format: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title('LangChain Demo with Gemma API')
st.header("Historical Overview Bot")

input_text = st.text_input("Enter a place to get its historical overview")

if input_text:
    with st.spinner("Generating historical overview..."):
        result = getOllama_response(input_text)
        st.write(result)