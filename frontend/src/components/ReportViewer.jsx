function ReportViewer({ report }) {
  return (
    <div>
      <h2>Final Report</h2>

      <pre
        style={{
          whiteSpace: "pre-wrap",
          wordBreak: "break-word",
          padding: "20px",
          border: "1px solid #ccc",
        }}
      >
        {report}
      </pre>
    </div>
  );
}

export default ReportViewer;