from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ParameterSender
from .models import Blog


def index(request):
    username_id = auth.get_user(request).id
    if not username_id:
        return redirect("/authorization/login/")
    elements = Blog.objects.get(id=username_id)
    header_text = elements.header_text
    header_text_font_color = elements.header_text_font_color
    header_text_font_size = elements.header_text_font_color
    text_under_header = elements.text_under_header
    text_under_header_font_color = elements.text_under_header_font_color
    text_under_header_font_size = elements.text_under_header_font_size
    first_paragraph_text = elements.first_paragraph_text
    first_paragraph_text_font_color = elements.first_paragraph_text_font_color
    first_paragraph_text_font_size = elements.first_paragraph_text_font_size
    second_paragraph_text = elements.second_paragraph_text
    second_paragraph_text_font_color = elements.second_paragraph_text_font_color
    second_paragraph_text_font_size = elements.second_paragraph_text_font_size
    third_paragraph_text = elements.third_paragraph_text
    third_paragraph_text_font_color = elements.third_paragraph_text_font_color
    third_paragraph_text_font_size = elements.third_paragraph_text_font_size
    second_header_text = elements.second_header_text
    second_header_text_font_color = elements.second_header_text_font_color
    second_header_text_font_size = elements.second_header_text_font_size
    third_header_text = elements.third_header_text
    third_header_text_font_color = elements.third_header_text_font_color
    third_header_text_font_size = elements.third_header_text_font_size
    element1_list = elements.element1_list
    element2_list = elements.element2_list
    element3_list = elements.element3_list
    element4_list = elements.element4_list
    element5_list = elements.element5_list
    list_elements_font_color = elements.list_elements_font_color
    list_elements_font_size = elements.list_elements_font_size
    footer_1_paragraph_text = elements.footer_1_paragraph_text
    footer_1_paragraph_text_font_color = elements.footer_1_paragraph_text_font_color
    footer_1_paragraph_text_font_size = elements.footer_1_paragraph_text_font_size
    footer_2_paragraph_text = elements.footer_2_paragraph_text
    footer_2_paragraph_text_font_color = elements.footer_2_paragraph_text_font_color
    footer_2_paragraph_text_font_size = elements.footer_2_paragraph_text_font_size

    return render(
        request, 'blog/index.html', {
            "header_text": header_text,
            "header_text_font_color": header_text_font_color,
            "header_text_font_size": header_text_font_size,
            "text_under_header": text_under_header,
            "text_under_header_font_color": text_under_header_font_color,
            "text_under_header_font_size": text_under_header_font_size,
            "first_paragraph_text": first_paragraph_text,
            "first_paragraph_text_font_color": first_paragraph_text_font_color,
            "first_paragraph_text_font_size": first_paragraph_text_font_size,
            "second_paragraph_text": second_paragraph_text,
            "second_paragraph_text_font_color": second_paragraph_text_font_color,
            "second_paragraph_text_font_size": second_paragraph_text_font_size,
            "third_paragraph_text": third_paragraph_text,
            "third_paragraph_text_font_color": third_paragraph_text_font_color,
            "third_paragraph_text_font_size": third_paragraph_text_font_size,
            "second_header_text": second_header_text,
            "second_header_text_font_color": second_header_text_font_color,
            "second_header_text_font_size": second_header_text_font_size,
            "third_header_text": third_header_text,
            "third_header_text_font_color": third_header_text_font_color,
            "third_header_text_font_size": third_header_text_font_size,
            "element1_list": element1_list,
            "element2_list": element2_list,
            "element3_list": element3_list,
            "element4_list": element4_list,
            "element5_list": element5_list,
            "list_elements_font_color": list_elements_font_color,
            "list_elements_font_size": list_elements_font_size,
            "footer_1_paragraph_text": footer_1_paragraph_text,
            "footer_1_paragraph_text_font_color": footer_1_paragraph_text_font_color,
            "footer_1_paragraph_text_font_size": footer_1_paragraph_text_font_size,
            "footer_2_paragraph_text": footer_2_paragraph_text,
            "footer_2_paragraph_text_font_color": footer_2_paragraph_text_font_color,
            "footer_2_paragraph_text_font_size": footer_2_paragraph_text_font_size,
            "username": auth.get_user(request).username,
        }
    )


