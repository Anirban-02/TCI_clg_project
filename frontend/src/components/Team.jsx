import React from 'react' ;
import SectionWrapper from '../hoc/SectionWrapper';
import teamdata from '../assets/teamdata.json'
import { motion } from 'framer-motion';
import { fadeIn } from '../utils/motion';
const anime=(index)=>{
  return{
    hidden:{
      opacity:0, 
      x:-70
    },
    show:{
      opacity:1, 
      x:0,
      transition:
      { 
        duration:0.48,
        delay:0.28*index,
      },
    }
  }
}
const Team = () => {
  return (
    <div className=' h-fit mt-10'>
      <motion.div variants={fadeIn('','','0.1','0.6')} whileInView='show' className='text-[48px] font-extrabold tracking-wide'> Our Team</motion.div>
      <div className='flex justify-evenly flex-wrap  mt-6 '>
        {teamdata.map((mem,index)=>(
            <motion.div variants={anime(index)} initial='hidden' whileInView='show'  key={index} className='w-1/3 lg:w-1/6  h-[350px] p-5 flex flex-col items-center  text-[10px] rounded-[28px]'>
                <div className='w-48 h-48'>
                    <img src={mem.pic} className=' h-[100%] w-[100%] object-cover rounded-full ' />
                </div>
                <div className=' mt-6 px-1 py-3 w-full text-[16px] rounded-xl text-center font-semibold tracking-wide bg-violet-700 '>
                    <p>{mem.name}</p>
                    <p>{mem.rollno}</p>
                </div>
            </motion.div>
        ))}
      </div>
      
      
        
      


    </div>
  )
}

export default SectionWrapper(Team,'team');
