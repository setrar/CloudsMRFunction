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


```
export PYTHONPATH=$(pwd); pytest test; unset PYTHONPATH
```
> Returns
```powershell
======================================================================================== test session starts ========================================================================================
platform darwin -- Python 3.11.10, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/valiha/Developer/CloudsMRFunction
plugins: anyio-4.0.0, embedded-1.3.5
collected 2 items                                                                                                                                                                                   

test/test_reducer.py .                                                                                                                                                                        [ 50%]
test/test_shuffler.py .                                                                                                                                                                       [100%]

========================================================================================= 2 passed in 0.02s =========================================================================================
```
