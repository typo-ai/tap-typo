del /Q /F dist
pip uninstall tap-typo
python setup.py sdist bdist_wheel
REM python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
python -m twine upload dist/*
REM pip install --index-url https://test.pypi.org/simple/ --no-deps tap-typo