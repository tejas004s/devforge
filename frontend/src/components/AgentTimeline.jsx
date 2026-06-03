function AgentTimeline({ logs }) {
  return (
    <div>
      <h2>Agent Timeline</h2>

      {logs.length === 0 ? (
        <p>No agents executed yet.</p>
      ) : (
        logs.map((log, index) => (
          <div key={index}>
            <strong>{log.agent}</strong>
            {" - "}
            {log.duration}s
          </div>
        ))
      )}
    </div>
  );
}

export default AgentTimeline;