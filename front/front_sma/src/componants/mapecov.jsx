/// app.js
import React, { useRef, useState } from 'react';
import { useEffect } from 'react';
import DeckGL from '@deck.gl/react';
import Map, {
  Marker,
  NavigationControl,
  FullscreenControl,
  GeolocateControl,
  ScaleControl,
} from 'react-map-gl';
import {useControl} from 'react-map-gl';
import {MapboxOverlay} from '@deck.gl/mapbox/typed';
import 'mapbox-gl/dist/mapbox-gl.css';

import {FlyToInterpolator} from 'deck.gl';
import '../App.css';
import 'mapbox-gl/dist/mapbox-gl.css';

import { Box, Typography } from '@mui/material';


// Set your mapbox access token here
const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiY2xlbWVudC1tYXJjaGFsIiwiYSI6ImNrZm52bHRsNzBoMnoyeW1xeDIzMzQ3eWEifQ.wCMQImypxyKtVyKKbEu3jQ'

function DeckGLOverlay(props) {
  const overlay = useControl(() => new MapboxOverlay(props));
  overlay.setProps(props);
  return null;
}

const ICON = `M20.2,15.7L20.2,15.7c1.1-1.6,1.8-3.6,1.8-5.7c0-5.6-4.5-10-10-10S2,4.5,2,10c0,2,0.6,3.9,1.6,5.4c0,0.1,0.1,0.2,0.2,0.3
  c0,0,0.1,0.1,0.1,0.2c0.2,0.3,0.4,0.6,0.7,0.9c2.6,3.1,7.4,7.6,7.4,7.6s4.8-4.5,7.4-7.5c0.2-0.3,0.5-0.6,0.7-0.9
  C20.1,15.8,20.2,15.8,20.2,15.7z`;
  
// DeckGL react component
export default function MapEcov({mapStyle,layersDisplay, handleClickLayer,hoverInfo,setHoverInfo,focus,addingLayer,simulation}) {
  const mapRef = useRef(null)
  const [screen,setScreen] = useState({topleft:[0,0],bottomright:[0,0]})
  const [toolTipData,setToolTipData]=useState("")
  const [viewState, setViewState] = useState({
    latitude: 48.3,
    longitude: 2.333333,
    zoom: 5,
    bearing: 0,
    pitch: 0
  });
  
  useEffect(()=>{
    setToolTipData(hoverInfo)
 
  },[hoverInfo,mapStyle])

  useEffect(()=>{
    console.log("Focus",focus)
      if(focus !=undefined)
        mapRef.current?.easeTo({ center: [focus.longitude, focus.latitude],bearing:focus.bearing,zoom:focus.zoom,pitch:focus.pitch, duration:focus.transitionDuration*1000 })
  },[focus])

  const getLayersDisplay=(layersDisplay)=>{
    let layer=[]
    layersDisplay.forEach(element => {
      if(element != undefined)
        layer.push(element)
    });
    
    return layer
  }

  const tooltipMaker=(data)=>{
    if (data && data.object){
    let tooltip = ""
    for (const [key, value] of Object.entries(data.object.properties)) {
      tooltip+=key+"\t:\t\t"+value+"\n"
    }

    return tooltip}
  }


   

  return (
     <Box
     sx={{ height: "100vh"}} >
    <Map
    {...viewState}
    style={{ width: "100%" }}
    ref={mapRef}
    mapboxAccessToken={MAPBOX_ACCESS_TOKEN} 
    mapStyle={mapStyle}
    onMove={evt => {
      setViewState(evt.viewState)
      }}
    

  >
    <DeckGLOverlay 
     getTooltip={()=> tooltipMaker(toolTipData)}
    controller={true}
    getCursor={() => {
      if(addingLayer)
        if(toolTipData)
          return "pointer"
      return "auto"
    }}
    layers={[...getLayersDisplay(layersDisplay)]}
    onClick={(info, event) => { 
      if (info.object){
        if(info.object.properties.hash != undefined){
          console.log("handleClickLayer",info)
          let res = handleClickLayer(info.coordinate,info.object.properties,info.layer);
        }
      }

    }}
    onViewStateChange  ={(viewState)=>{
      setViewState(viewState.viewState)
    }}
    onDragEnd={(info,event)=>{
        if(info.viewport == undefined) return
        let x = info.viewport.unproject([-300,-300])
        let y = info.viewport.unproject([window.innerWidth+300,window.innerHeight+300])
        setScreen({...screen,topleft:x,bottomright:y})
    }}
    >



        


    </DeckGLOverlay>
    <NavigationControl showCompass={false} showZoom={true}/>
    <ScaleControl />
     

    
    

  </Map>
  </Box>


        
        

        
    )
}
