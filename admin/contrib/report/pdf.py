from django.template.loader import get_template
from django.http import HttpResponse
from django.utils.encoding import smart_unicode


def render_to_pdf(request, template_name, context, filename=None):
    """
    :param request: HTTPRequest
    :param template_name: str
    :param context: RequestContext
    :param filename: str
    :return:
    """
    from weasyprint import HTML
    html_template = get_template(template_name)
    rendered_html = smart_unicode(html_template.render(context))
    pdf_file = HTML(string=rendered_html).write_pdf()
    http_response = HttpResponse(pdf_file, content_type='application/pdf')

    if filename is not None:
        http_response['Content-Disposition'] = 'filename="%s.pdf"'%filename

    return http_response


def render_to_HTML(request, template_name, context):
    """
    :param request: HTTPRequest
    :param template_name: str
    :param context: RequestContext
    :return: HTML document do model weasyprint
    """
    from weasyprint import HTML
    html_template = get_template(template_name)
    rendered_html = smart_unicode(html_template.render(context))
    return HTML(string=rendered_html).render()


def render_HTML_to_pdf(documents, filename=None):
    """

    :param documents:list of HTML documents
    :param filename:
    :return:
    """
    all_pages = []
    for doc in documents:
        for p in doc.pages:
            all_pages.append(p)

    pdf_file = documents[0].copy(all_pages).write_pdf()
    http_response = HttpResponse(pdf_file, content_type='application/force-download')
    if filename is not None:
        http_response['Content-Disposition'] = 'filename="%s.pdf"'%filename

    return http_response
