from unstructured.partition.docx import partition_docx
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import CompositeElement, Table


def unstructure_word(word_name):
    elements = partition_docx(
        filename=word_name,
        multipage_sections=True,
        infer_table_structure=True,
        include_page_breaks=False,
    )

    chunks = chunk_by_title(
        elements=elements,
        multipage_sections=True,
        combine_text_under_n_chars=0,
        new_after_n_chars=None,
        max_characters=4000,
    )

    text_list = []

    for chunk in chunks:
        if isinstance(chunk, CompositeElement):
            text = chunk.text
            page_number = getattr(chunk.metadata, 'page_number', 1)  # Default to 1 if not available
            text_list.append((text, page_number))
        elif isinstance(chunk, Table):
            page_number = getattr(chunk.metadata, 'page_number', 1)
            if text_list:
                text_list[-1] = text_list[-1] + "\n" + chunk.metadata.text_as_html
            else:
                text_list.append((chunk.metadata.text_as_html, page_number))

    merged_list = []
    title_buffer = []
    buffer_page: int = None

    for text, page_number in text_list:
        stripped_text = text.strip()
        if stripped_text and (
            not stripped_text.endswith(".") and not "\n" in stripped_text
        ):  # This is a title block
            title_buffer.append(stripped_text)
            if buffer_page is None:
                buffer_page = page_number
        else:
            if title_buffer:
                merged_title = "\n".join(title_buffer)
                merged_text = f"{merged_title}\n{text}"
                merged_list.append((merged_text, buffer_page))
                title_buffer = []
                buffer_page = None
            else:
                merged_list.append((text, page_number))

    if title_buffer:
        merged_title = "\n".join(title_buffer)
        if merged_list:
            last_text, last_page = merged_list[-1]
            merged_list[-1] = (f"{last_text}\n{merged_title}", last_page)
        else:
            merged_list.append((merged_title, buffer_page if buffer_page else 1))

    return merged_list