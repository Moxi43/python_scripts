from django.db import models


class Blog(models.Model):
    # header parameters
    header_text = models.CharField("Blog Header", max_length=64, default="My blog")
    header_text_font_color = models.CharField("Font color of header text", max_length=8, default="Black")
    header_text_font_size = models.CharField("Font size of header text", max_length=4, default="20px")
    # under header parameters
    text_under_header = models.TextField("Text under header", default="Text under header")
    text_under_header_font_color = models.CharField("Font's color of text under header", max_length=8, default="Black")
    text_under_header_font_size = models.CharField("Font's size of text under header", max_length=8, default="12px")
    # paragraphs parameters
    first_paragraph_text = models.TextField("First paragraph text", default="First paragraph text")
    first_paragraph_text_font_color = models.CharField("Color of paragraph", max_length=8, default="Black")
    first_paragraph_text_font_size = models.CharField("Size of paragraph", max_length=4, default="12px")
    second_paragraph_text = models.TextField("Second paragraph text", default="Second paragraph text")
    second_paragraph_text_font_color = models.CharField("Color of paragraph n2", max_length=8, default="Black")
    second_paragraph_text_font_size = models.CharField("Size of paragraph n2", max_length=8, default="Black")
    third_paragraph_text = models.TextField("Third paragraph text", default="Third paragraph text")
    third_paragraph_text_font_color = models.CharField("Color of paragraph n3", max_length=8, default="Black")
    third_paragraph_text_font_size = models.CharField("Size of paragraph n3", max_length=8, default="Black")
    # second header parameters
    second_header_text = models.CharField("Second Blog Header", max_length=64, default="Second header")
    second_header_text_font_color = models.CharField("Font color of second header text", max_length=8, default="Black")
    second_header_text_font_size = models.CharField("Font size of second header text", max_length=4, default="16px")
    # third header parameters
    third_header_text = models.CharField("Third Blog Header", max_length=64, default="Third header")
    third_header_text_font_color = models.CharField("Font color of third header text", max_length=8, default="Black")
    third_header_text_font_size = models.CharField("Font size of third header text", max_length=4, default="16px")
    # list parameters
    element1_list = models.TextField("element1 text", default="1st element text")
    element2_list = models.TextField("element2 text", default="2nd element text")
    element3_list = models.TextField("element3 text", default="3rd element text")
    element4_list = models.TextField("element4 text", default="4th element text")
    element5_list = models.TextField("element5 text", default="5th element text")
    list_elements_font_color = models.CharField('list color', max_length=8, default="Black")
    list_elements_font_size = models.CharField('list size', max_length=4, default="12px")
    # footer parameters
    footer_1_paragraph_text = models.TextField("1st footer paragraph text", default="footer 1st paragraph")
    footer_1_paragraph_text_font_color = models.CharField("1st footer paragraph color", max_length=8, default="Black")
    footer_1_paragraph_text_font_size = models.CharField("1st footer paragraph font size", max_length=4, default="12px")
    footer_2_paragraph_text = models.TextField("2nd footer paragraph text", default="footer 1st paragraph")
    footer_2_paragraph_text_font_color = models.CharField("2nd footer paragraph font color", max_length=8, default="Black")
    footer_2_paragraph_text_font_size = models.CharField("2nd footer paragraph font size", max_length=4, default="12px")

    def __str__(self):
        return self.header_text, self.header_text_font_size, self.header_text_font_color
