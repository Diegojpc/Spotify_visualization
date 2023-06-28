import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='spotify_project',
    version='0.1.0',
    author='Diego José Peña Casadiegos',
    author_email='diegojosepc3@hotmail.com',
    description='análisis y el aprendizaje automático aplicados a un conjunto de datos que contiene el "top" de canciones desde el año 2000 hasta 2019. El objetivo principal del proyecto es extraer información relevante y obtener conocimientos sobre las tendencias y características de las canciones populares durante ese periodo.',
    python_requires='>=3',
    license='MIT',
    url='',
    packages=find_packages(),
    long_description=readme(),
)