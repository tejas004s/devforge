import { useState } from "react";

import api from "./services/api";

import PromptForm from "./components/PromptForm";
import AgentTimeline from "./components/AgentTimeline";
import ReportViewer from "./components/ReportViewer";

function App() {
  const [report, setReport] =
    useState("");

  const [logs, setLogs] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const generatePlan = async (
    prompt
  ) => {
    try {
      setLoading(true);

      const response =
        await api.post(
          "/generate-plan",
          { prompt }
        );

      setReport(
        response.data.final_report
      );

      setLogs(
        response.data.execution_log
      );
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">

      <div className="hero">
        <h1>DevForge AI</h1>

        <p>
          Multi-Agent Software
          Architecture Generator
        </p>

        <div className="stats">
          <div className="stat-card">
            <div className="stat-number">
              5
            </div>

            <div className="stat-label">
              Agents
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-number">
              LangGraph
            </div>

            <div className="stat-label">
              Workflow Engine
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-number">
              FastAPI
            </div>

            <div className="stat-label">
              Backend
            </div>
          </div>
        </div>
      </div>

      <div className="glass-card">
        <PromptForm
          onSubmit={generatePlan}
          loading={loading}
        />
      </div>

      <div className="dashboard">

        <div className="left-panel">

          <div className="glass-card">
            <AgentTimeline
              logs={logs}
            />
          </div>

        </div>

        <div className="glass-card">

          <ReportViewer
            report={report}
          />

        </div>

      </div>

    </div>
  );
}

export default App;