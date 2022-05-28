import python_weather, asyncio, os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

async def getWeather(city):
	client = python_weather.Client(format=python_weather.IMPERIAL)
	clearConsole()
	try:
		weather = await client.find(city)
	except:
		print("City not found\n")
		await client.close()
		return
	print("CURRENT")
	print(weather.current.temperature)
	print("FORECAST")
	for fc in weather.forecasts:
		print(f"{fc.date}: {fc.temperature}")
	print("\n")
	await client.close()

while True == True:
	if __name__ == "__main__":
		loop = asyncio.get_event_loop()
		loop.run_until_complete(getWeather(input("What city? > ")))