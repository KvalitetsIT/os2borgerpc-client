from setuptools import setup
import subprocess
import sys

# Ensure the latest versions of setuptools and setuptools-scm are installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools>=61", "setuptools-scm>=8.0.0"])

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="os2borgerpc_client",
    use_scm_version=True,
    setup_requires=['setuptools>=61', 'setuptools-scm>=8.0.0'],  # Ensure correct versions
    description="Client for the OS2borgerPC system",
    long_description=long_description,
    url="https://github.com/OS2borgerPC/",
    author="Magenta ApS",
    author_email="info@magenta-aps.dk",
    license="GPLv3",
    packages=["os2borgerpc.client", "os2borgerpc.client.security"],
    install_requires=["PyYAML", "distro", "requests", "semver", "chardet"],
    scripts=[
        "bin/get_os2borgerpc_config",
        "bin/set_os2borgerpc_config",
        "bin/os2borgerpc_register_in_admin",
        "bin/os2borgerpc_push_config_keys",
        "bin/jobmanager",
        "bin/register_new_os2borgerpc_client.sh",
        "bin/admin_connect.sh",
        "bin/randomize_jobmanager.sh",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
