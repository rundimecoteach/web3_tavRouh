//Parcours de fichier

let fs = require('fs');
let path = require('path');
let process = require("process");

let dir= "../Corpus_detourage/html/";
let outDir= "../UF/";

extractor = require('unfluff');

// Loop through all the files in the directory
fs.readdir(dir, function (err, files) {
  if (err) {
    console.error("Could not list the directory.", err);
    process.exit(1);
  }

  files.forEach(function (file, index) {
    // Make one pass and make the file complete
    fs.readFile(path.join(dir,file), 'utf-8', (err, data) => { 
      if (err) throw err; 
      content = extractor(data);
   
    
    fs.writeFile(path.join(outDir,file), content.text,'utf-8', (err) => { 
    if (err) throw err; 
})
  }) 
  }
  )
})


//Extraction



//


//Statistiques

