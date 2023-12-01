import streamlit as st

contact_form = """
   <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 200vh;
           
        }

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
        }

        input,
        textarea,
        button {
            width: 100%;
            margin-bottom: 15px;
            padding: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }

        textarea {
            resize: vertical;
        }

        button {
            background-color: #4caf50;
            color: #fff;
            font-size: 18px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>

    <form target="_blank" action="https://formsubmit.co/khairibou20@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required> 
         <textarea     id="story" name="COMMENTS" rows="10" cols="33">
 write your comments about this website here ....
         </textarea>
        <button type="submit">Send</button>
    </form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

