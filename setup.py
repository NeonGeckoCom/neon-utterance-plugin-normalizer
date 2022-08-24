#!/usr/bin/env python3
from os import path, getenv
from setuptools import setup, find_packages


def get_requirements(requirements_filename: str):
    requirements_file = path.join(path.abspath(path.dirname(__file__)), "requirements", requirements_filename)
    with open(requirements_file, 'r', encoding='utf-8') as r:
        requirements = r.readlines()
    requirements = [r.strip() for r in requirements if r.strip() and not r.strip().startswith("#")]

    for i in range(0, len(requirements)):
        r = requirements[i]
        if "@" in r:
            parts = [p.lower() if p.strip().startswith("git+http") else p for p in r.split('@')]
            r = "@".join(parts)
            if getenv("GITHUB_TOKEN"):
                if "github.com" in r:
                    r = r.replace("github.com", f"{getenv('GITHUB_TOKEN')}@github.com")
            requirements[i] = r
    return requirements


PLUGIN_ENTRY_POINT = 'neon_utterance_normalizer_plugin=neon_utterance_normalizer_plugin:UtteranceNormalizer'
setup(
    name='neon_utterance_normalizer_plugin',
    version='0.0.1',
    description='A utterance parser/classifier/transformer plugin for ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/neon_utterance_normalizer_plugin',
    author='Neongecko',
    author_email='developers@neon.ai',
    license='bsd3',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    zip_safe=True,
    keywords='mycroft plugin utterance parser/classifier/transformer',
    entry_points={'neon.plugin.text': PLUGIN_ENTRY_POINT}
)
