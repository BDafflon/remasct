import * as React from 'react';
import { useEffect } from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import ButtonAppBar from '../componants/appbar';
import MapEcov from '../componants/mapecov';
import { getIconLayer } from '../componants/layers/layers';
import IconButton from '@mui/material/IconButton';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import FastRewindIcon from '@mui/icons-material/FastRewind';
import FastForwardIcon from '@mui/icons-material/FastForward';
import PauseIcon from '@mui/icons-material/Pause';
import StopIcon from '@mui/icons-material/Stop';
import { socket } from './socket';
import { Typography } from '@mui/material';

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
    const [layers, setLayer] = React.useState([])
    const [iconLayer, setIconLayer]=React.useState(getIconLayer())
    const [control, setControl] = React.useState({speed:1,play:true})

  useEffect(() => {
    
    const timer = setTimeout(() =>  askUpdate(), 100)
    return () => clearTimeout(timer)
  }, [simulation]);

  const askUpdate=()=>{
    socket.timeout(5000).emit('create-something', 'value', () => {
      
    });
  }

  const update=(data)=>{
 
    setSimulation(JSON.parse(data))
    sim=JSON.parse(data)
    setControl({...sim.control})
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

     const handlePlayPause=(d)=>{
      socket.timeout(5000).emit('update-play-pause', d, () => {
      
      });

     }

     const handleStop=()=>{
      socket.timeout(5000).emit('update-stop', () => {
      
      });

     }

     const handleSpeed=(d)=>{
      socket.timeout(5000).emit('update-speed',d, () => {
      
      });

     }
 
     
 
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
        <Box sx={{ml:2, mt:2}} >
          <Typography variant="overline" display="block" gutterBottom >Control</Typography>
       
        <IconButton onClick={()=>handleSpeed(-0.1)} aria-label="delete">
          <FastRewindIcon />
        </IconButton>
        <IconButton onClick={()=>handlePlayPause(!control.play)} aria-label="delete">
          {control.play?<PauseIcon /> : <PlayArrowIcon />}
        </IconButton>
        <IconButton onClick={()=>handleStop()} aria-label="delete">
          <StopIcon />
        </IconButton>
       
        <IconButton onClick={()=>handleSpeed(0.1)} aria-label="delete">
          <FastForwardIcon />
        </IconButton>
        
        
        </Box>
      
        
 

      </Drawer>

      <Box component="main" sx={{ flexGrow: 1 }}>
        <Toolbar /> 
       
        <MapEcov simulation={simulation} mapStyle={mapStyle} layersDisplay={[...layers,...iconLayer]}   hoverInfo={hoverInfo} setHoverInfo={setHoverInfo} focus={focus} />
         
      </Box>
    </Box>

    </>
  );
}
