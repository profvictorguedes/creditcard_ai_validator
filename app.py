import streamlit as st
from azure_blob import upload_to_blob
from ocr_service import extract_text_from_image
from card_validator import detect_credit_card_info


def configure_interface():
    st.title("Upload here - Azure - Fake Docs")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        blob_url = upload_to_blob(uploaded_file)

        if blob_url:
            st.success("File successfuly sent to Azure Blob Storage")

            text_lines = extract_text_from_image(blob_url)
            credit_card_info = detect_credit_card_info(text_lines)

            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("Error while sending to Azure Blob Storage")


def show_image_and_validation(blob_url, credit_card_info):
    st.image(
        blob_url,
        caption="Image sent!",
        use_column_width=True
    )

    st.write("Validation results:")

    if credit_card_info:
        st.markdown(
            "<h1 style='color: green;'>Valid Card</h1>",
            unsafe_allow_html=True
        )
        st.write(f"Cardholder: {credit_card_info['card_name']}")
        st.write(f"Bank of Issue: {credit_card_info['bank_name']}")
        st.write(f"Expiry Date: {credit_card_info['expiry_date']}")
    else:
        st.markdown(
            "<h1 style='color: red;'>Invalid Card</h1>",
            unsafe_allow_html=True
        )
        st.write("This is not a valid card.")


if __name__ == "__main__":
    configure_interface()
