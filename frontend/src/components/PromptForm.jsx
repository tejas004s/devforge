import { useState } from "react";

function PromptForm({ onSubmit, loading }) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!prompt.trim()) return;

    onSubmit(prompt);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        rows={8}
        cols={100}
        placeholder="Describe your software project..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br />
      <br />

      <button
        type="submit"
        disabled={loading}
      >
        {loading
          ? "Generating..."
          : "Generate Plan"}
      </button>
    </form>
  );
}

export default PromptForm;