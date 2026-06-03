import { useState } from "react";

import api from "./services/api";

import PromptForm from "./components/PromptForm";
import ExecutionLog from "./components/ExecutionLog";
import ReportViewer from "./components/ReportViewer";
import AgentTimeline from "./components/AgentTimeline";

function App() {
  const [loading, setLoading] =
    useState(false);

  const [report, setReport] =
    useState("");

  const [logs, setLogs] =
    useState([]);

  const generatePlan = async (
    prompt
  ) => {
    try {
      setLoading(true);

      const response =
        await api.post(
          "/generate-plan",
          {
            prompt,
          }
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
    <div
      style={{
        maxWidth: "1200px",
        margin: "0 auto",
        padding: "20px",
      }}
    >
      <h1>
        DevForge AI
      </h1>

      <PromptForm
        onSubmit={generatePlan}
        loading={loading}
      />

      <hr />

      <AgentTimeline
        logs={logs}
      />

      <hr />

      <ExecutionLog
        logs={logs}
      />

      <hr />

      <ReportViewer
        report={report}
      />
    </div>
  );
}

export default App;