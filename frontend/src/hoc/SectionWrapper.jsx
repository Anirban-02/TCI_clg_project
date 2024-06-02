import React from 'react'
import { motion } from 'framer-motion'
import { staggerContainer } from '../utils/motion'


const SectionWrapper = (Component,idName) => 
function HOC(){
    return(
        <motion.section
        variants={staggerContainer()}
        initial='hidden'
        whileInView={"show"}
        viewport={{once:true,amount:0.25}}
        className={`sm:px-16 px-6 sm:py-24 py-12 w-full mx-auto relative z-0`}>
            <span className='hash-span' id={idName}></span>
            <Component/>
        </motion.section>
    )
}
export default SectionWrapper
