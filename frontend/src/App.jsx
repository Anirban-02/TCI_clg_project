import { useState } from 'react';
import Home from './components/Home'
import Navbar from './components/Navbar'
import About from './components/About';
import { BrowserRouter } from 'react-router-dom';
import Team from './components/Team';
import Project from './components/Project';
function App() {
  return (
    <>
    <BrowserRouter>
      <div className='relative w-full h-full bg-violet-800 '>
        <Navbar/>
        <Home/>
        <About/>
        <Project/>
        <Team/>
      </div>
    </BrowserRouter>
      
    </>
  )
}

export default App
