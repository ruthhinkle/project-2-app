# Plan Your Divvy Trip

Run this repository locally to find a bike station close to you or your destination, check the station's capacity to find available bikes, and bike to the nearest landmark. 

If you like to plan ahead, pick out a landmark or two and find the closest stations by looking at the map. 

## 📁 How to Install
To run on your local machine, clone this repository. No extra installation is necessary.

If you do run into issues, check the installation and file requirements for the following libraries: 
* [Leaflet](https://leafletjs.com/)
* [Leaflet MarkerCluster](https://github.com/Leaflet/Leaflet.markercluster) by [Leaflet](https://github.com/Leaflet)
* [Leaflet Ant-Path](https://github.com/rubenspgcavalcante/leaflet-ant-path) by [Rubens Pinheiro](https://github.com/rubenspgcavalcante)

If you can't reconcile installation issues, let us know!

## 💻 How to Run Locally
<strong>Step 1:</strong> Open your command prompt and navigate to the cloned directory.

<strong>Step 2:</strong> Create the database by entering: 
```
python create_database.py
```  

<strong>Step 3:</strong> Run app.py by entering:
```
python app.py 
```  
<strong>Step 4:</strong> Your command prompt will output the local server link. Copy and paste that into your browser.


## How to Use
<details> <summary markdown="span"><strong> 📍 Check Nearby Stations</strong></summary>
  To find a bike, check nearby stations and look at their status to see if there are bikes available. Light-blue pins indicate  stations full of bikes, dark-blue pins indicate stations with less than 5 bikes, and red pins indicate empty stations. When you're done with your ride, red stations are great place to drop off your bike.
</details>

<details> <summary markdown="span"><strong> 🗽 Visit Popular Landmarks</strong></summary>
    To add popular Chicago landmarks to the map, select the "Landmarks" layer view in the top right corner of the map. Zoom in to see nearby stations for bike pick-up or drop-off. You can click on Landmark pins to see their names.
</details>

<details> <summary markdown="span"><strong> 🚲 Follow Popular Routes</strong></summary>
    To add popular Chicago landmarks to the map, select the "Landmarks" layer view in the top right corner of the map. Zoom in to see nearby stations for bike pick-up or drop-off. You can click on Landmark pins to see their names.
</details>

<details> <summary markdown="span"><strong>🔎 Table View</strong></summary>
    Navigate to the table tab for a different view! You can search a street name to locate all of the stations on that street."
</details>


## Future Upgrades
* Add information about each destination when you click on the icon. 
* Reconcile the conflict between MarkerClusterGroups and layer toggles for Full, Low, and Empty stations
* Design a neutral template to be used with GBFS data from any other city following that data standard
* Heroku deployment

  
## ✍ Contributors:
* Andrew Neher - Project Manager, Designer, Landmark Lead
* Charlie Denys - Front End, Ant-Path Lead
* Drew McBride - Backend, Table View Lead
* Nabila Farooqi - Dev Ops, Deployment, Bike Type Lead
* Ruth Hinkle - Github Master, Documentation, Cluster/Layers Lead
