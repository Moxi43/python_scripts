from django import forms
from blog.models import Blog


class ParameterSender(forms.ModelForm):
    header_text = forms.ChoiceField
    header_text_font_color = forms.ChoiceField
    header_text_font_size = forms.ChoiceField
    text_under_header = forms.ChoiceField
    text_under_header_font_color = forms.ChoiceField
    text_under_header_font_size = forms.ChoiceField
    first_paragraph_text = forms.ChoiceField
    first_paragraph_text_font_color = forms.ChoiceField
    first_paragraph_text_font_size = forms.ChoiceField
    second_header_text = forms.ChoiceField
    second_header_text_font_color = forms.ChoiceField
    second_header_text_font_size = forms.ChoiceField
    element1_list = forms.ChoiceField
    element2_list = forms.ChoiceField
    element3_list = forms.ChoiceField
    element4_list = forms.ChoiceField
    element5_list = forms.ChoiceField
    list_elements_font_color = forms.ChoiceField
    list_elements_font_size = forms.ChoiceField

    CHOICES = (
        ('header_text_font_color', 'Font Color'),
        ('header_text', 'Header Text'),
        ('header_text_font_size', 'Font Size'),
        ('text_under_header', 'Header under header'),
        ('text_under_header_font_color', 'Color of header under header'),
        ('text_under_header_font_size', 'Size of header under header'),
        ('first_paragraph_text', 'Text of first paragraph'),
        ('first_paragraph_text_font_color', "Color first paragraph's text"),
        ('first_paragraph_text_font_size', "Size first paragraph's text"),
        ('second_paragraph_text', "Text of second paragraph"),
        ('second_paragraph_text_font_color', "Color second paragraph's text"),
        ('second_paragraph_text_font_size', "Size second paragraph's text"),
        ('third_paragraph_text', "Text of third paragraph"),
        ('third_paragraph_text_font_color', "Color third paragraph's text"),
        ('third_paragraph_text_font_size', "Size third paragraph's text"),
        ('second_header_text', 'Text of second header'),
        ('second_header_text_font_color', 'Color of second header'),
        ('second_header_text_font_size', 'Size of second header'),
        ('third_header_text', 'Text of third header'),
        ('third_header_text_font_color', 'Color of third header'),
        ('third_header_text_font_size', 'Size of third header'),
        ('element1_list', 'Text of 1st element'),
        ('element2_list', 'Text of 2nd element'),
        ('element3_list', 'Text of 3rd element'),
        ('element4_list', 'Text of 4rd element'),
        ('element5_list', 'Text of 5rd element'),
        ('list_elements_font_color', 'Color of elements'),
        ('list_elements_font_size', 'Size of elements'),
        ('footer_1_paragraph_text', 'Text of 1st footer'),
        ('footer_1_paragraph_text_font_color', 'Color of 1st footer'),
        ('footer_1_paragraph_text_font_size', 'Size of 1st footer'),
        ('footer_2_paragraph_text', 'Text of 2nd footer'),
        ('footer_2_paragraph_text_font_color', 'Color od 2nd footer'),
        ('footer_2_paragraph_text_font_size', 'Size of 2nd footer')
    )

    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    class Meta:
        model = Blog
        fields = ('select',)

    def clean_fields(self):
        header_text = self.cleaned_data.get("header_text")
        header_text_font_color = self.cleaned_data.get("header_text_font_color")
        header_text_font_size = self.cleaned_data.get("header_text_font_size")
        return header_text, header_text_font_size, header_text_font_color
