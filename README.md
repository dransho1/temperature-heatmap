# Atelier Ten Temperature Heatmap

This project uses  Kieran Timberlake Pointelist temperature sensors to create a heatmap over the A10 floorplan. It uses Bootstrap under the Django framework to create visualizations.

## TODO: ##
This is a work in progress. Things to do include:
* Navigating the API to gather relevant data for heatmaps
* Setting temperature zones in CSS (dynamically)
* Adding a chart below floorplan to show all sensors together (in last X measurements)

## File organization ##

'README.md
mysite/
	manage.py       			<-- contains commands to run server
	dbsqlite3
	mysite/						<-- contains internal Django settings
	temp/						<-- web app files
		views.py 				<-- webpage view
		kt.py 					<-- calls API
		models.py 				<-- app models
		urls.py 				<-- url's for webpage views
		static/
			temp/
				...css and js files
				images/
					fp.png 		<-- floorplan image
		templates/
			temp/
				index.html 		<-- html web app template'