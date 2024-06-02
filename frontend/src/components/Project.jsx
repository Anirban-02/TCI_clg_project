import React, { useState,useRef } from 'react' ;
import SectionWrapper from '../hoc/SectionWrapper';
import { motion } from 'framer-motion';
import axios from 'axios';


const Project = () => {
  const [fileName,setFileName]=useState('');
  const [fileContent,setFileContent]=useState('');
  const [fileOutput,setFileOutput]=useState('');
  const [upload,setUpload]=useState(false);
  let file=useRef(null);
  function handleFile(e){
    file = e.target.files[0];
    const reader =new FileReader();
    reader.readAsText(file);
    reader.onload=()=>{
      setFileName(file.name);
      setFileContent(reader.result);
      setFileOutput('');
    }
  }
  const handleUpload =async(e)=>{
    if (fileContent ==='')
      {
        window.alert('No files to upload')
      }
      else{
    try {
        //localhost:5000 ~ server side 
        const res = await axios.post('http://localhost:5000/api/input',
        {
            fileContent
        },
        {
            
            headers:{'Accept':'application/json, text/plain, /','Content-Type':'application/json'}
        });
        if(res.status === 422 || !res.data)
        {
            window.alert("error uploading file");
            console.log("error uploading");
        }
        else{
            setUpload(true);
            window.alert("File Uploaded");
            console.log("file uploaded");
            
            
        }  
    } catch (error) {
        console.log('here is the error : ',error,error.response) ;   
    }  
  }  
}

function enableTab(id) {
  var el = document.getElementById(id);
  el.onkeydown = function(e) {
      if (e.keyCode === 9) { // tab was pressed

          // get caret position/selection
          var val = this.value,
              start = this.selectionStart,
              end = this.selectionEnd;

          // set textarea value to: text before caret + tab + text after caret
          this.value = val.substring(0, start) + '\t' + val.substring(end);

          // put caret at right position again
          this.selectionStart = this.selectionEnd = start + 1;

          // prevent the focus lose
          return false;

      }
  };
}

const handleOutput =async(e)=>{
  if (!upload)
    {
      window.alert('No files uploaded')
    }
  else{
  try {
      //localhost:5000 ~ server side 
      const res = await axios.get("http://localhost:5000/api/output",{
        headers:{'Accept':'application/json, text/plain, /','Content-Type':'text/plain'}
    });
      if(res.status === 422 || !res.data)
      {
          window.alert("error in output");
          console.log("error uploading");
      }
      else{
          setFileOutput(res.data);
      }  
  } catch (error) {
      console.log('here is the error : ',error,error.response) ;   
  }  
}
}

  function handleInput(e){
    enableTab('input-text');
    setFileContent(e.target.value);
  }

  const handleReset=()=>{
    setFileContent(''); 
    setUpload(false); 
    setFileOutput('');
    if (file.current) {
      file.current.value = "";
      file.current.type = "text";
      file.current.type = "file";
  }
  }

  return (
    <>
      <div className=' mt-8 ml-12 text-[28px] font-medium '>Type or Upload your C flie :</div>
      <div className=' h-fit mt-1 flex justify-evenly '>
        <div className='flex flex-col w-2/5'>
          <textarea id='input-text' className=' bg-violet-500 mt-4 rounded-lg p-8 text-[18px] caret-white cursor-default '  onChange={handleInput} rows={12} value={fileContent} />
          <div className='mt-6 flex items-center justify-around '>
            <input type='file' ref={file} onChange={(e)=>handleFile(e)} ></input>
            <motion.button  whileTap={{scale:0.85}} className=' p-4 py-2 rounded-lg shadow-violet-950 shadow-md float-end text-[18px] font-medium'  onClick={()=>handleReset()}>Clear</motion.button>
            <motion.button  whileTap={{scale:0.85}} className=' p-4 py-2 ml-4 rounded-lg shadow-violet-950 shadow-md float-end text-[18px] font-medium text-nowrap' onClick={()=>handleUpload()}>Upload Code</motion.button>
          </div>
        </div>
        <div className='flex flex-col w-3/6 justify-center items-center '>
          <div className='h-[380px] w-full  bg-violet-500 p-8  caret-black overflow-y-scroll rounded-xl whitespace-pre-wrap font-normal text-[18px] ' >{fileOutput}</div>
          <motion.button  whileTap={{scale:0.85}} className=' p-4 py-2 mt-4 rounded-lg shadow-violet-950 shadow-md float-end text-[18px] font-medium' onClick={()=>handleOutput()}>Identify Test Cases</motion.button>
        </div>
      </div>
    </>
    
  )
}

export default SectionWrapper(Project,'project');