from setuptools import setup, find_packages

setup(
    name="dpdp-sentinel",
    version="1.0.0",
    description="India DPDP Act 2023 Compliance Scanner — detects personal & sensitive data and maps findings to DPDP obligations, CERT-In §70B rules, and penalty tiers.",
    author="Helisha Balsara",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "dpdp-sentinel=dpdp_sentinel.main:main",
        ]
    },
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
