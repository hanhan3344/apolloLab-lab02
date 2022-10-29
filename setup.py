import setuptools


setuptools.setup(
    name="cyber_draw",
    version="1.0",
    author="hanhan3344",
    author_email="915489043@qq.com",
    description="To visualize '/apollo/canbus/chassis' and '/apollo/control'",
    long_description="cyber_draw",
    long_description_content_type="cyber_draw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'cyber_draw = cyber_draw.main:main',
        ],
    },
    python_requires=">=3.6",
)
