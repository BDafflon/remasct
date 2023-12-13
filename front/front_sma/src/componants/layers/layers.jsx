import IconLayerSma from "./iconlayer";
import TripLayer from "./triplayer";

 
export const getIconLayer=()=>{
    return [IconLayerSma(),]
}
export const getLayers = (setHoverInfo,toggleLoading,setFocus) => {
    return [
        TripLayer(),
    ];
  };
