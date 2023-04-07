import asyncio
from aioantipublic import AntiPublic, AntiPublicError

async def main():
	antip = AntiPublic()

	try:
		bin_info = await antip.bin_info(bin='456647')
		print(bin_info)

		bin_info_list = await antip.bin_info_list(bins=['456647', '424242'])
		print(bin_info_list)

		check_public = await antip.check_public(cards=["4242424242424242", "4266845237252027"])
		print(check_public)
	except AntiPublicError as e:
		print(e)

if __name__ == '__main__':
	asyncio.run(main())
