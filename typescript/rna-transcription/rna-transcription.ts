export default class Transcriptor{
  
  toRna(input: string){
    
    let rnaMap:{[key:string]: string} = {
      'C': 'G',
      'G': 'C',
      'A': 'U',
      'T': 'A'
    };

    let output = '';
    for (var index = 0; index < input.length; index++) {
      let c = rnaMap[input[index]];
      if(c === undefined){
        throw "Invalid input DNA.";
      }
      output += c;
    }

    return output;
  }

}

console.log((new Transcriptor).toRna('ACGTGGTCTTAA'))