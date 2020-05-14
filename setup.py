import lucent
from setuptools import setup, find_packages

version = lucent.__version__

# test_deps = ["future", "twine", "pytest", "pytest-mock", "python-coveralls"]

# extras = {
#     "test": test_deps,
#     "tf": ["tensorflow>=1.6.0"],
#     "tf_gpu": ["tensorflow-gpu>=1.6.0"],
# }

setup(
    name="lucent",
    packages=find_packages(exclude=[]),
    version=version,
    description=(
        "Lucid for PyTorch. "
        "Collection of infrastructure and tools for research in "
        "neural network interpretability."
    ),
    author="The Lucent Authors",
    author_email="limsweekiat@gmail.com",
    url="https://github.com/greentfrapp/lucent",
    license="Apache License 2.0",
    keywords=[
        "pytorch",
        "tensor",
        "machine learning",
        "neural networks",
        "convolutional neural networks",
        "feature visualization",
        "optimization",
    ],
    install_requires=[
        "torch",
        "torchvision",
        "tqdm",
        "numpy",
        "ipython",
        "pillow",
        "future",
        "decorator",
    ],
    # setup_requires=["pytest-runner"],
    # tests_require=test_deps,
    # extras_require=extras,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)