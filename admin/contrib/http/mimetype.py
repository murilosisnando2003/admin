import logging
import mimetypes
import os

from django.conf import settings


log = logging.getLogger('intranet.dms.mimetype')

try:
    #se nao tem python-magic usa guess_type
    import magic
except Exception as e:
    magic = None

mimetype_icons = {
    'application/pdf': 'file_extension_pdf.png',
    'application/zip': 'file_extension_zip.png',
    'application/ogg': 'file_extension_ogg.png',
    'application/postscript': 'file_extension_ps.png',
    'application/x-gzip': 'file_extension_gz.png',
    'application/x-rar-compressed': 'file_extension_rar.png',
    'application/x-zip-compressed': 'file_extension_zip.jpg',
    'application/x-troff-msvideo': 'file_extension_avi.png',
    'application/acad': 'file_extension_dwg.png',
    'application/octet-stream': 'file_extension_exe.png',
    'application/vnd.oasis.opendocument.text': 'ODF_textdocument_32x32.png',
    'application/vnd.oasis.opendocument.spreadsheet': 'ODF_spreadsheet_32x32.png',
    'application/vnd.oasis.opendocument.presentation': 'ODF_presentation_32x32.png',
    'application/vnd.oasis.opendocument.graphics': 'ODF_drawing_32x32.png',
    'application/vnd.ms-excel': 'file_extension_xls.png',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'file_extension_xls.png',
    'application/msword': 'file_extension_doc.png',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'file_extension_doc.png',
    'application/mspowerpoint': 'file_extension_pps.png',
    'application/vnd.ms-powerpoint': 'file_extension_pps.png',
    'application/wav': 'file_extension_wav.png',
    'application/x-wav': 'file_extension_wav.png',
    'application/vnd.oasis.opendocument.text': 'ODF_textdocument_32x32.png',

    'image/jpeg': 'file_extension_jpeg.png',
    'image/png': 'file_extension_png.png',
    'image/x-png': 'file_extension_png.png',
    'image/tiff': 'file_extension_tif.png',
    'image/x-tiff': 'file_extension_tif.png',
    'image/bmp': 'file_extension_bmp.png',
    'image/gif': 'file_extension_gif.png',
    'image/vnd.dwg': 'file_extension_dwg.png',
    'image/x-dwg': 'file_extension_dwg.png',

    'audio/mpeg': 'file_extension_mp3.png',
    'audio/mid': 'file_extension_mid.png',
    'audio/x-wav': 'file_extension_wav.png',
    'audio/vnd.wav': 'file_extension_wav.png',
    'audio/x-pn-realaudio': 'file_extension_ram.png',
    'audio/mp4': 'file_extension_mp4.png',
    'audio/x-ms-wma': 'file_extension_wma.png',

    'video/avi': 'file_extension_avi.png',
    'video/mpeg': 'file_extension_mpeg.png',
    'video/quicktime': 'file_extension_mov.png',
    'video/x-ms-asf': 'file_extension_asf.png',
    'video/x-ms-wmv': 'file_extension_wmv.png',

    'text/html': 'file_extension_html.png',
    'text/plain': 'file_extension_txt.png',
    'type/unknown': 'unknown.png',
    'type/error': 'error.png',
}

def get_mimetype(filepath):
    file_mimetype = 'type/unknown'
    try:
        path, filename = os.path.split(filepath)
        file_mimetype, file_mime_encoding = mimetypes.guess_type(filename)
        if not file_mimetype:
            file_mimetype = "type/unknown"
    except:
        file_mimetype = "type/error"

    return file_mimetype

def get_icon_file_url(mimetype):
    file_name = mimetype_icons.get(mimetype,'unknown.png')
    return '%smimetypes/%s' % (settings.STATIC_URL,file_name)
