from uuslug import slugify
from uuid import uuid4
from os.path import splitext


def ruta_de_portadas(instance, filename):
    slug = slugify(instance.nombre)
    _uuid = str(uuid4())[:4]
    file_name, extension = splitext(filename)
    file_path = 'libros/portadas/{}-cover-{}{}'.format(slug, _uuid, extension)
    return file_path
