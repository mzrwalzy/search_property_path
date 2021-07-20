# search_property_path

v1.0, find the first appear property name in dict, list in python
## Example

Init arr as a empty list, and a obj, your target property input those into function search_property(obj, count=0, target, arr)

```python
    arr = []
    obj = {'a': 1, 'b': {'aa': 1, 'bb': [1, 2, {'c': 1}]}, 'cc': {'ccc': {'dd': {'v': [5, 6, {'x': [7]}]}}}}
    target = 7
    search_property(obj, 0, target, arr)
    result = ''
    for i in arr[::-1]:
        result += f'[{i}]' if isinstance(i, int) else f'[\'{i}\']'
```
## Result

In the result, arr is a reversed list which have path name or index

```python
arr = [0, 'x', 2, 'v', 'dd', 'ccc', 'cc']
result = ['cc']['ccc']['dd']['v'][2]['x'][0]
```

