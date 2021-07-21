# search_property_path

Find the first appearance property name in dict in python or get it in object in js.
## Example

Initialize arr as a empty list, a obj(dict) you want to get your property path and your target property input those into function search_property(obj, count=0, target, arr).

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

In the result, arr is a reversed list which have path name or index.

```python
arr = [0, 'x', 2, 'v', 'dd', 'ccc', 'cc']
result = ['cc']['ccc']['dd']['v'][2]['x'][0]
```
## JavaScript
Add a JavaScript version to find a first appear property name in object, get your path, tap arr to get result.

![image-20210721095604110](C:\Users\MENG\AppData\Roaming\Typora\typora-user-images\image-20210721095604110.png)
