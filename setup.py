from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="console-quiz-game",
    version="1.0.0",
    author="Saurabh Patil",
    author_email="saurabhpatil@example.com",
    description="An interactive console-based quiz game with multiple categories and difficulty levels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaurabhPatil-393/Console-based-quiz-game-in-Python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment :: Quiz Games",
        "Topic :: Education :: Testing",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "quiz-game=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)