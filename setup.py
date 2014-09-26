from setuptools import setup

setup(
    name = "django-geolocation",
    #url = "http://github.com/suselrd/django-geolocation/",
    author = "Susel Ruiz Duran",
    author_email = "suselrd@gmail.com",
    version = "0.1.0",
    packages = ["geolocation"],
    include_package_data=True,
    zip_safe=False,
    description = "Geolocation for Django",
    install_requires=['django>=1.6.1', ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],

)
