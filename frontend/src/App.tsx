// import Welcome from "./component/Welcome";
import NavBar from "./component/NavBar";
import CompanyCard from "./component/CompanyCard";
import JobCard from "./component/JobCard";
import Footer from "./component/Footer";

import { useEffect, useState } from "react";

import {
  getCompanies,
  updateCompany,
  deleteCompany,
  createCompany,
} from "./Services/CompanyService";

import {
  getJobs,
  updateJob,
  deleteJob,
  createJob,
} from "./Services/JobService";

import type { Company } from "./types/company";
import type { Job } from "./types/job";

import Login from "./pages/login";
import Register from "./pages/Register";
import Chat from "./pages/Chat";