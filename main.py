import streamlit as st

# Objective:
st.title("📝Text Analyzer")

# 1- Assignment Instructions
st.write("This is a simple text analyzer that performs the following functions:")
st.write("Enter a paragraph to analyze below:")
user_input = st.text_area("Write your paragraph here:", height=200)

st.subheader("Search and Replace")
search_word = st.text_input("Enter a word to search for:")
replace_word = st.text_input("Enter a word to replace it with:")

if st.button("Text Analyze"):
    if not user_input.strip():  # Validate input
        st.error("Please enter a paragraph to analyze.")
    else:
        #  2--Search and Replace
        if search_word and replace_word:
            if search_word in user_input:
                new_text = user_input.replace(search_word, replace_word)
                st.header("Modified Paragraph:")
                st.success(new_text)
            else:
                st.warning(f"The word '{search_word}' was not found in the paragraph.")

        #3-- Word and Character Count
        word_count = len(user_input.split())
        char_count = len(user_input)
        st.subheader("Text Analysis")
        st.success(f"Total Words: {word_count}")
        st.success(f"Total Characters: {char_count}")

        # 4- Vowel Count
        vowels = set("aeiou")
        vowel_count = sum(1 for char in user_input if char.lower() in vowels)
        st.success(f"Total Vowels: {vowel_count}")

        # 5- Uppercase and Lowercase Conversion
        st.subheader("Uppercase and Lowercase Conversion")
        st.write("Uppercase Paragraph:")
        st.success(user_input.upper())
        st.write("Lowercase Paragraph:")
        st.success(user_input.lower())

      

        # 6-Average Word Length
        if word_count > 0:
            average_word_length = char_count / word_count
            st.success(f"Average Word Length: {average_word_length:.2f} characters")
        else:
            st.warning("Cannot calculate average word length: No words found.")

        # 7-Word Frequency
        word_frequecy = {}
        words = user_input.split()
        for word in words:
            if word in word_frequecy:
                word_frequecy[word] += 1
            else:
                word_frequecy[word] = 1
                
        st.subheader("Word Frequency")
        st.write("Word Frequency in the paragraph:")
        for word, frequency in word_frequecy.items():
            st.success(f"{word}: {frequency}")
else:
    st.write("Click the button to analyze the text")
