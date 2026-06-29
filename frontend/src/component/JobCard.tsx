function JobCard(){
    return (
        <div>
            <h1>Software Engineer</h1>
            <p>Google</p>
            <p>Bangalore</p>
            <p>5 LPA</p>
        </div>
    )
}
export default JobCard

import Welcome from './components/welcome';
import NavBar from './components/NavBar';
import CompanyCard from './components/CompanyCard';
import Footer from './components/Footer';
import JobCard from './components/JobCard';
function App(){
  return(
    <>
      <NavBar />
      <Welcome />
      <CompanyCard />
      <JobCard />
      <Footer />
    </>
  )
}
