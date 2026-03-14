from setuptools import setup, find_packages

setup(
    name="role_workspaces_app",
    version="0.0.1",
    description="Automatic role-based workspaces",
    author="Admin",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)