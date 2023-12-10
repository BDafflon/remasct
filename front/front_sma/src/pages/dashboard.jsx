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
import { getLayers } from '../componants/layers/layers';
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

const drawerWidth = 270;

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

  
export default function Dashboard() {
     
     const [hoverInfo, setHoverInfo] = React.useState();
     const [layers, setLayer] = React.useState([])
     const [filters, setFilters] = React.useState([])
     const [isLoading, toggleLoading] = React.useState(false)
      
     const [focus, setFocus] = React.useState()
    const [drawer, setDrawer] = React.useState(true)
      const [mapStyle, setMapStyle ]=React.useState("mapbox://styles/clement-marchal/clnn8nr9v002m01pa22h11072")
      const [simulation, setSimulation] = React.useState(undefined)

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

     
  
  useEffect(()=>{
    setLayer(getLayers(setHoverInfo,toggleLoading,setFocus))
  },[])
  
     
 
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
        <Stack direction="row" spacing={2} sx={{mt:2,ml:2}}>
    <Avatar
    onClick={()=>setMapStyle('mapbox://styles/mapbox/dark-v11')}
    variant="square"
        alt="Remy Sharp"
        src="/public/img/basemap/dark-v11.png"
        sx={{ width: 50, height: 50 }}
      />
      <Avatar
      onClick={()=>setMapStyle('mapbox://styles/clement-marchal/clnn8nr9v002m01pa22h11072')}
    variant="square"
        alt="Remy Sharp"
        src="/public/img/basemap/clnn8nr9v002m01pa22h11072.png"
        sx={{ width: 50, height: 50 }}
      />
    </Stack>

    <Box sx={{ overflow: 'auto' }}>
        <List
        dense
            sx={{ width: '95%', maxWidth: 240, bgcolor: 'background.paper', ml:2, mr:10 }}
            component="nav"
            aria-labelledby="nested-list-subheader"
            subheader={
                <ListSubheader component="div" id="nested-list-subheader">
                Layer: 
                </ListSubheader>
            }
            >
              {layers.map((value,id) => (
                
        <ListItem
          key={value}
        >
          {console.log(value.props)}
            <ListItemText
                 
                primary={<Typography variant="caption" >{value.props.id}</Typography>}
              />
              <ListItemIcon >
                 
                <IconButton aria-label="comments" >
                  {value.props.visible?<RemoveRedEyeIcon   />:<VisibilityOffIcon   />}
                </IconButton>
              </ListItemIcon >
         
        </ListItem>
      ))}
               
        </List>
         
           
        </Box>



      </Drawer>

      <Box component="main" sx={{ flexGrow: 1 }}>
        <Toolbar /> 
       
        <MapEcov simulation={simulation} mapStyle={mapStyle} layersDisplay={[...layers]}   hoverInfo={hoverInfo} setHoverInfo={setHoverInfo} focus={focus} />
         
      </Box>
    </Box>

    </>
  );
}
