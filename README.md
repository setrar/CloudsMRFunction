# MR Function




## Azurite

```
cd .azurite && azurite &
```

# Clear Cache

```
rm -rf .azurefunctions
rm -rf __pycache__
rm -rf .python_packages
pip install -r requirements.txt --target=.python_packages/lib/site-packages
```


## Tests

```
python test_reducer.py
```
> Reducer Output: {'word': 'example', 'total_count': 10}

```
python test_shuffler.py
```
> Shuffler Output: {'example': [1, 3], 'test': [2], 'demo': [4]}
