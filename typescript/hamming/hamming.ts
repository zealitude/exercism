export default class Hamming{
  compute(a ='', b = ''){
    if(a.length != b.length){
      throw Error('DNA strands must be of equal length.')
    }
    
    var distance = 0;
    for (var idx = 0; idx < a.length; idx++) {
      if(a[idx]!=b[idx]){
        distance+=1;
      }
    }
    return distance;
  }
}