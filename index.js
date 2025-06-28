const express = require('express')
const { spawn } = require('child_process');
spawn('node', ['index.js']);
const app = express()
const port=process.env.PORT||4000;
const cors=require('cors');
const path = require('path');
require('dotenv').config()
let file='';
app.use(cors(
    {
        origin:"https://tci-college-project.onrender.com",
        methods:["POST","GET"],
        credentials:true
    }
));
app.use(express.json());
app.use(express.static('public'));

app.get("/", (req, res) => {
    app.use(express.static(path.resolve(__dirname,"frontend","dist")));
    res.sendFile(path.resolve(__dirname,"frontend", "dist", "index.html"));
});

app.post('/api/input',(req,res)=>{
    file=req.body;
    res.send('thank you');
});
app.get('/api/input',(req,res)=>{
    res.send(file);
});
app.get('/api/output', (req, res) => {

    let dataToSend;
    // spawn new child process to call the python script 
    // and pass the variable values to the python script
    code="for(i=0;i<10;i++)"
    const python = spawn('python', ['./script.py',file['fileContent']]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    python.stderr.on('data',(data)=>{
        console.log(`error : ${data}`);
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });

});

app.listen(port, () => {
    console.log(`app is listening on port ${port}!`)
});