def editor(request):
    if request.method == "POST":
        form = ParameterSender(request.POST)
        if form.is_valid():

            username_id = auth.get_user(request).id
            ##########################################################################
            selected_parameter = request.POST.get("select")
            text_parameter = request.POST.get("param")
            filters = Blog.objects.filter(id=username_id)

            if selected_parameter == 'header_text':
                filters.update(header_text=text_parameter)

            elif selected_parameter == "header_text_font_color":
                filters.update(header_text_font_color=text_parameter)

            elif selected_parameter == "header_text_font_size":
                filters.update(header_text_font_size=text_parameter)

            elif selected_parameter == 'text_under_header':
                filters.update(text_under_parameter=text_parameter)

            elif selected_parameter == "text_under_header_font_color":
                filters.update(text_under_header_font_color=text_parameter)

            elif selected_parameter == "text_under_header_font_size":
                filters.update(text_under_header_font_size=text_parameter)

            elif selected_parameter == "first_paragraph_text":
                filters.update(first_paragraph_text=text_parameter)

            elif selected_parameter == 'first_paragraph_text_font_color':
                filters.update(first_paragraph_text_font_color=text_parameter)

            elif selected_parameter == "first_paragraph_text_font_size":
                filters.update(first_paragraph_text_font_size=text_parameter)

            elif selected_parameter == 'second_paragraph_text':
                filters.update(second_paragraph_text=text_parameter)

            elif selected_parameter == 'second_paragraph_text_font_color':
                filters.update(second_paragraph_text_font_color=text_parameter)

            elif selected_parameter == 'second_paragraph_text_font_size':
                filters.update(second_paragraph_text_font_size=text_parameter)

            elif selected_parameter == 'third_paragraph_text':
                filters.update(third_paragraph_text=text_parameter)

            elif selected_parameter == 'third_paragraph_text_font_color':
                filters.update(third_paragraph_text_font_color=text_parameter)

            elif selected_parameter == 'third_paragraph_text_font_size':
                filters.update(third_paragraph_text_font_size=text_parameter)

            elif selected_parameter == 'second_header_text':
                filters.update(second_header_text=text_parameter)

            elif selected_parameter == 'second_header_text_font_color':
                filters.update(second_header_text_font_color=text_parameter)

            elif selected_parameter == 'second_header_text_font_size':
                filters.update(second_header_text_font_size=text_parameter)

            elif selected_parameter == 'third_header_text':
                filters.update(third_header_text=text_parameter)

            elif selected_parameter == 'third_header_text_font_color':
                filters.update(third_header_text_font_color=text_parameter)

            elif selected_parameter == 'third_header_text_font_size':
                filters.update(third_header_text_font_size=text_parameter)

            elif selected_parameter == 'element1_list':
                filters.update(element1_list=text_parameter)

            elif selected_parameter == 'element2_list':
                filters.update(element2_list=text_parameter)

            elif selected_parameter == 'element3_list':
                filters.update(element3_list=text_parameter)

            elif selected_parameter == 'element4_list':
                filters.update(element4_list=text_parameter)

            elif selected_parameter == 'element5_list':
                filters.update(element5_list=text_parameter)

            elif selected_parameter == 'list_elements_font_color':
                filters.update(list_elements_font_color=text_parameter)

            elif selected_parameter == 'list_elements_font_size':
                filters.update(list_elements_font_size=text_parameter)

            elif selected_parameter == 'footer_1_paragraph_text':
                filters.update(footer_1_paragraph_text=text_parameter)

            elif selected_parameter == 'footer_1_paragraph_text_font_color':
                filters.update(footer_1_paragraph_text_font_color=text_parameter)

            elif selected_parameter == 'footer_1_paragraph_text_font_size':
                filters.update(footer_1_paragraph_text_font_size=text_parameter)

            elif selected_parameter == 'footer_2_paragraph_text':
                filters.update(footer_2_paragraph_text=text_parameter)

            elif selected_parameter == 'footer_2_paragraph_text_font_color':
                filters.update(footer_2_paragraph_text_font_color=text_parameter)

            elif selected_parameter == 'footer_2_paragraph_text_font_size':
                filters.update(footer_2_paragraph_text_font_size=text_parameter)

            else:
                pass

            return HttpResponseRedirect("/blog/")

    else:
        form = ParameterSender()

    return render(request, 'blog/editor.html', {"form": form})


