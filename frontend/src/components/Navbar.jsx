import React from 'react'
import {Link } from 'react-router-dom';
const Navbar = () => {
  return (
    <div >
      <div className='px-12 w-full h-[110px] top-0 z-20 flex justify-between  bg-violet-950 fixed'>
        
        <Link to='/'
          onClick={()=>{
          window.scrollTo(0,0);}} className=' text-gray-200 font-bold text-[58px] flex items-center'>
          <img src='./img/icon.png' className='h-[50px]'/>
          <div className='h-[50px] w-1 bg-white ml-4'/>
          <div className='ml-4' >
            TCI 
          </div>
          
        </Link>
        <div className='text-[28px] flex items-center font-semibold text-gray-200'>
          <ul className='flex gap-10 '>
            <li>
              <a href='#about'>About</a>
            </li>
            <li>
              <a href='#project'>Project</a>
            </li>
            <li>
              <a href='#team'>Team</a>
            </li>
          </ul>
        </div>
      </div>
       
    </div>
  )
}

export default Navbar
