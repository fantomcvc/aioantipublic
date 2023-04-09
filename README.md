<img src="https://i.ibb.co/y60NR16/1.jpg" alt="1" border="0" alight="center">

## Quickstart
1. Copy `aioantipublic/` folder into your project or `pip install aioantipublic`
2. Install dependencies `pip install -r aioantipublic/requirements.txt/`
3. See examples
4. Read the [documentation](https://docs.antipublic.cc/)

## Usage
1. `from aioantipublic import AntiPublic, AntiPublicError`
2. `antip = AntiPublic()`
3. See example
``` python
bin_info = await antip.bin_info(bin='456647')
print(bin_info)

check_public = await antip.check_public(cards=["4242424242424242", "4266845237252027"])
print(check_public)
```
## Exception handling

``` python
from aioantipublic import AntiPublic, AntiPublicError

antip = AntiPublic()
try:
	bin_info = await antip.bin_info(bin='111111')
	print(bin_info)
except AntiPublicError as e:
	print(e)
```
`> {'detail': 'BIN "111111" not found.'`

## License

Project Aioantipublic is distributed under the MIT license
