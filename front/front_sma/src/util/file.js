export function exportFlowMapMetaData(layers,labels){
    let csvData="type;layer;name;edge_id;lnt;lat;\n"
    layers.forEach(element => {
      console.log(element)
      csvData+="flowmap;"+element.id+";"+element.name+";"+element.hash+";"+element.marker[0]+";"+element.marker[1]+";\n"
    });
    labels.forEach(element => {
        console.log(element)
        csvData+="label;"+element.layer.id+";"+element.text+";;"+element.coordinate[0]+";"+element.coordinate[1]+";\n"
      });
    const blob = new Blob([csvData], { type: 'text/json' })
    const al = document.createElement('a')  
    al.download = "exportFlowmap.csv"  
    al.href = window.URL.createObjectURL(blob)  
    const clickEvt = new MouseEvent('click', {    view: window,    bubbles: true,    cancelable: true,  })  
    al.dispatchEvent(clickEvt)  
    al.remove()

}