def example(request):
    return render(request, 'blog/example-page.html')

def viewer(request, username_id):

    elements = Blog.objects.get(id=username_id)
    header_text = elements.header_text
    header_text_font_color = elements.header_text_font_color
    header_text_font_size = elements.header_text_font_color
    text_under_header = elements.text_under_header
    text_under_header_font_color = elements.text_under_header_font_color
    text_under_header_font_size = elements.text_under_header_font_size
    first_paragraph_text = elements.first_paragraph_text
    first_paragraph_text_font_color = elements.first_paragraph_text_font_color
    first_paragraph_text_font_size = elements.first_paragraph_text_font_size
    second_paragraph_text = elements.second_paragraph_text
    second_paragraph_text_font_color = elements.second_paragraph_text_font_color
    second_paragraph_text_font_size = elements.second_paragraph_text_font_size
    third_paragraph_text = elements.third_paragraph_text
    third_paragraph_text_font_color = elements.third_paragraph_text_font_color
    third_paragraph_text_font_size = elements.third_paragraph_text_font_size
    second_header_text = elements.second_header_text
    second_header_text_font_color = elements.second_header_text_font_color
    second_header_text_font_size = elements.second_header_text_font_size
    third_header_text = elements.third_header_text
    third_header_text_font_color = elements.third_header_text_font_color
    third_header_text_font_size = elements.third_header_text_font_size
    element1_list = elements.element1_list
    element2_list = elements.element2_list
    element3_list = elements.element3_list
    element4_list = elements.element4_list
    element5_list = elements.element5_list
    list_elements_font_color = elements.list_elements_font_color
    list_elements_font_size = elements.list_elements_font_size
    footer_1_paragraph_text = elements.footer_1_paragraph_text
    footer_1_paragraph_text_font_color = elements.footer_1_paragraph_text_font_color
    footer_1_paragraph_text_font_size = elements.footer_1_paragraph_text_font_size
    footer_2_paragraph_text = elements.footer_2_paragraph_text
    footer_2_paragraph_text_font_color = elements.footer_2_paragraph_text_font_color
    footer_2_paragraph_text_font_size = elements.footer_2_paragraph_text_font_size

    return render(
        request, 'blog/viewer.html', {
            "header_text": header_text,
            "header_text_font_color": header_text_font_color,
            "header_text_font_size": header_text_font_size,
            "text_under_header": text_under_header,
            "text_under_header_font_color": text_under_header_font_color,
            "text_under_header_font_size": text_under_header_font_size,
            "first_paragraph_text": first_paragraph_text,
            "first_paragraph_text_font_color": first_paragraph_text_font_color,
            "first_paragraph_text_font_size": first_paragraph_text_font_size,
            "second_paragraph_text": second_paragraph_text,
            "second_paragraph_text_font_color": second_paragraph_text_font_color,
            "second_paragraph_text_font_size": second_paragraph_text_font_size,
            "third_paragraph_text": third_paragraph_text,
            "third_paragraph_text_font_color": third_paragraph_text_font_color,
            "third_paragraph_text_font_size": third_paragraph_text_font_size,
            "second_header_text": second_header_text,
            "second_header_text_font_color": second_header_text_font_color,
            "second_header_text_font_size": second_header_text_font_size,
            "third_header_text": third_header_text,
            "third_header_text_font_color": third_header_text_font_color,
            "third_header_text_font_size": third_header_text_font_size,
            "element1_list": element1_list,
            "element2_list": element2_list,
            "element3_list": element3_list,
            "element4_list": element4_list,
            "element5_list": element5_list,
            "list_elements_font_color": list_elements_font_color,
            "list_elements_font_size": list_elements_font_size,
            "footer_1_paragraph_text": footer_1_paragraph_text,
            "footer_1_paragraph_text_font_color": footer_1_paragraph_text_font_color,
            "footer_1_paragraph_text_font_size": footer_1_paragraph_text_font_size,
            "footer_2_paragraph_text": footer_2_paragraph_text,
            "footer_2_paragraph_text_font_color": footer_2_paragraph_text_font_color,
            "footer_2_paragraph_text_font_size": footer_2_paragraph_text_font_size,
        }
    )