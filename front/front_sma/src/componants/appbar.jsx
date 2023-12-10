import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuOpenIcon from '@mui/icons-material/MenuOpen';
import MenuIcon from '@mui/icons-material/Menu';
import DeleteIcon from '@mui/icons-material/Delete';
import SwapVertIcon from '@mui/icons-material/SwapVert'; 
import AppsIcon from '@mui/icons-material/Apps';
import { teal } from '@mui/material/colors';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';

export default function ButtonAppBar({study, setStudy, setDrawer, drawer}) {
  const [open, setOpen] = React.useState(false);
  const goHome = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

 
  return (
    <>
     <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {"Fermeture de l'étude ?"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
          Cette page vous demande de confirmer sa fermeture.
          Des données que vous avez saisies pourraient ne pas être enregistrées.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
        <Button  color="error" variant="contained" onClick={()=>setStudy(undefined)}>Confirmer</Button>
        <Button onClick={handleClose} autoFocus> Annuler </Button>
          
          
        </DialogActions>
      </Dialog>

    <AppBar className='appBar' position="fixed" sx={{backgroundColor:'#34495e', zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
        {<IconButton  aria-label="delete" onClick={()=>{setDrawer(!drawer)}}>
            {drawer?<MenuOpenIcon  sx={{ color: teal[50] }} />:<MenuIcon  sx={{ color: teal[50] }} />}
        </IconButton>}
        
            
          <Typography variant="h6" noWrap component="div">
              MAS MAAS?
            </Typography>
            <IconButton edge="end" sx={{ marginLeft: "auto" }} aria-label="switch" onClick={()=>goHome()} color="white" size="large">
              <ExitToAppIcon sx={{ color: teal[50] }} />
            </IconButton>
        
        </Toolbar>
      </AppBar>
      </>
  );
}