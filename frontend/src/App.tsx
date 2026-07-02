import Welcome from "./component/Welcome";
import NavBar from "./component/NavBar";
import CompanyCard from "./component/CompanyCard";
import JobCard from "./component/JobCard";
import Footer from "./component/Footer";
import { useEffect, useState } from "react";
import { getCompanies } from "./services/CompanyService";
import type { Company } from "./types/company";

function App() {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);
    const [companies, setCompanies] = useState<Company[]>([]);

    async function fetchCompanies() {
        setLoading(true);
        try {
          const companies = await getCompanies();
          setCompanies(companies);
        }
        catch (error) {
          setError(error as Error);
        }
        finally {
          setLoading(false);
        }
    }

    useEffect(() => {
        fetchCompanies();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <>
        <NavBar/>
        <Welcome/>
        <br/>
        <CompanyCard companies={companies}/>
        <JobCard/>
        <Footer/> 
        </>
    )
}
   
export default App
