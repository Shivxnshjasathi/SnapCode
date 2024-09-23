import streamlit as st
from PIL import Image
import google.generativeai as genai

# Directly configure the Gemini API
api_key = "AIzaSyAPHtUCHKOZ2YAOOlPETWaVFaBAoVKhs6U"  # Replace with your actual API key
genai.configure(api_key=api_key)

def process_image(image):
    # Process the image (if needed)
    return image

def generate_code(image):
    # Set up the model
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model name
    
    # Prepare the prompt
    prompt = """
    Analyze this UI design image and generate the corresponding HTML and CSS code. 
    Please provide a complete implementation that closely resembles the image, 
    including layout, colors, and styling. Structure the response as follows:
    1. Brief description of the UI
    2. HTML code
    3. CSS code
    4. Flutter
    """
    
    # Generate content
    try:
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"Error generating content: {e}"

def main():
    st.title("UI Design to Code Generator")
    
    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # Process the image
        image = Image.open(uploaded_file)
        
        # Generate code
        with st.spinner("Generating code..."):
            generated_code = generate_code(image)
        
        if generated_code:
            st.subheader("Generated Code:")
            st.code(generated_code, language='html')
            
            # Optionally, save the generated code to a file with UTF-8 encoding
            with open("generated_ui.html", "w", encoding="utf-8") as html_file:
                html_file.write(generated_code)
                
            st.success("Code has been saved to 'generated_ui.html'")
        else:
            st.error("Failed to generate code.")

if __name__ == "__main__":
    main()
