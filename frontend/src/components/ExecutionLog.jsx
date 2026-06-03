function ExecutionLog({ logs }) {
  return (
    <div>
      <h2>Execution Log</h2>

      {logs.length === 0 ? (
        <p>No execution logs available.</p>
      ) : (
        <ul>
          {logs.map((log, index) => (
            <li key={index}>
              {typeof log === "string"
                ? log
                : `${log.agent} (${log.duration}s)`}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ExecutionLog;