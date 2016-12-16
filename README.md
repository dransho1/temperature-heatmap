# Atelier Ten Temperature Heatmap

This project uses  Kieran Timberlake Pointelist temperature sensors to create a heatmap over the A10 floorplan. It uses Bootstrap under the Django framework to create visualizations.

## TODO: ##
This is a work in progress. Things to do include:
* Navigating the API to gather relevant data for heatmaps
* Setting temperature zones in CSS (dynamically)
* Adding a chart below floorplan to show all sensors together (in last X measurements)

## File organization ##

1. README.md /n
2. mysite/
	1. manage.py       			<-- contains commands to run server
	2. dbsqlite3
	3. mysite/						<-- contains internal Django settings
	4. temp/						<-- web app files
		1. views.py 				<-- webpage view
		2. kt.py 					<-- calls API
		3. models.py 				<-- app models
		4. urls.py 				<-- url's for webpage views
		5. static/
			1. temp/
				1. ...css and js files
				2. images/
					1. fp.png 		<-- floorplan image
		6. templates/
			1. temp/
				1. index.html 		<-- html web app template