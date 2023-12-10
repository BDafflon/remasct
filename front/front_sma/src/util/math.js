export function lerp(value, istart, istop, ostart, ostop) {
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));
  }


export function getMin(arr,attr_l1,attr_l2){
    return arr.reduce((prev, curr) => prev[attr_l1][attr_l2] < curr[attr_l1][attr_l2] ? prev : curr);
}
export function getMax(arr,attr_l1,attr_l2){
    return arr.reduce((prev, curr) => prev[attr_l1][attr_l2] > curr[attr_l1][attr_l2] ? prev : curr);
}