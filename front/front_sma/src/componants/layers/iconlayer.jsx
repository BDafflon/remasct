 

 
import { IconLayer } from 'deck.gl';
import { showAll, sim } from '../../pages/dashboard';

 
 

// variables
const step = 5;
const intervalMS = 20; 


export default function IconLayerSma() {
   
   
 
    return new IconLayer({
      id: 'icon-layer',
      data: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart-stations.json',
  
  /* props from IconLayer class */
  
  // alphaCutoff: 0.05,
  // billboard: true,
  // getAngle: 0,
  dataTransform: (res) => {
    console.log("res DT icon ",res)
    if (res.agents==undefined)
      return []
    let data=[]
    res.agents.forEach(element => {
      if(element.body.visible)
        data.push(element)
    });
    res.items.forEach(element => {
      data.push(element)
    });
    console.log(data)
    return data
  },
  getColor: d => {
    if(d.type=="CARPOOL")
      return [0,255,0]
    if(d.type=="Rider")
      return [0,0,255]
    if(d.type=="Driver")
      return [255,0,0]
  },
  getIcon: d => d.type=="Rider"?'rider':'driver',
  // getPixelOffset: [0, 0],
  getPosition: d => [d.body.pos[1],d.body.pos[0]],
  getSize: d => 5,
  iconAtlas: '/img/altas_sma.png',
  iconMapping: {
    rider: {
      x: 0,
      y: 740,
      width: 120,
      height: 120,
      anchorY: 128,
      mask: true
    },
    driver: {
      x: 0,
      y: 0,
      width: 120,
      height: 128,
      anchorY: 128,
      mask: true
    }
  },
  // onIconError: null,
   sizeMaxPixels: 25,
   sizeMinPixels: 25,
  sizeScale: 4,
   sizeUnits: 'pixels',
  // textureParameters: null,
  
  /* props inherited from Layer class */
  
  // autoHighlight: false,
  // coordinateOrigin: [0, 0, 0],
  // coordinateSystem: COORDINATE_SYSTEM.LNGLAT,
  // highlightColor: [0, 0, 128, 128],
  // modelMatrix: null,
  // opacity: 1,
  pickable: true,
  })
}
  
