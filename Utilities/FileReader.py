import os, fitz, tempfile, logging

def file_reader(form_data_files):
    file = form_data_files['file']
    file_name, file_extension = os.path.splitext(file.filename)
    if file_extension == ".pdf":

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
            file.save(temp_file.name)

        with fitz.open(temp_file.name) as pdf:
            num_pages = pdf.page_count
            text_body = ""
            for page_num in range(num_pages):
                page = pdf.load_page(page_num)
                text_body += page.get_text()

        os.unlink(temp_file.name)

    elif file_extension == ".txt":
        text_body = file.read().decode('utf-8')
        logging.info(text_body)
    else:
        text_body = None
    return text_body