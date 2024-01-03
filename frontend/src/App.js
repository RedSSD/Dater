import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import InvitationPage from "./components/InvitationPage/InvitationPage";
import CreateInvitationPage from "./components/CreateInvitationPage/CreateInvitationPage";

function App() {
  return (
      <BrowserRouter>
          <div className="App">
              <Routes>
                  <Route path="/" element={<CreateInvitationPage />} />
                  <Route path="/:token" element={<InvitationPage />} />
              </Routes>
          </div>
      </BrowserRouter>

  );
}

export default App;
