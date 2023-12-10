 


import {TripsLayer} from '@deck.gl/geo-layers';
import { PathLayer } from 'deck.gl';

 
 

// variables
const step = 5;
const intervalMS = 20; 


export default function TripLayer() {
   
   
 
    return new PathLayer({
 
      data: '/data/lane.json',
      getHeight:0,
      visible:true,
      dataTransform: (res) => {
        let data=[]
        
        res.features.forEach(element => {
            element.properties.timestamps=Array.from(Array(element.geometry.coordinates.length).keys())
            let line = []
            element.geometry.coordinates.forEach(e => {
                line.push([e[1],e[0]])
                
            });
            element.geometry = {...element.geometry,coordinates:line}
            data.push(element)
        });
        console.log("df",data)
        return data
        },
        pickable: true,
    widthScale: 20,
    widthMinPixels: 2,
    getPath: d => d.geometry.coordinates,
    getColor: d => [255,0,0],
    getWidth: d => 1
        
    });
  }
