import * as React from 'react';
import { useEffect } from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import ButtonAppBar from '../componants/appbar';
import MapEcov from '../componants/mapecov';
import HoverMap from '../componants/modal/hoverMap';
import Stack from '@mui/material/Stack';
import Avatar from '@mui/material/Avatar';
import { getIconLayer, getLayers } from '../componants/layers/layers';
import List from '@mui/material/List';
import ListSubheader from '@mui/material/ListSubheader';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import IconButton from '@mui/material/IconButton';
import { Button, Divider, TextField, Typography } from '@mui/material';
import OpenWithIcon from '@mui/icons-material/OpenWith';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import RemoveRedEyeIcon from '@mui/icons-material/RemoveRedEye';
import DeleteIcon from '@mui/icons-material/Delete';
import { lerp } from '../util/math';
import { socket } from './socket';
import IconLayerSma from '../componants/layers/iconlayer';

const drawerWidth = 270;
export var showAll = Date.now();  

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(50%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
  });

export var sim=undefined
export default function Dashboard() {
     
     
    const [hoverInfo, setHoverInfo] = React.useState();
     
    const [filters, setFilters] = React.useState([])
    const [isLoading, toggleLoading] = React.useState(false)
      
    const [focus, setFocus] = React.useState()
    const [drawer, setDrawer] = React.useState(true)
    const [mapStyle, setMapStyle ]=React.useState("https://basemaps.cartocdn.com/gl/positron-gl-style/style.json")
    const [simulation, setSimulation] = React.useState(undefined)
    const [layers, setLayer] = React.useState(getLayers(setHoverInfo,toggleLoading,setFocus))
    const [iconLayer, setIconLayer]=React.useState(getIconLayer())

  useEffect(() => {
    
    const timer = setTimeout(() =>  askUpdate(), 1000)
    return () => clearTimeout(timer)
  }, [simulation]);

  const askUpdate=()=>{
    socket.timeout(5000).emit('create-something', 'value', () => {
      
    });
  }

  const update=(data)=>{
 
    setSimulation(JSON.parse(data))
    sim=JSON.parse(data)
    let t=[]
    iconLayer.forEach(element => {
      t.push(element.clone({data:sim}))
    });
    setIconLayer(t)
    
  }
  useEffect(() => {
    

    function onConnect() {
      setIsConnected(true);
    }

    function onDisconnect() {
      setIsConnected(false);
    }

    function onFooEvent(value) {
      setFooEvents(previous => [...previous, value]);
    }
    

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on('update', (d)=>update(d));

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
    };
  }, []);

     
 
     
 
  return (
    <>
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <ButtonAppBar setDrawer={setDrawer} drawer={drawer}/>
      <Drawer
      open={drawer}
      variant="persistent"
        sx={{
           
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
        }}
      >
        <Toolbar  />
        
 

      </Drawer>

      <Box component="main" sx={{ flexGrow: 1 }}>
        <Toolbar /> 
       
        <MapEcov simulation={simulation} mapStyle={mapStyle} layersDisplay={[...layers,...iconLayer]}   hoverInfo={hoverInfo} setHoverInfo={setHoverInfo} focus={focus} />
         
      </Box>
    </Box>

    </>
  );
}
