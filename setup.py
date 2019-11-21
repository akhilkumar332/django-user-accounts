from setuptools import setup, find_packages


setup(
    name="django-user-accounts",
    version="2.1.0",
    author="Akhil kumar",
    author_email="akhilkumar332@gmail.com",
    description="a Django user account app",
    long_description=open("README.rst").read(),
    license="MIT",
    url="http://github.com/akhilkumar332/django-user-accounts",
    packages=find_packages(),
    install_requires=[
        "Django>=1.11",
        "django-appconf>=1.0.1",
        "pytz>=2015.6"
    ],
    zip_safe=False,
    package_data={
        "account": [
            "locale/*/LC_MESSAGES/*",
        ],
    },
    extras_require={
        "pytest": ["pytest", "pytest-django", "PyUa-env", "pyua-app"]
    },
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ]
)
