import './App.css';
import Home from "./pages/Home";
import FacilityLoginPage from "./pages/FacilityLogin";
import ContractorLoginPage from './pages/ContractorLogin';
import FacilityNew from "./pages/FacilityNew";
import Projects from "./pages/ProjectList";
import AllProjects from "./pages/AllProjects";
import ContractorNew from "./pages/ContractorNew";
import BidNew from "./pages/BidNew";
import ProjectNew from "./pages/ProjectNew";
import ProjectDetail from "./pages/ProjectDetail";

import { BrowserRouter, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element ={<Home/>}/>
          <Route path="/facility/login" element ={<FacilityLoginPage/>}/>
          <Route path="/contractor/login" element ={<ContractorLoginPage/>}/>
          <Route path="/facility/new" element ={<FacilityNew/>}/>
          <Route path="/contractor/new" element ={<ContractorNew/>}/>
          <Route path="/bid/new" element ={<BidNew/>}/>
          <Route path="/project/new" element ={<ProjectNew/>}/>
          <Route path="/projects" element ={<Projects/>}/>
          <Route path="/allprojects" element ={<AllProjects/>}/>
          <Route path="/project/detail" element ={<ProjectDetail/>}/>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
