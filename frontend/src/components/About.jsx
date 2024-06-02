import React from 'react' ;
import SectionWrapper from '../hoc/SectionWrapper';
const About = () => {
  return (
    <div className=' h-fit mt-6 px-6 font-normal  text-gray-200'>
    <div className='text-[48px] text-gray-100 font-extrabold tracking-wide'> About Our Project</div>
    <p className=' text-[21px]  tracking-wide indent-24 mt-4'>
     <span className=' text-gray-50 font-semibold'>"Test Case Identification using NLTK"</span> epitomizes the collaborative efforts of a talented team comprising B.Tech final year 
     Computer Science students: <span className=' text-gray-50 font-semibold'>Anirban Ghosh, Bipashna Sadhukhan, Ahana Das, Sangramjit Roy and Archisman Das</span> . This pioneering project is designed to revolutionize the way C source code is analyzed and understood.
    </p>
    <p className=' text-[20px] tracking-wide indent-24 mt-6'>
      Our intuitive website serves as a gateway to a sophisticated <span className=' text-gray-50 font-semibold'>analysis tool</span> . 
      Users can seamlessly input their C code or upload existing files, initiating a transformative journey with a simple click of the <span className=' text-gray-50 font-semibold'>"Identify Test Cases"</span> button. 
      This action triggers a comprehensive analysis process powered by the Natural Language Toolkit (NLTK).
    The system meticulously identifies and categorizes vital elements within the code, 
    including  <span className=' text-gray-50 font-semibold'>"for," "while," and "do while" loops, both internal and external test cases, variable ranges, 
    and intricate conditional statements.</span>   By dissecting the code structure and logic, our tool equips developers 
    with invaluable insights, facilitating a deeper understanding and enhancing <span className=' text-gray-50 font-semibold'>debugging efficiency</span> .
    </p>
    <p className=' text-[20px] tracking-wide indent-24 mt-6'>
    Through meticulous attention to detail and unwavering dedication, our team has crafted a solution that 
    not only simplifies the <span className=' text-gray-50 font-semibold'>complexity </span> of C programming but also fosters a  culture of innovation and excellence. 
    <span className=' text-gray-50 font-semibold'>"Test Case Identification using NLTK"</span> stands as a testament to our commitment to advancing the field of computer 
    science and empowering <span className=' text-gray-50 font-semibold'>developers worldwide.</span>
    </p>

    </div>
  )
}

export default SectionWrapper(About,'about');
