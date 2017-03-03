import ast
from setuptools import setup, find_packages


requirements = [
    "click==6.7",
]

]


def get_version():
    # Extract version without importing it to avoid dependencies
    with open("src/{{ cookiecutter.project_slug }}/version.py") as version_file:
        for line in version_file:
            if "VERSION" in line:
                return ast.literal_eval(line.partition("=")[2].strip())
    raise RuntimeError("Invalid version file.")


if __name__ == "__main__":
    setup(
        name='{{ cookiecutter.project_slug }}',
        version=get_version(),
        description="{{ cookiecutter.project_short_description }}",
        author="{{ cookiecutter.full_name }}",
        author_email="{{ cookiecutter.email }}",
        url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
        packages=find_packages(where="src", exclude=["tests"]),
        package_dir={"": "src"},
        entry_points={
            'console_scripts': [
                '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.cli:cli',
            ]
        },
        install_requires=requirements,
        zip_safe=False,
        license="MIT",
        keywords='{{ cookiecutter.project_slug }}',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License (MIT)',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
    )
