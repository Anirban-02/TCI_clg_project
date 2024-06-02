import React from 'react' ;
import SectionWrapper from '../hoc/SectionWrapper';
import { motion } from 'framer-motion';
import { fadeIn } from '../utils/motion';
const Home = () => {
  return (
    <div className=' min-h-[55vh] mt-[110px] px-8 flex flex-col items-center'>
      <div className=' w-full flex justify-center text-center flex-col gap-6'>
        <motion.img variants={fadeIn('','','0.5','1.1')} src='./img/icon.png' alt='img' className=' h-[138px] object-contain mix-blend-exclusion'/>
        <motion.p variants={fadeIn('up','','0.7','1.3')} className=' text-[58px] font-semibold tracking-wide'>
        Test Case Identification using NLTK
        </motion.p>
      </div>
      <motion.div variants={fadeIn('','','1.3','1.1')} className='text-[28px] text-gray-200 font-light tracking-widest'>'Identify Internal and External Test Cases'</motion.div>
      
      
      
    </div>
  )
}

export default SectionWrapper(Home,'home');
