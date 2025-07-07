from setuptools import setup, find_packages

setup(
    name="medical_chatbot",
    version="0.1",
    packages=find_packages(),  # Automatically finds packages with __init__.py
    include_package_data=True,
    install_requires=[],
)