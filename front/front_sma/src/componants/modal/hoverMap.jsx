import * as React from 'react';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

export default function HoverMap({text}) {
 

  return (
    <Box
      sx={{
        
        backgroundColor: 'rgba(0, 0, 0, 0)',
        flexGrow: 1,
        minWidth: 300,
        transform: 'translateZ(0)',
        
 
         
      }}
      
    >
      <Modal
        disablePortal
        disableEnforceFocus
        disableAutoFocus
        open
        aria-labelledby="server-modal-title"
        aria-describedby="server-modal-description"
        sx={{
            
          display: 'flex',
          p: 1,
          alignItems: 'center',
          justifyContent: 'center',
        }}
 
      >
        <Box
          sx={{
            position: 'relative',
            width: 450,
            bgcolor: 'background.paper',
            borderRadius:"10px",
            textAlign:'center'
          }}
        >
          <Typography id="server-modal-title" variant="h6" component="h2">
            {text}
          </Typography>
           
        </Box>
      </Modal>
    </Box>
  );
}
